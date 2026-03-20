# AccessorySecurity.Event

**Framework**: Accessory Transport Extension  
**Kind**: enum

An enumeration of security events during the key exchange process.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
enum Event
```

#### Overview

The [`AccessorySecuritySession.EventHandler`](accessorysecuritysession/eventhandler.md) protocol’s [`securityEventHandler(event:)`](accessorysecuritysession/eventhandler/securityeventhandler(event:).md) method receives events of this type.

## Topics

### Handling key exchange events
- [AccessorySecurity.Event.keyRequest](accessorysecurity/event/keyrequest.md)
  A key exchange event that initiates the key exchange process.
- [case keyReply(ciphersuite: AccessorySecurity.Crypto.Ciphersuite, publicKey: Data)](accessorysecurity/event/keyreply(ciphersuite:publickey:).md)
  A key exchange event that provides the accessory’s ciphersuite and public key to the host.
- [case keyExchange(keyMaterial: AccessorySecurity.Crypto.KeyMaterial)](accessorysecurity/event/keyexchange(keymaterial:).md)
  A key exchange event that provides cryptographic key material to the extension.
- [AccessorySecurity.Event.encapsulatedKey(_:)](accessorysecurity/event/encapsulatedkey(_:).md)
  A key exchange event that provides the accessory’s encapsulated key to the host.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecurity/event)*