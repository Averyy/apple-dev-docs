# AccessorySecurity.Event.keyReply(ciphersuite:publicKey:)

**Framework**: Accessory Transport Extension  
**Kind**: case

A key exchange event that provides the accessory’s ciphersuite and public key to the host.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
case keyReply(ciphersuite: AccessorySecurity.Crypto.Ciphersuite, publicKey: Data)
```

#### Discussion

Send this event during the second step of the key exchange process in response to a [`AccessorySecurity.Event.keyRequest`](accessorysecurity/event/keyrequest.md) event.

## Parameters

- `ciphersuite`: The cryptographic ciphersuite the accessory supports.
- `publicKey`: A data object containing the accessory’s public key.

## See Also

- [AccessorySecurity.Event.keyRequest](accessorysecurity/event/keyrequest.md)
  A key exchange event that initiates the key exchange process.
- [case keyExchange(keyMaterial: AccessorySecurity.Crypto.KeyMaterial)](accessorysecurity/event/keyexchange(keymaterial:).md)
  A key exchange event that provides cryptographic key material to the extension.
- [AccessorySecurity.Event.encapsulatedKey(_:)](accessorysecurity/event/encapsulatedkey(_:).md)
  A key exchange event that provides the accessory’s encapsulated key to the host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecurity/event/keyreply(ciphersuite:publickey:))*