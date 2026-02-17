# AccessorySecurity.Event.encapsulatedKey(_:)

**Framework**: Accessory Transport Extension  
**Kind**: case

A key exchange event that provides the accessory’s encapsulated key to the host.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
case encapsulatedKey(Data)
```

#### Discussion

The system sends this event during the fourth step of the key exchange process after receiving the host’s public and encapsulated keys.

## Parameters

- `encapsulatedKey`: A data object containing the encapsulated key.

## See Also

- [AccessorySecurity.Event.keyRequest](accessorysecurity/event/keyrequest.md)
  A key exchange event that initiates the key exchange process.
- [case keyReply(ciphersuite: AccessorySecurity.Crypto.Ciphersuite, publicKey: Data)](accessorysecurity/event/keyreply(ciphersuite:publickey:).md)
  A key exchange event that provides the accessory’s ciphersuite and public key to the host.
- [case keyExchange(keyMaterial: AccessorySecurity.Crypto.KeyMaterial)](accessorysecurity/event/keyexchange(keymaterial:).md)
  A key exchange event that provides cryptographic key material to the extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecurity/event/encapsulatedkey(_:))*