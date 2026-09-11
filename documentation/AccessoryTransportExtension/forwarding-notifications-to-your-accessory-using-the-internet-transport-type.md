# Forwarding notifications to your accessory using the internet transport type

**Framework**: Accessory Transport Extension

Send notification data to your accessory over the internet when Bluetooth connectivity is unavailable.

#### Overview

The Accessory Transport Extension framework supports delivering iOS system notifications over the internet to an accessory you develop. When notification delivery occurs over the internet, your accessory receives notifications even when it’s out of Bluetooth range of the paired iPhone. The system selects a transport type automatically when a notification is ready for forwarding: Bluetooth if the accessory is connected, local network if available and supported by the accessory, or internet if available and supported by the accessory.

Forwarding notifications over the internet follows much of the same process as Bluetooth forwarding, as described in [`Receiving iOS notifications on an accessory`](receiving-ios-notifications-on-an-accessory.md). The steps include:

- Prompt the person to allow forwarding by calling into the [`Accessory Notifications`](https://developer.apple.com/documentation/accessorynotifications) framework.
- Provide extensions for data curation, crytographic key exchange, and data transmission.
- Implement a [`NotificationsForwarding.AccessoryNotificationsHandler`](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler) for notification life cycle events.

Transporting notifications over the internet is different from the Bluetooth process in the following ways:

- Cryptographic operations require the [`SecurityMessage.CipherSuite.xWing`](securitymessage/ciphersuite-swift.enum/xwing.md) cipher suite.
- The security message’s [`supportedTransports`](securitymessage/supportedtransports.md) contains [`AccessoryTransport.internet`](accessorytransport/internet.md).
- The framework provides a [`pushToken`](accessorytransportsession/pushtoken.md) for notification-response routing back to the correct device.
- Rather than AES-GCM encryption, the system uses a *Symmetric Key Ratchet*, which derives a new encryption key for every message.
- Decryption-key identification requires the wire transmission format to include ratchet metadata in addition to ciphertext.

#### Request Permission to Forward Notifications

Before the system provides notification data to your app, the person needs to allow notification forwarding. Call  [`requestForwarding(for:)`](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationcenter/requestforwarding(for:)) from your companion app to ask the person for permission. Pass the [`ASAccessory`](https://developer.apple.com/documentation/accessorysetupkit/asaccessory) object that AccessorySetupKit provides when your companion app registers the accessory:

```swift
import AccessoryNotifications
import AccessorySetupKit

let accessory: ASAccessory = /* The accessory object from AccessorySetupKit. */
let center = AccessoryNotificationCenter()
let result = try await center.requestForwarding(for: accessory)
```

The system prompts the person to select the applications on their device to which they agree to receive notifications. The [`ForwardingDecision`](https://developer.apple.com/documentation/accessorynotifications/forwardingdecision) value that the [`requestForwarding(for:)`](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationcenter/requestforwarding(for:)) method returns represents the person’s decision. If the person approves, the app selections they made determine the substance of a given notification that the system provides your app for forwarding.

#### Create the Notification Forwarding Extensions

Notification forwarding relies on coordination between three app extensions that your app provides:

- **[`AccessoryDataProvider`](accessorydataprovider.md)**: Receives notification content and prepares it for transmission.
- **[`AccessoryTransportSecurity`](accessorytransportsecurity.md)**: Manages cryptographic key exchange with your accessory.
- **[`AccessoryTransportAppExtension`](accessorytransportappextension.md)**: Relays encrypted data to your accessory.

The system coordinates these extensions, encrypting notification data before transmission so that only your accessory can decrypt it. Internet and Bluetooth transport require the same extension implementations regardless of the transport the system chooses at runtime. To create these extensions, see [`Receiving iOS notifications on an accessory`](receiving-ios-notifications-on-an-accessory.md).

#### Configure a Shared App Group

Your companion app is the iOS app that pairs with your accessory using AccessorySetupKit and runs on the person’s iPhone. The companion app might need to share certain data across its extensions to support internet transport. For example, when multiple of your app’s targets in Xcode, including the extensions, need authentication tokens for your webserver, a maximum payload size, or the same list of supported content types, use *App groups* to share the common data.

Add an App Groups capability to your app target and all extension targets in Xcode, using the same app group identifier across all targets. Store shared data from your app using `UserDefaults(suiteName:)` or `FileManager.containerURL(forSecurityApplicationGroupIdentifier:)`:

```swift
// In the companion app, write configuration to the shared container.
let sharedDefaults = UserDefaults(suiteName: "group.com.yourcompany.accessoryapp")
sharedDefaults?.set(authToken, forKey: "ServerAuthToken")
sharedDefaults?.set(maxPayloadSize, forKey: "MaxPayloadSize")
sharedDefaults?.set(contentPreferences, forKey: "ContentPreferences")

// In the extension, read from the shared container.
let sharedDefaults = UserDefaults(suiteName: "group.com.yourcompany.accessoryapp")
let authToken = sharedDefaults?.string(forKey: "ServerAuthToken")
let maxPayloadSize = sharedDefaults?.integer(forKey: "MaxPayloadSize")
```

#### Specify Internet Transport During Key Exchange

*Key exchange* is the process during which your accessory and the system agree on a shared secret without transmitting the secret itself. This exchange allows each side to encrypt and decrypt data, and avoid extraneous listeners on the connection. To support internet transport alongside other transport types, the system establishes an encryption mechanism that works across every transport that your accessory specifies.

The system records the transports that your app supports once during a cryptographic key exchange. Initiate the key exchange from your app’s [`AccessoryTransportSecurity`](accessorytransportsecurity.md) extension and specify `internet` as a supported transport type:

```swift
let message = SecurityMessage(
    keyType: .publicKey,
    /* Required for internet transport. */
    cipherSuite: .xWing,
    version: .version1,
    key: accessoryPublicKey,
    /* The transports your app supports. */
    supportedTransports: [.bluetooth, .internet]
)

try session.sendSecurityMessage(message)
```

#### Prepare Payloads for Supported Transports

When your app supports multiple transport types, the session’s [`transport`](accessorytransportsession/transport.md) identifies the transport that the system selects. Your data provider can prepare different payloads per transport type:

```swift
func addNotification(_ notification: AccessoryNotification,
                     alertingContext: AlertingContext) async throws -> Bool {
    guard alertingContext.shouldAlert else { return false }
    // Prepare a payload for each supported transport.
    let message = AccessoryMessage {
        AccessoryMessage.Payload(
            transport: .bluetooth,
            data: serializeNotification(notification, for: .bluetooth))
        AccessoryMessage.Payload(
            transport: .internet,
            data: serializeNotification(notification, for: .internet))
    }
    try await session?.send(message: message)
    return true
}
```

Create a payload tailored for each transport type so the system can deliver the message efficiently. For example, you can include image attachments in a Bluetooth payload and omit them from internet payloads to reduce data consumption or latency.

#### Handle Internet Delivery in Your Transport Extension

Your [`AccessoryTransportAppExtension`](accessorytransportappextension.md) may run in a separate process for each active transport. Check [`transport`](accessorytransportsession/transport.md) to determine which transport the current session uses, and forward the message to your accessory accordingly.

For internet sessions, also forward [`pushToken`](accessorytransportsession/pushtoken.md) to your accessory alongside the notification data. The system registers your companion app for remote notifications and manages that registration internally; you don’t need to add the Push Notifications capability or call `registerForRemoteNotifications()` yourself; the system automatically provides `pushToken` to your transport extension. The push token identifies the iOS device to APNs, and the system populates it when [`transport`](accessorytransportsession/transport.md) is [`AccessoryTransport.internet`](accessorytransport/internet.md), including the value for every internet session. Your accessory stores this token and combines it with the [`sessionID`](transportmessage/sessionid.md) to route any responses back to the correct device and data provider extension:

```swift
class TransportEventHandler: AccessoryTransportSession.EventHandler {
    func messageReceived(_ message: TransportMessage,
                         completion: @escaping @Sendable
                         (AccessoryMessage.Result) -> Void) {
        switch session.transport {
        case .bluetooth:
            sendViaBluetooth(message.data, sessionID: message.sessionID)
            completion(.success)

        case .internet:
            // Convert the push token to a hex string for JSON transmission.
            let hexToken = session.pushToken?.map {
                String(format: "%02x", $0) }.joined()

            sendViaInternet(message.data,
                            sessionID: message.sessionID,
                            pushToken: hexToken)
            completion(.success)

        case .localNetwork:
            sendViaLocalNetwork(message.data, sessionID: message.sessionID)
            completion(.success)

        case nil:
            completion(.failure(.transportUnavailable))
        }
    }
}
```

Convert the push token `Data` value to a hex-encoded string before including it in any JSON payload your accessory transmits to your server. The session ID identifies which data provider extension the response targets; the push token identifies which device to deliver it to. Your accessory’s server pushes response data back to the device directly through APNs, using its own APNs provider credentials and the forwarded push token to identify the target device.

#### Export Key Exchange Secrets on Your Accessory

Internet transport uses a Symmetric Key Ratchet for per-message encryption. Your accessory initializes the Symmetric Key Ratchet from the HPKE secrets established during Bluetooth key exchange. For more information about HPKE secrets and Bluetooth, see [`Receiving iOS notifications on an accessory`](receiving-ios-notifications-on-an-accessory.md).

Export a single pair of secrets and reuse it for every feature your accessory supports over the internet. This process contrasts with a Bluetooth transport, which derives a separate key pair per feature. When your accessory completes key exchange, export secrets for both directions from the HPKE recipient and initialize two independent ratchet instances, one per direction:

```swift
// On the accessory, after receiving the encapsulated key from the system.
let recipient = try HPKE.Recipient(
    privateKey: accessoryPrivateKey,
    ciphersuite: .XWingMLKEM768X25519_SHA256_AES_GCM_256,
    info: protocolInfo,
    encapsulatedKey: encapsulatedKeyFromSystem
)

// Internet transport keys off the same Bluetooth peripheral identifier
//  as `protocolInfo`, not the cipher suite, version, or a per-feature ID.
guard let bluetoothUUID: String = securityMessage.identifier else {
    /* Handle a missing identifier. */
}
let hostToAccessoryContext = Data(
    "AccessoryInternetKey-HostToAccessory-\(bluetoothUUID)".utf8)
let accessoryToHostContext = Data(
    "AccessoryInternetKey-AccessoryToHost-\(bluetoothUUID)".utf8)

// Export the secrets from both directions and store them for the session lifetime.
let hostToAccessorySecret = try recipient.exportSecret(
    context: hostToAccessoryContext,
    outputByteCount: 32
)
let accessoryToHostSecret = try recipient.exportSecret(
    context: accessoryToHostContext,
    outputByteCount: 32
)
// Derive a four-byte key ID from the accessory's public key.
let keyID = Data(SHA384.hash(data: accessoryPublicKey.rawRepresentation)).prefix(4)

// Initialize two ratchet instances, one per direction. `hostToAccessorySecret` is
//  the root key for messages arriving from the iPhone. `accessoryToHostSecret` is
//  the root key for messages the accessory sends to the iPhone.
initializeRatchets(
    incomingRootKey: hostToAccessorySecret,
    outgoingRootKey: accessoryToHostSecret,
    keyID: keyID
)
```

> ❗ **Important**: Export secrets once, when your accessory handles the [`SecurityMessage.KeyType.encapsulatedKey`](securitymessage/keytype-swift.enum/encapsulatedkey.md) message during key exchange. Store both exported secrets and persist the ratchet state for the session lifetime. Don’t re-export secrets for individual messages.

#### Decrypt Internet Delivered Notifications on Your Accessory

Each internet-delivered message carries three fields: a 4-byte `keyID` that identifies the ratchet instance to use, a 4-byte little-endian `messageIndex` that specifies the ratchet step, and a variable-length ciphertext in the format `nonce (12 bytes) || ciphertext || tag (16 bytes)`.

A ratchet step is the single derivation that produces one message’s encryption key and advances the ratchet to the next chain key, and a fresh key protects each message without repeating a previous one. Performing a ratchet step derives a fresh message key and advances the chain key using a single HKDF `expand` call with SHA-256:

```swift
let ratchetKeyDerivationLabel = Data(
    "AccessoryTransportSecurity-RatchetKeys-".utf8)

// Derives the message key and next chain key for a single ratchet step.
func ratchetStep(chainKey: SymmetricKey, messageIndex: UInt32) ->
    (messageKey: SymmetricKey, nextChainKey: SymmetricKey) {

    let info = ratchetKeyDerivationLabel + withUnsafeBytes(of:
        messageIndex.littleEndian) { Data($0) }

    let output = HKDF<SHA256>.expand(pseudoRandomKey:
        chainKey, info: info, outputByteCount: 64)

    return output.withUnsafeBytes { bytes in
        (messageKey: SymmetricKey(data: bytes.prefix(32)),
         nextChainKey: SymmetricKey(data: bytes.suffix(32)))
    }
}
```

The `chainKey` argument is the current 256-bit chain key, and `messageIndex` is the message index the ratchet encodes as a 4-byte little-endian value in the derivation info. After deriving the message key at the index the incoming message specifies, use AES-256-GCM to decrypt:

```swift
// On the accessory: decrypt an internet-delivered notification message.
func decryptMessage(keyID: Data, messageIndex: UInt32,
                    ciphertext: Data) throws -> Data {

    // Verify the key ID matches this session's ratchet.
    guard keyID == self.keyID else {
        throw RatchetError.invalidKeyID
    }
    // Derive the message key at the specified ratchet index.
    let messageKey = try incomingRatchet.messageKey(forIndex: UInt64(messageIndex))
    // Decrypt the ciphertext (nonce || ciphertext || tag format).
    let sealedBox = try AES.GCM.SealedBox(combined: ciphertext)
    let plaintext = try AES.GCM.open(sealedBox, using: messageKey)
    // Persist the ratchet state after every successful decryption.
    saveRatchetState()
    return plaintext
}
```

The ratchet supports out-of-order delivery by caching up to 50,000 skipped message keys. Because it removes each cached key upon first use, decrypting one message never exposes the key for any other message, preserving forward secrecy. Persist the ratchet state after every successful decryption so that out-of-order tracking survives across sessions.

## See Also

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)
  Create custom app extensions that manage iOS system notifications for your accessory.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/forwarding-notifications-to-your-accessory-using-the-internet-transport-type)*