# SecurityMessage

**Framework**: Accessory Transport Extension  
**Kind**: struct

A structure that carries key material for negotiating a secure channel between the system and an accessory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
struct SecurityMessage
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Overview

Your [`AccessoryTransportSecurity`](accessorytransportsecurity.md) extension sends instances of this type to initiate key exchange and receives them during [`messageReceived(_:completion:)`](accessorysecuritysession/eventhandler/messagereceived(_:completion:).md) to complete the exchange.

## Topics

### Creating security messages
- [init(keyType: SecurityMessage.KeyType, cipherSuite: SecurityMessage.CipherSuite, version: SecurityMessage.CipherSuite.Version, key: Data, supportedTransports: [AccessoryTransport], identifier: String?)](securitymessage/init(keytype:ciphersuite:version:key:supportedtransports:identifier:).md)
  Initializes a security message with key material and metadata.
### Accessing key material
- [let key: Data](securitymessage/key.md)
  The key data carried by this message.
- [let keyType: SecurityMessage.KeyType](securitymessage/keytype-swift.property.md)
  The type of key carried by this message.
- [SecurityMessage.KeyType](securitymessage/keytype-swift.enum.md)
  Identifies the type of key carried by a [`SecurityMessage`](securitymessage.md).
### Determining encryption method
- [let cipherSuite: SecurityMessage.CipherSuite](securitymessage/ciphersuite-swift.property.md)
  The cipher suite used for key exchange.
- [let version: SecurityMessage.CipherSuite.Version](securitymessage/version.md)
  The cipher suite version.
- [SecurityMessage.CipherSuite](securitymessage/ciphersuite-swift.enum.md)
  A cryptographic cipher suite used during key exchange.
### Specifying transport preferences
- [let supportedTransports: [AccessoryTransport]](securitymessage/supportedtransports.md)
  An array of transports the accessory supports for sending sensitive information.
### Deriving HPKE keys
- [let identifier: String?](securitymessage/identifier.md)
  An optional Bluetooth identifier that the system uses to derive HPKE keys.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AccessoryFeature](accessoryfeature.md)
  A protocol that defines a capability for an accessory data provider extension.
- [struct AccessoryMessage](accessorymessage.md)
  A structure that represents a message to send to an accessory.
- [class AccessorySecuritySession](accessorysecuritysession.md)
  A class that manages a security session between the extension and the system.
- [struct TransportMessage](transportmessage.md)
  A structure that represents a message for transmission between the system and an accessory.
- [enum AccessoryTransport](accessorytransport.md)
  Supported transport types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/securitymessage)*