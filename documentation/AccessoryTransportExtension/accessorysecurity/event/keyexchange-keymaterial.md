# AccessorySecurity.Event.keyExchange(keyMaterial:)

**Framework**: Accessory Transport Extension  
**Kind**: case

A key exchange event that provides cryptographic key material to the extension.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
case keyExchange(keyMaterial: AccessorySecurity.Crypto.KeyMaterial)
```

#### Discussion

The system sends this event as the third step of the key exchange process after receiving the accessory’s ciphersuite and public key.

## Parameters

- `keyMaterial`: A structure containing the host’s key material.

## See Also

- [AccessorySecurity.Event.keyRequest](accessorysecurity/event/keyrequest.md)
  A key exchange event that initiates the key exchange process.
- [case keyReply(ciphersuite: AccessorySecurity.Crypto.Ciphersuite, publicKey: Data)](accessorysecurity/event/keyreply(ciphersuite:publickey:).md)
  A key exchange event that provides the accessory’s ciphersuite and public key to the host.
- [AccessorySecurity.Event.encapsulatedKey(_:)](accessorysecurity/event/encapsulatedkey(_:).md)
  A key exchange event that provides the accessory’s encapsulated key to the host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecurity/event/keyexchange(keymaterial:))*