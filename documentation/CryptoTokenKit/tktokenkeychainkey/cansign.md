# canSign

**Framework**: CryptoTokenKit  
**Kind**: property

Whether the key can be used to sign data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var canSign: Bool { get set }
```

#### Discussion

This property is equivalent to the `kSecAttrCanSign` type attribute.

## See Also

- [var keyType: String](tktokenkeychainkey/keytype.md)
  The type of the key. Currently, only [`kSecAttrKeyTypeRSA`](https://developer.apple.com/documentation/Security/kSecAttrKeyTypeRSA) and `kSecAttrKeyTypeECSECPrimeRandom` are supported values.
- [var keySizeInBits: Int](tktokenkeychainkey/keysizeinbits.md)
- [var applicationTag: Data?](tktokenkeychainkey/applicationtag.md)
  The private tag data.
- [var publicKeyData: Data?](tktokenkeychainkey/publickeydata.md)
  The public key data.
- [var publicKeyHash: Data?](tktokenkeychainkey/publickeyhash.md)
  The SHA1 hash of the raw public key.
- [var canDecrypt: Bool](tktokenkeychainkey/candecrypt.md)
  Whether the key can be used to decrypt data.
- [var canPerformKeyExchange: Bool](tktokenkeychainkey/canperformkeyexchange.md)
  Whether the key can be used to perform Diffie-Hellman style cryptographic key exchange.
- [var isSuitableForLogin: Bool](tktokenkeychainkey/issuitableforlogin.md)
  Whether the key can be used for system login.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/cansign)*