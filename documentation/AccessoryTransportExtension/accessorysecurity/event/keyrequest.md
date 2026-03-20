# AccessorySecurity.Event.keyRequest

**Framework**: Accessory Transport Extension  
**Kind**: case

A key exchange event that initiates the key exchange process.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
case keyRequest
```

#### Discussion

The system sends this event as the first step of the key exchange process to begin establishing secure communication with the accessory.

## See Also

- [case keyReply(ciphersuite: AccessorySecurity.Crypto.Ciphersuite, publicKey: Data)](accessorysecurity/event/keyreply(ciphersuite:publickey:).md)
  A key exchange event that provides the accessory’s ciphersuite and public key to the host.
- [case keyExchange(keyMaterial: AccessorySecurity.Crypto.KeyMaterial)](accessorysecurity/event/keyexchange(keymaterial:).md)
  A key exchange event that provides cryptographic key material to the extension.
- [AccessorySecurity.Event.encapsulatedKey(_:)](accessorysecurity/event/encapsulatedkey(_:).md)
  A key exchange event that provides the accessory’s encapsulated key to the host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecurity/event/keyrequest)*