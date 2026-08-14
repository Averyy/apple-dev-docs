# Receiving iOS notifications on an accessory

**Framework**: Accessory Transport Extension

Create custom app extensions that manage iOS system notifications for your accessory.

#### Overview

When someone opts into notification forwarding for your accessory from their iPhone, the system identifies your accessory with the reference your companion app receives from [`AccessorySetupKit`](https://developer.apple.com/documentation/accessorysetupkit). The system prompts the person for permission to forward notifications to the accessory from the apps that they choose in the prompt.

Implement three extensions using the [`Accessory Notifications`](https://developer.apple.com/documentation/accessorynotifications) framework to forward notifications securely:

- **[`AccessoryDataProvider`](accessorydataprovider.md)**: Receives notification content and prepares it for transmission.
- **[`AccessoryTransportSecurity`](accessorytransportsecurity.md)**: Manages cryptographic key exchange with your accessory.
- **[`AccessoryTransportAppExtension`](accessorytransportappextension.md)**: Relays encrypted data to your accessory over Bluetooth.

The system coordinates these extensions, encrypting notification data before transmission so that only your accessory can decrypt it.

Your accessory receives the notification data and decrypts it using [`HPKE (RFC9180)`](https://developer.apple.comhttps://datatracker.ietf.org/doc/rfc9180/) before parsing the notification details. Extract the notification properties such as title, subtitle, body, and any rich content you include in the transmission.

Alert for the notification on your accessory by presenting it on screen, playing a sound, or triggering a haptic effect that uses touch to give users feedback. You can include a suggested alerting strategy in your transmission based on particular situations or hints the system provides.

#### Register for Notification Forwarding

To register your accessory’s companion app for notification forwarding, call the [`AccessoryNotificationCenter`](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationcenter) class’s [`requestForwarding(for:)`](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationcenter/requestforwarding(for:)) method:

```swift
import AccessoryNotifications
import AccessorySetupKit

// Register the accessory with AccessorySetupKit.
let accessory: ASAccessory = /* ... */

// Prompt for permission to opt into notification forwarding.
let center = AccessoryNotificationCenter()
let result = try await center.requestForwarding(for: accessory)
```

The system prompts the person for permission to forward notifications and allows them to select the apps on their device that can provide notifications. When the person finishes interacting with the UI and dismisses the prompt, the [`requestForwarding(for:)`](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationcenter/requestforwarding(for:)) method returns the person’s choice in the [`ForwardingDecision`](https://developer.apple.com/documentation/accessorynotifications/forwardingdecision) result. The [`ForwardingDecision.allow`](https://developer.apple.com/documentation/accessorynotifications/forwardingdecision/allow) value indicates that the person allows your accessory to receive notifications from all applicable apps. If the result is [`ForwardingDecision.limited`](https://developer.apple.com/documentation/accessorynotifications/forwardingdecision/limited), your accessory can receive notifications from a subset of apps. The other decision types indicate the person doesn’t opt into notification forwarding.

#### Create an Extension to Receive Notifications

To receive notification content, create an [`AccessoryDataProvider`](accessorydataprovider.md) extension in your accessory’s companion app by adding a new target to your Xcode project with the app extension type. In the extension’s target properties, specify the extension point identifier `com.apple.accessory-data-provider` and declare a capability for `AccessoryNotifications.NotificationsForwarding`:

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

In your extension’s code, implement the [`AccessoryDataProvider`](accessorydataprovider.md) protocol and provide a handler that conforms to [`NotificationsForwarding.AccessoryNotificationsHandler`](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler):

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
    
    func didActivate(for session: NotificationsForwarding.Session) {
        self.session = session
    }
    
    func addNotification(_ notification: AccessoryNotification, 
                        alertingContext: AlertingContext) async throws -> Bool {
        // Curate the notification details for your accessory.
    }
    
    func updateNotification(_ notification: AccessoryNotification) {
        // Accommodate updated notification data.
    }
    
    func removeNotification(identifier: AccessoryNotification.Identifier) {
        // Remove a previously displayed notification.
    }
    
    func removeAllNotifications() {
        // Remove all notifications.
    }
    
    func messageHandler(_ message: AccessoryMessage) {
        // Handle messages from the accessory.
    }
    
    func didInvalidate() {
        // Clean up when the session ends.
    }
}
```

The system requires your app extension to have the [`com.apple.developer.accessory-data-provider`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.accessory-data-provider) entitlement to use the [`AccessoryDataProvider`](accessorydataprovider.md) protocol.

#### Receive and Process Notifications

When a notification occurs on the iPhone, the system invokes your extension by calling [`didActivate(for:)`](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler/didactivate(for:)), passing in a session object. Save a reference to the session for use across multiple notifications.

The system then calls [`addNotification(_:alertingContext:)`](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler/addnotification(_:alertingcontext:)) on your extension, passing in the notification’s details. Parse the [`AccessoryNotification`](https://developer.apple.com/documentation/accessorynotifications/accessorynotification) structure, selecting just the information your accessory needs. Notification details include:

- **Display content**: [`title`](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/title), [`subtitle`](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/subtitle), and [`summary`](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/summary) (for Apple Intelligence summaries)
- **Rich elements**: [`sourceIcon`](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/sourceicon), [`contextIcon`](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/contexticon), [`attachments`](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/attachments), and [`body`](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/body), which can contain a genmoji through the [`NSAdaptiveImageGlyph`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/nsadaptiveimageglyph) class
- **Interactive components**: [`actions`](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/actions) array
- **Metadata**: [`identifier`](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/identifier-swift.property), [`sourceName`](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/sourcename), [`threadIdentifier`](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/threadidentifier), [`deliveryDate`](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/deliverydate), and [`displayDate`](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/displaydate-swift.property)
- **Priority attributes**: [`attributes`](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/attributes-swift.property) for critical, time-sensitive, or priority notifications

Serialize the notification details you select and create an [`AccessoryMessage`](accessorymessage.md) to send the curated data to your accessory:

```swift
func addNotification(_ notification: AccessoryNotification, 
                    alertingContext: AlertingContext) async throws -> Bool {
    // Check if the notification needs to alert.
    guard alertingContext.shouldAlert else {
        return false
    }
    
    // Extract and serialize notification data.
    let notificationData = serializeNotification(notification)
    
    // Create a message payload.
    let message = AccessoryMessage {
        AccessoryMessage.Payload(transport: .bluetooth, data: notificationData)
    }
    
    // Send the message payload to your accessory.
    try await session?.send(message: message)
    
    // Return true to indicate successful alerting.
    return true
}

// Chooses fields the accessory supports and implements a custom binary format.
func serializeNotification(_ notification: AccessoryNotification) -> Data {
    var data = Data()
    // Add title, subtitle, body, and so on.
    return data
}
```

You can send one message per notification, or you can partition the data for a single notification into multiple payloads. If Bluetooth is unavailable, the system delivers the message on any transport currently available.

The method returns a Boolean value indicating whether your accessory alerted for the notification. Return `true` if the accessory successfully alerts the person, or `false` otherwise. This information helps the system coordinate alerting across multiple devices.

#### Create an Extension to Send Notifications Securely

Create an [`AccessoryTransportSecurity`](accessorytransportsecurity.md) extension to manage the cryptographic key exchange process. Add a new extension target to your Xcode project. In the extension’s target properties, specify the extension point identifier `com.apple.accessory-transport-security`:

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

In your extension’s code, implement the [`AccessoryTransportSecurity`](accessorytransportsecurity.md) protocol, in which you [`accept(_:)`](accessorysecuritysession/request/accept(_:).md) incoming security session requests for your accessory:

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

The system requires your app extension to have the [`com.apple.developer.accessory-transport-security`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.accessory-transport-security) entitlement to use the [`AccessoryTransportSecurity`](accessorytransportsecurity.md) protocol.

#### Provide a Security Event Handler

The security extension assists with cryptography by handling key exchange messages between your accessory and the system. Provide an event handler that conforms to the [`AccessorySecuritySession`](accessorysecuritysession.md) class’s [`AccessorySecuritySession.EventHandler`](accessorysecuritysession/eventhandler.md) protocol. The system calls your handler’s [`messageReceived(_:completion:)`](accessorysecuritysession/eventhandler/messagereceived(_:completion:).md) method with security messages during the key exchange:

```swift
class SecurityEventHandler: AccessorySecuritySession.EventHandler {
    private var session: AccessorySecuritySession
    private var keyMaterial: SecurityMessage?
    private var publicKeyData: Data?
    private var privateKeyData: Data?
    
    init(session: AccessorySecuritySession) {
        self.session = session
    }
    
    func messageReceived(_ message: SecurityMessage, 
                        completion: @escaping @Sendable (AccessoryMessage.Result) -> Void) {
        switch message.keyType {
        case .encapsulatedKey:
            handleKeyExchange(message: message, completion: completion)
        default:
            completion(.success)
        }
    }
    
    // Cleans up key material.
    func sessionInvalidated(error: (any Error)?) {
        keyMaterial = nil
        privateKeyData = nil
        publicKeyData = nil
    }
}
```

#### Initiate Key Exchange From Your Accessory

Your accessory initiates the key exchange process when it’s ready to establish encrypted communication. Generate a public-private key pair on your accessory and send the public key to the system. Choose [`SecurityMessage.CipherSuite.xWing`](securitymessage/ciphersuite-swift.enum/xwing.md) for post-quantum security, or [`SecurityMessage.CipherSuite.p256`](securitymessage/ciphersuite-swift.enum/p256.md) as a fallback if your accessory doesn’t support XWing:

```swift
func handleKeyRequest(cipherSuite: SecurityMessage.CipherSuite) {
    do {
        let accessoryPublicKey: Data
        let accessoryPrivateKey: Data
        
        switch cipherSuite {
        case .xWing:
            // Generate an XWing key pair.
            let privateKey = try XWingMLKEM768X25519.PrivateKey()
            accessoryPrivateKey = privateKey.seedRepresentation
            accessoryPublicKey = privateKey.publicKey.rawRepresentation
            
        case .p256:
            // Generate a P256 key pair.
            let privateKey = P256.KeyAgreement.PrivateKey()
            accessoryPrivateKey = privateKey.rawRepresentation
            accessoryPublicKey = privateKey.publicKey.rawRepresentation
        }
        
        privateKeyData = accessoryPrivateKey
        publicKeyData = accessoryPublicKey
        
        // Send public key to the system.
        let message = SecurityMessage(
            keyType: .publicKey,
            cipherSuite: cipherSuite,
            version: .version1,
            key: accessoryPublicKey,
            supportedTransports: [.bluetooth]
        )
        
        try session.sendSecurityMessage(message)
    } catch {
        session.cancel(error: error)
    }
}
```

To use [`AccessoryTransport.internet`](accessorytransport/internet.md) or [`AccessoryTransport.localNetwork`](accessorytransport/localnetwork.md) transports, you must use XWing for enhanced security. Specify the supported transports in the `supportedTransports` parameter.

#### Complete the Key Exchange

The system generates cryptographic key material and sends it to your extension by invoking your handler’s [`messageReceived(_:completion:)`](accessorysecuritysession/eventhandler/messagereceived(_:completion:).md) method with a [`SecurityMessage`](securitymessage.md) that has a [`SecurityMessage.KeyType.encapsulatedKey`](securitymessage/keytype-swift.enum/encapsulatedkey.md) key type. Forward this key material to your accessory via Bluetooth and call the completion handler:

```swift
func handleKeyExchange(message: SecurityMessage, 
                      completion: @escaping @Sendable (AccessoryMessage.Result) -> Void) {
    guard let privateKeyData = privateKeyData,
          let publicKeyData = publicKeyData else {
        completion(.failure(.transportFailed))
        return
    }
    
    self.keyMaterial = message
    
    do {
        // Send key material to the accessory via Bluetooth.
        sendKeyMaterialToAccessory(message)
        
        // Inform the system of successful transmission.
        completion(.success)
    } catch {
        session.cancel(error: error)
        completion(.failure(.transportFailed))
    }
}
```

The completion handler is required. Call it with `.success` if the key material successfully transmits to your accessory, or `.failure(.transportFailed)` if transmission fails but may recover. If you don’t call the completion handler, the system assumes successful delivery.

#### Implement an Extension to Relay Encrypted Notifications

To send the encrypted data to your accessory, use an [`AccessoryTransportAppExtension`](accessorytransportappextension.md). Implement the [`messageReceived(_:completion:)`](accessorytransportsession/eventhandler/messagereceived(_:completion:).md) method in your event processing code, and the system calls your handler to transmit encrypted data for each message payload:

```swift
class TransportEventHandler: AccessoryTransportSession.EventHandler {
    func messageReceived(_ message: TransportMessage, 
                        completion: @escaping @Sendable (AccessoryMessage.Result) -> Void) {
        do {
            // Transmit encrypted notification data to the accessory over Bluetooth.
            try sendToAccessory(message.data, sessionID: message.sessionID)
            completion(.success)
        } catch {
            // Transport failed but may recover.
            completion(.failure(.transportFailed))
        }
    }
    
    // Cleans up when the session ends.
    func sessionInvalidated(error: (any Error)?) {
        // Clean up connection state.
    }
}
```

The system encrypts notification data using keys exchanged through your [`AccessoryTransportSecurity`](accessorytransportsecurity.md) extension before delivering it to your handler. Because the data is encrypted, your extension is unable to read or otherwise make sense of the data, and can only transmit it.

Call the completion handler with `.success` if the message transmits successfully, `.failure(.transportFailed)` if the transport fails but may recover, or `.failure(.transportUnavailable)` if the transport is unavailable. The system retries failed messages or attempts delivery on a different transport.

Add the [`com.apple.developer.accessory-transport-extension`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.accessory-transport-extension) entitlement to your extension’s code signature to use the [`AccessoryTransportAppExtension`](accessorytransportappextension.md) protocol.

#### Decrypt Notification Data on Your Accessory

When your accessory receives the encrypted notification data, it decrypts the data using [`HPKE (RFC9180)`](https://developer.apple.comhttps://datatracker.ietf.org/doc/rfc9180/) with keys exchanged through the transport security extension.

The accessory and extension share a secret, that is, a custom string phrase, for the HPKE decryption algorithm. Build the string using information about the protocol and key material:

```swift
let cipherSuite = securityMessage.cipherSuite.description  // The value is "xWing" or "p256".
let version = securityMessage.version.description          
let identifier = securityMessage.identifier ?? deviceUUID  // The CBPeripheral UUID.
let protocolInfo = Data("\(cipherSuite)-\(version)-\(identifier)".utf8)
```

> ❗ **Important**: The version component is the fully spelled-out word `Version1`, not the abbreviated `v1`.

Create an HPKE receiver from the accessory’s private key and protocol information. The following code uses the [`SecurityMessage.CipherSuite.xWing`](securitymessage/ciphersuite-swift.enum/xwing.md) cipher suite:

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
    encapsulatedKey: encapsulatedKeyFromSystem
)
```

Alternatively, the following code creates an HPKE receiver using the fallback [`SecurityMessage.CipherSuite.p256`](securitymessage/ciphersuite-swift.enum/p256.md) cipher suite:

```swift
let privateKey = try P256.KeyAgreement.PrivateKey(rawRepresentation: accessoryPrivateKeyData)

let recipient = try HPKE.Recipient(
    privateKey: privateKey,
    ciphersuite: .P256_SHA256_AES_GCM_256,
    info: protocolInfo,
    encapsulatedKey: encapsulatedKeyFromSystem
)
```

Derive a notification forwarding-specific secret by appending the direction and feature ID to the protocol information. The feature ID is the session ID of the transport message that you receive from [`messageReceived(_:completion:)`](accessorytransportsession/eventhandler/messagereceived(_:completion:).md).

```swift
let featureID = // The transport message's session ID.   
let context = Data("\(protocolInfo)-HostToAccessory-\(featureID)".utf8)
let secret = try recipient.exportSecret(context: context, outputByteCount: 32)
```

The direction is `HostToAccessory` for data that flows from the iPhone to the accessory, and `AccessoryToHost` for data that flows from the accessory to the iPhone.

The system encrypts notification data using AES-GCM as specified in NIST Special Publication 800-38D. The ciphertext on the wire encodes as:

```swift
IV (12 bytes) || ciphertext || MAC (16 bytes)
```

Decrypt the data using the feature-specific secret:

```swift
let sealedBox = try AES.GCM.SealedBox(combined: encryptedData)
let plaintext = try AES.GCM.open(sealedBox, using: secret)
```

If decryption fails, close the connection, reset the encryption state, and resynchronize the key exchange. If decryption succeeds, parse the notification information according to your accessory’s custom format.

#### Alert Someone About a Notification

To alert for a notification, present it on screen, play a sound, or trigger a haptic effect that uses touch to give users feedback on your accessory device.

Use the [`AlertingContext`](https://developer.apple.com/documentation/accessorynotifications/alertingcontext) to determine whether a notification requires an alert. The system provides the [`shouldAlert`](https://developer.apple.com/documentation/accessorynotifications/alertingcontext/shouldalert) property, which represents the person’s preferred notification behavior using notification settings and the iOS device’s current Focus state.

The [`notificationCanAlert`](https://developer.apple.com/documentation/accessorynotifications/alertingcontext/notificationcanalert) property indicates whether the notification has sound and alert permissions. The system might set [`notificationCanAlert`](https://developer.apple.com/documentation/accessorynotifications/alertingcontext/notificationcanalert) to `false` when the notification already alerts on another device or if device settings disable alerting for the notification.

The [`isSuppressedByFocus`](https://developer.apple.com/documentation/accessorynotifications/alertingcontext/issuppressedbyfocus) property indicates whether the device’s Focus state suppresses notification alerts.

For specialized notification types, check [`kind`](https://developer.apple.com/documentation/accessorynotifications/alertingcontext/kind-swift.property) to apply appropriate handling. For example, use the [`AlertingContext.Kind.incomingCall`](https://developer.apple.com/documentation/accessorynotifications/alertingcontext/kind-swift.enum/incomingcall) case for full-screen displays or priority alerts. Use [`sound`](https://developer.apple.com/documentation/accessorynotifications/alertingcontext/sound-swift.property) to determine sound characteristics, including whether the notification ignores silent mode with [`shouldIgnoreSilentMode`](https://developer.apple.com/documentation/accessorynotifications/alertingcontext/sound-swift.struct/shouldignoresilentmode).

#### Handle Notification Updates and Removals

The forwarding life cycle includes requests to update a notification after your accessory receives it, or to remove one or more existing notifications.

When a notification’s content changes, the system notifies your extension by calling [`updateNotification(_:)`](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler/updatenotification(_:)). Update the notification on your accessory without alerting again:

```swift
func updateNotification(_ notification: AccessoryNotification) {
    let notificationData = serializeNotification(notification)
    let message = AccessoryMessage {
        AccessoryMessage.Payload(transport: .bluetooth, data: notificationData)
    }
    Task {
        try await session?.send(message: message)
    }
}
```

If someone dismisses a notification on another device after your accessory receives the notification, the system follows up with a removal request by calling [`removeNotification(identifier:)`](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler/removenotification(identifier:)):

```swift
// Requests the removal of a notification from the accessory.
func removeNotification(identifier: AccessoryNotification.Identifier) {
    let removalData = serializeRemoval(identifier)
    let message = AccessoryMessage {
        AccessoryMessage.Payload(transport: .bluetooth, data: removalData)
    }
    Task {
        try await session?.send(message: message)
    }
}
```

The system calls [`removeAllNotifications()`](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler/removeallnotifications()) when your accessory needs to remove all notifications, such as when the person deletes the app that sent the notifications:

```swift
// Requests the removal of all notifications from the accessory.
func removeAllNotifications() {
    let clearData = serializeClearAll()
    let message = AccessoryMessage {
        AccessoryMessage.Payload(transport: .bluetooth, data: notificationData)
    }
    Task {
        try await session?.send(message: message)
    }
}
```

## See Also

- [protocol AccessoryDataProvider](accessorydataprovider.md)
  A protocol for an extension that receives iOS system notifications and curates their data for your accessory.
- [protocol AccessoryDataProviderConfiguration](accessorydataproviderconfiguration.md)
  A protocol that configures and manages communication between the extension and the system.
- [protocol AccessoryTransportSecurity](accessorytransportsecurity.md)
  A protocol for an extension that handles cryptographic key exchange with your accessory.
- [protocol AccessoryTransportSecurityConfiguration](accessorytransportsecurityconfiguration.md)
  A protocol that configures and manages communication between your security extension and the system.
- [Accessory Notifications](../accessorynotifications/accessorynotifications.md)
  Receive forwarded iOS system notifications on an accessory that you develop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/receiving-ios-notifications-on-an-accessory)*