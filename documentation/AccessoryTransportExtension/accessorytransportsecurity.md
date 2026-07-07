# AccessoryTransportSecurity

**Framework**: Accessory Transport Extension  
**Kind**: protocol

A protocol for an extension that handles cryptographic key exchange with your accessory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
protocol AccessoryTransportSecurity : AppExtension
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Overview

Implement this protocol in an extension with an `EXExtensionPointIdentifier` value of `com.apple.accessory-transport-security` to manage the key exchange process that establishes encrypted communication with your accessory. The extension runs in a separate process for security isolation and communicates with the system through the extension’s configuration object ([`AccessoryTransportSecurityConfiguration`](accessorytransportsecurityconfiguration.md)).

> ❗ **Important**: The system requires your app extension to have the [`com.apple.developer.accessory-transport-security`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.accessory-transport-security) entitlement to use this protocol.

#### Add the Necessary Target Configuration

In your extension’s target properties, specify the extension point identifier:

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

#### Implement the Extension Point

In your extension’s Swift code, implement the protocol and provide an event handler that responds to key exchange messages:

```swift
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

class SecurityEventHandler: AccessorySecuritySession.EventHandler {
    private var session: AccessorySecuritySession
    
    init(session: AccessorySecuritySession) {
        self.session = session
    }
    
    func messageReceived(_ message: SecurityMessage, 
                        completion: @escaping @Sendable (AccessoryMessage.Result) -> Void) {
        // Handle encapsulated key from system.
        sendKeyMaterialToAccessory(message)
        completion(.success)
    }
    
    func sessionInvalidated(error: (any Error)?) {
        // Clean up key material.
    }
}
```

#### Initiate Key Exchange

Your accessory initiates the key exchange by generating a public-private key pair and sending the public key to the system. Choose [`SecurityMessage.CipherSuite.xWing`](securitymessage/ciphersuite-swift.enum/xwing.md) for post-quantum security or [`SecurityMessage.CipherSuite.p256`](securitymessage/ciphersuite-swift.enum/p256.md) as a fallback:

```swift
// Generate key pair.
let privateKey = try XWingMLKEM768X25519.PrivateKey()
let publicKey = privateKey.publicKey.rawRepresentation

// Send public key to system.
let message = SecurityMessage(
    keyType: .publicKey,
    cipherSuite: .xWing,
    version: .version1,
    key: publicKey,
    supportedTransports: [.bluetooth]
)

try session.sendSecurityMessage(message)
```

The system generates cryptographic key material and delivers it to your extension by calling [`messageReceived(_:completion:)`](accessorysecuritysession/eventhandler/messagereceived(_:completion:).md) with a [`SecurityMessage`](securitymessage.md) containing [`SecurityMessage.KeyType.encapsulatedKey`](securitymessage/keytype-swift.enum/encapsulatedkey.md). Forward this key material to your accessory via Bluetooth and call the completion handler with the transmission result.

For more information, see [`Receiving iOS notifications on an accessory`](receiving-ios-notifications-on-an-accessory.md).

## Topics

### Accepting session requests
- [func accept(sessionRequest: AccessorySecuritySession.Request) -> AccessorySecuritySession.Request.Decision](accessorytransportsecurity/accept(sessionrequest:).md)
  Evaluates incoming security session requests for an accessory.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)

## See Also

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)
  Create custom app extensions that manage iOS system notifications for your accessory.
- [protocol AccessoryDataProvider](accessorydataprovider.md)
  A protocol for an extension that receives iOS system notifications and curates their data for your accessory.
- [protocol AccessoryDataProviderConfiguration](accessorydataproviderconfiguration.md)
  A protocol that configures and manages communication between the extension and the system.
- [protocol AccessoryTransportSecurityConfiguration](accessorytransportsecurityconfiguration.md)
  A protocol that configures and manages communication between your security extension and the system.
- [Accessory Notifications](../AccessoryNotifications/AccessoryNotifications.md)
  Receive forwarded iOS system notifications on an accessory that you develop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsecurity)*