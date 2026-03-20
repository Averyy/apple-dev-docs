# identifier

**Framework**: Accessory Transport Extension  
**Kind**: property

An identifier that the system uses to derive HPKE keys.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
let identifier: String
```

#### Discussion

For more information about HPKE keys, see the [`HPKE (RFC9180)`](https://developer.apple.comhttps://datatracker.ietf.org/doc/rfc9180/) specification.

## See Also

- [let publicKey: Data](accessorysecurity/crypto/keymaterial/publickey.md)
  A data object that contains your public key.
- [var encapsulatedKey: Data](accessorysecurity/crypto/keymaterial/encapsulatedkey.md)
  A data object that contains an encapsulated key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecurity/crypto/keymaterial/identifier)*