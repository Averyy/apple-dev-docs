# Receiving iOS notifications on an accessory

**Framework**: Accessory Notifications

Create custom app extensions that manage notifications for your accessory.

#### Overview

When someone opts into notification forwarding for your accessory from their iPhone, the system identifies your accessory with the reference your companion app receives from [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit). The system prompts the person for permission to forward notifications to the accessory from the apps that they choose in the prompt.

Implement three extensions using the Accessory Notification framework to forward notifications securely:

- **[`AccessoryDataProvider`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryDataProvider)**: Receives notification content and prepares it for transmission.
- **[`AccessoryTransportSecurity`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryTransportSecurity)**: Manages cryptographic key exchange with your accessory.
- **[`AccessoryTransportAppExtension`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryTransportAppExtension)**: Relays encrypted data to your accessory over Bluetooth.

The system coordinates these extensions, encrypting notification data before transmission so that only your accessory can decrypt it.

> **Note**: The API will support relaying data to an accessory over the internet in a subsequent version of the framework.

Your accessory receives the notification data and decrypts it using [`HPKE (RFC9180)`](https://developer.apple.comhttps://datatracker.ietf.org/doc/rfc9180/) before parsing the notification details. Extract the notification properties such as title, subtitle, body, and any rich content you include in the transmission.

Alert for the notification on your accessory by presenting it on screen, playing a sound, or triggering a haptic. You can include a suggested alerting strategy in your transmission based on particular situations or hints the system provides.

#### Register for Notification Forwarding

To register your accessory’s companion app for notification forwarding, call the [`AccessoryNotificationCenter`](AccessoryNotificationCenter.md) class’s [`requestForwarding(for:)`](AccessoryNotificationCenter/requestForwarding(for:).md) method:

```swift
import AccessoryNotifications
import AccessorySetupKit

// Register the accessory with AccessorySetupKit.
let accessory: ASAccessory = /* ... */

// Prompt for permission to opt into notification forwarding.
let center = AccessoryNotificationCenter()
let result = try await center.requestForwarding(for: accessory)
```

The system prompts the person for permission to forward notifications and allows them to select the apps on their device that can provide notifications. When the person finishes interacting with the UI and dismisses the prompt, the [`requestForwarding(for:)`](AccessoryNotificationCenter/requestForwarding(for:).md) method returns the person’s choice in the [`ForwardingDecision`](forwardingdecision.md) result. The [`ForwardingDecision.allow`](forwardingdecision/allow.md) value indicates that the person allows your accessory to receive notifications from all applicable apps. If the result is [`ForwardingDecision.limited`](forwardingdecision/limited.md), your accessory can receive notifications from a subset of apps. The other decision types indicate the person doesn’t opt into notification forwarding.

#### Create an Extension to Receive Notifications

To receive notification content, create an [`AccessoryDataProvider`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryDataProvider) extension in your accessory’s companion app by adding a new target to your Xcode project with the app extension type. In the extension’s target properties, specify the extension point identifier `com.apple.accessory-data-provider` and declare a capability for `AccessoryNotifications.NotificationsForwarding`:

```xml
<plist>
    <dict>
        <key>EXAppExtensionAttributes</key>
        <dict>
            <key>EXExtensionPointIdentifier</key>
            <string>com.apple.accessory-data-provider</string>
            <key>EXCapabilities</key>
            <array>
                <string>AccessoryNotifications.NotificationsForwarding</string>
            </array>
        </dict>
    </dict>
</plist>
```

In your extension’s code, implement the [`AccessoryDataProvider`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryDataProvider) protocol and provide a handler that conforms to [`NotificationsForwarding.AccessoryNotificationsHandler`](notificationsforwarding/accessorynotificationshandler.md):

```swift
import AccessoryNotifications
import AccessoryTransportExtension

@main
struct DataProvider: AccessoryDataProvider {
    var extensionPoint: AppExtensionPoint {
        Identifier("com.apple.accessory-data-provider")
        Implementing {
            NotificationsForwarding {
                NotificationHandler()
            }
        }
    }
}
// Responds to system-related notification requests.
class NotificationHandler: AccessoryNotificationsHandler {
    var session: NotificationsForwarding.Session?
    
    func activate(for session: NotificationsForwarding.Session) {
        self.session = session
    }
    
    func add(notification: AccessoryNotification, 
             alertingContext: AlertingContext, 
             alertCoordinator: AlertCoordinating) {
        // Curate the notification details for your accessory.
    }
    
    func update(notification: AccessoryNotification) {
        // Accommodate updated notification data.
    }
    
    func remove(notification: AccessoryNotification) {
        // Remove a previously displayed notification.
    }
    
    func removeAllNotifications() {
        // Remove all notifications.
    }
}
```

#### Receive and Process Notifications

When a notification occurs on the iPhone, the system invokes your extension by calling [`activate(for:)`](notificationsforwarding/accessorynotificationshandler/activate(for:).md), passing in a session object. Save a reference to the session for use across multiple notifications.

The system then calls `NotificationsForwarding/AccessoryNotificationsHandler/add(notification:alertingContext:alertCoordinator:)` on your extension, passing in the notification’s details. Parse the [`AccessoryNotification`](accessorynotification.md) structure, selecting just the information your accessory needs. Notification details include:

- **Display content**: [`title`](accessorynotification/title.md), [`subtitle`](accessorynotification/subtitle.md), and [`summary`](accessorynotification/summary.md) (for Apple Intelligence summaries)
- **Rich elements**: [`sourceIcon`](accessorynotification/sourceicon.md), [`contextIcon`](accessorynotification/contexticon.md), [`attachments`](accessorynotification/attachments.md), and [`body`](accessorynotification/body.md), which can contain a genmoji through the [`NSAdaptiveImageGlyph`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/nsadaptiveimageglyph) class
- **Interactive components**: [`actions`](accessorynotification/actions.md) array
- **Metadata**: [`identifier`](accessorynotification/identifier-swift.property.md), [`sourceName`](accessorynotification/sourcename.md), [`threadIdentifier`](accessorynotification/threadidentifier.md), [`deliveryDate`](accessorynotification/deliverydate.md), and [`displayDate`](accessorynotification/displaydate-swift.property.md)
- **Priority attributes**: [`attributes`](accessorynotification/attributes-swift.property.md) for critical, time-sensitive, or priority notifications

Serialize the notification details you select and create an [`AccessoryMessage`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryMessage) to send the curated data to your accessory:

```swift
func add(notification: AccessoryNotification, 
         alertingContext: AlertingContext, 
         alertCoordinator: AlertCoordinating) {
    // Check if the notification needs to alert.
    guard alertingContext.shouldAlert else {
        alertCoordinator.complete(didAlert: false)
        return
    }
    
    // Extract and serialize notification data.
    let notificationData = serializeNotification(notification)
    
    // Create a message payload.
    let message = AccessoryMessage {
        AccessoryMessage.Payload(transport: .bluetooth, data: notificationData)
    }    
    // Send the message payload to your accessory.
    Task {
        do {
            try await session?.sendMessage(message)
            alertCoordinator.complete(didAlert: true)
        } catch {
            alertCoordinator.fail(error)
        }
    }
}
// Chooses fields the accessory supports and implements a custom binary format.
func serializeNotification(_ notification: AccessoryNotification) -> Data {
    var data = Data()
    // Add title, subtitle, body, and so on.
    return data
}
```

You can send one message per notification, or you can partition the data for a single notification into multiple payloads.

#### Create an Extension to Send Notifications Securely

Create an [`AccessoryTransportSecurity`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryTransportSecurity) extension to prepare for notification encryption, which involves sharing cryptographic items between your accessory, app extension, and the system. Add a new extension target to your Xcode project. In the extension’s target properties, specify the extension point identifier `com.apple.accessory-transport-security`:

```xml
<plist>
    <dict>
        <key>EXAppExtensionAttributes</key>
        <dict>
            <key>EXExtensionPointIdentifier</key>
            <string>com.apple.accessory-transport-security</string>
        </dict>
    </dict>
</plist>
```

In your extension’s code, implement the [`AccessoryTransportSecurity`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryTransportSecurity) protocol, in which you [`accept(_:)`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessorySecuritySession/Request/accept(_:)) incoming security session requests for your accessory:

```swift
import AccessoryTransportExtension
import CryptoKit

@main
struct TransportSecurity: AccessoryTransportSecurity {
    @AppExtensionPoint.Bind
    static var boundExtensionPoint: AppExtensionPoint {
        Identifier("com.apple.accessory-transport-security")
    }
    
    func accept(sessionRequest: AccessorySecuritySession.Request) -> AccessorySecuritySession.Request.Decision {
        return sessionRequest.accept {
            SecurityEventHandler(session: sessionRequest.session)
        }
    }
}
```

#### Provide a Security Event Handler

The security extension assists with cryptography by calling your app at various stages in the notification data encryption process. Provide an event handler that conforms to the [`AccessorySecuritySession`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessorySecuritySession) class’s [`AccessorySecuritySession.EventHandler`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessorySecuritySession/EventHandler) protocol. The system calls your handler’s doc://com.apple.documentation/documentation/accessorytransportextension/AccessorySecuritySession/EventHandler/securityEventHandler(event:) method with security events that represent each stage of the process, doc://com.apple.documentation/documentation/accessorytransportextension/AccessorySecurity/Event/keyRequest and doc://com.apple.documentation/documentation/accessorytransportextension/AccessorySecurity/Event/keyExchange(keyMaterial:):

```swift
class SecurityEventHandler: AccessorySecuritySession.EventHandler {
    private var session: AccessorySecuritySession
    private var keyMaterial: AccessorySecurity.Crypto.KeyMaterial?
    private var publicKeyData: Data?
    private var privateKeyData: Data?
    
    init(session: AccessorySecuritySession) {
        self.session = session
    }    
    func securityEventHandler(event: AccessorySecurity.Event) {
        switch event {
        case .keyRequest:
            handleKeyRequest()
        case .keyExchange(let keyMaterial):
            handleKeyExchange(keyMaterial: keyMaterial)
        default:
            break
        }
    }
    // Cleans up key material.    
    func invalidationHandler(error: (any Error)?) {
        keyMaterial = nil
        privateKeyData = nil
        publicKeyData = nil
    }
}
```

#### Respond to a Key Request

When the system sends a doc://com.apple.documentation/documentation/accessorytransportextension/AccessorySecurity/Event/keyRequest event, generate a public-private key pair on your accessory and return the public key to the system. Choose doc://com.apple.documentation/documentation/accessorytransportextension/AccessorySecurity/Crypto/Ciphersuite/XWing for the highest level of security, or doc://com.apple.documentation/documentation/accessorytransportextension/AccessorySecurity/Crypto/Ciphersuite/P256 as a fallback, if your accessory doesn’t support doc://com.apple.documentation/documentation/accessorytransportextension/AccessorySecurity/Crypto/Ciphersuite/XWing:

```swift
func handleKeyRequest() {
    do {
        // Generate an XWing key pair.
        let privateKey = try XWingMLKEM768X25519.PrivateKey()
        privateKeyData = privateKey.seedRepresentation
        publicKeyData = privateKey.publicKey.rawRepresentation
        
        // Return the public key to the system.
        let event: AccessorySecurity.Event = .keyReply(
            ciphersuite: .XWing,
            publicKey: publicKeyData
        )
        try session.sendSecurityEvent(event)
    } catch {
        session.cancel(error: error)
    }
}
```

The following example uses the doc://com.apple.documentation/documentation/accessorytransportextension/AccessorySecurity/Crypto/Ciphersuite/P256 fallback ciphersuite:

```swift
let privateKey = P256.KeyAgreement.PrivateKey()
privateKeyData = privateKey.rawRepresentation
publicKeyData = privateKey.publicKey.rawRepresentation

let event: AccessorySecurity.Event = .keyReply(
    ciphersuite: .P256,
    publicKey: publicKeyData
)
```

#### Facilitate a Key Exchange

The system generates cryptographic key material and sends it to your extension by invoking the doc://com.apple.documentation/documentation/accessorytransportextension/AccessorySecurity/Event/keyExchange(keyMaterial:) event. Forward the key material to your accessory so it can derive shared encryption keys, as required by the [`HPKE (RFC9180)`](https://developer.apple.comhttps://datatracker.ietf.org/doc/rfc9180/) specification:

```swift
func handleKeyExchange(keyMaterial: AccessorySecurity.Crypto.KeyMaterial) {
    guard let privateKeyData = privateKeyData,
          let publicKeyData = publicKeyData else {
        session.cancel(error: nil)
        return
    }
    
    self.keyMaterial = keyMaterial
    
    do {
        // Send key material to the accessory via Bluetooth.
        sendKeyMaterialToAccessory(keyMaterial)
        
        // Receive encapsulated key from the accessory.
        let encapsulatedKey = receiveEncapsulatedKeyFromAccessory()
        
        // Send encapsulated key to the system.
        let event: AccessorySecurity.Event = .encapsulatedKey(encapsulatedKey)
        try session.sendSecurityEvent(event)
    } catch {
        session.cancel(error: error)
    }
}
```

#### Implement an Extension to Relay Encrypted Notifications

To send the encrypted data to your accessory, use an [`AccessoryTransportAppExtension`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryTransportAppExtension). Implement the [`dataEventHandler(event:)`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryTransportSession/EventHandler/dataEventHandler(event:)) method in your event processing code, and the system calls your handler to transmit encrypted data for each message payload:

```swift
class TransportEventHandler: AccessoryTransportSession.EventHandler {
    func dataEventHandler(event: AccessoryTransportSession.DataEvent) {
        switch event {
        case .ciphertext(let data, let featureID):
            // Transmit encrypted notification data and the provided feature ID 
            //  to the accessory over Bluetooth.
            sendToAccessory(data, featureID)
        }
    }    
    func invalidationHandler(error: AccessoryTransportSession.Error?) {
        // Clean up when the session ends.
    }
}
```

The system encrypts notification data using keys exchanged through your [`AccessoryTransportSecurity`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryTransportSecurity) extension before delivering it as ciphertext to your handler. Because the data is encrypted, your extension is unable to read or otherwise make sense of the data, and can only transmit it.

#### Decrypt Notification Data on Your Accessory

When your accessory receives the encrypted notification data, it decrypts the data using [`HPKE (RFC9180)`](https://developer.apple.comhttps://datatracker.ietf.org/doc/rfc9180/) with keys exchanged through the transport security extension.

The accessory and extension share a secret, that is, a custom string phrase, for the HPKE decryption algorithm. Build the string using information about the protocol and key material:

```swift
let ciphersuite = keyMaterial.ciphersuite.description  // The value is "XWing" or "P256".
let version = keyMaterial.version.description          // Always "v1".
let identifier = keyMaterial.identifier                // The device's UUID.
let protocolInfo = Data("\(ciphersuite)-\(version)-\(identifier)".utf8)
```

Create an HPKE receiver from the accessory’s private key and protocol information. The following code uses the doc://com.apple.documentation/documentation/accessorytransportextension/AccessorySecurity/Crypto/Ciphersuite/XWing ciphersuite:

```swift
let publicKey = try XWingMLKEM768X25519.PublicKey(rawRepresentation: accessoryPublicKeyData)
let privateKey = try XWingMLKEM768X25519.PrivateKey(
    seedRepresentation: accessoryPrivateKeyData,
    publicKey: publicKey
)

let recipient = try HPKE.Recipient(
    privateKey: privateKey,
    ciphersuite: .XWingMLKEM768X25519_SHA256_AES_GCM_256,
    info: protocolInfo,
    encapsulatedKey: keyMaterial.encapsulatedKey
)
```

Alternatively, the following code creates an HPKE receiver using the fallback doc://com.apple.documentation/documentation/accessorytransportextension/AccessorySecurity/Crypto/Ciphersuite/P256 cipherstuite:

```swift
let privateKey = try P256.KeyAgreement.PrivateKey(rawRepresentation: accessoryPrivateKeyData)

let recipient = try HPKE.Recipient(
    privateKey: privateKey,
    ciphersuite: .P256_SHA256_AES_GCM_256,
    info: protocolInfo,
    encapsulatedKey: keyMaterial.encapsulatedKey
)
```

Derive a notification forwarding-specific secret by appending the direction and feature ID to the protocol information:

```swift
let featureID = /* Value received from the DataEvent. */   
let context = Data("\(protocolInfo)-HostToAccessory-\(featureID)".utf8)
let secret = try recipient.exportSecret(context: context, outputByteCount: 32)
```

The direction is `HostToAccessory` for data that flows from the iPhone to the accessory, and `AccessoryToHost` for data that flows from the accessory to the iPhone.

The system encrypts notification data using AES-GCM as specified in NIST Special Publication 800-38D. The ciphertext on the wire encodes as:

```None
IV (12 bytes) || ciphertext || MAC (16 bytes)
```

Decrypt the data using the feature-specific secret:

```swift
let sealedBox = try AES.GCM.SealedBox(combined: encryptedData)
let plaintext = try AES.GCM.open(sealedBox, using: secret)
```

If decryption fails, close the connection, reset the encryption state, and resynchronize the key exchange. If decryption succeeds, parse the notification information according to your accessory’s custom format.

#### Alert Someone About a Notification

To alert for a notification, present it on screen, play a sound, or trigger a haptic on your accessory device.

Use the [`AlertingContext`](alertingcontext.md) to determine whether a notification requires an alert. The system provides the [`shouldAlert`](alertingcontext/shouldalert.md) property, which represents the person’s preferred notification behavior using notification settings and the iOS device’s current Focus state.

The [`notificationCanAlert`](alertingcontext/notificationcanalert.md) property indicates whether the notification has sound and alert permissions. The system might set [`notificationCanAlert`](alertingcontext/notificationcanalert.md) to `false` when the notification already alerts on another device or if device settings disable alerting for the notification.

The [`isSuppressedByFocus`](alertingcontext/issuppressedbyfocus.md) property indicates whether the device’s Focus state suppresses notification alerts.

#### Send Information Back to the App

To confirm that the accessory has received and alerted for a notification, the accessory sends information back to the app.

> ❗ **Important**: The API will support receiving information from the accessory in a subsequent version of the framework.

The accessory starts by transmitting the information over Bluetooth to your transport extension, and your app’s extensions use doc://com.apple.documentation/documentation/accessorytransportextension/accessorytransportsession/senddata(_:featureid:) along with the following API, depending on the type of status:

- Confirmation of alerting success (see `AlertCoordinating`). Your extension calls `AlertCoordinating/complete(didAlert:)` or `AlertCoordinating/fail(_:)`, depending on the outcome.
- A person’s interaction with a notification (see `AccessoryNotificationManaging` and [`AccessoryNotification`](accessorynotification.md)). For example, the accessory reports whether the person invokes the notification’s default action by tapping the notification ([`AccessoryNotification.Action`](accessorynotification/action.md)), or whether the person provides text back to the app ([`userText`](notificationresponse/usertext.md)), for text-based notifications.

#### Handle Notification Updates and Removals

The forwarding life cycle includes requests to update a notification after your accessory receives it, or to remove one or more existing notifications.

When a notification’s content changes, the system notifies your extension by calling `NotificationsForwarding/AccessoryNotificationsHandler/update(notification:)`. Update the notification on your accessory without alerting again:

```swift
func update(notification: AccessoryNotification) {
    let notificationData = serializeNotification(notification)
    let message = AccessoryMessage {
        AccessoryMessage.Payload(transport: .bluetooth, data: notificationData)
    }
    Task {
        try await session?.sendMessage(message)
    }
}
```

If someone dismisses a notification on another device after your accessory receives the notification, the system follows up with a removal request by calling `NotificationsForwarding/AccessoryNotificationsHandler/remove(notification:)`:

```swift
// Requests the removal of a notification from the accessory.
func remove(notification: AccessoryNotification) {
    let removalData = serializeRemoval(notification.identifier)
    let message = AccessoryMessage {
        AccessoryMessage.Payload(transport: .bluetooth, data: removalData)
    }
    Task {
        try await session?.sendMessage(message)
    }
}
```

The system calls [`removeAllNotifications()`](notificationsforwarding/accessorynotificationshandler/removeallnotifications().md) when your accessory needs to remove all notifications, such as when the person deletes the app that sent the notifications:

```swift
// Requests the removal of all notifications from the accessory.
func removeAllNotifications() {
    let clearData = serializeClearAll()
    let message = AccessoryMessage {
        AccessoryMessage.Payload(transport: .bluetooth, data: clearData)
    }    
    Task {
        try await session?.sendMessage(message)
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/receiving-ios-notifications-on-an-accessory)*