# keyType

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The type of the key. Currently, only [`kSecAttrKeyTypeRSA`](../../Security/ksecattrkeytypersa.md) and `kSecAttrKeyTypeECSECPrimeRandom` are supported values.

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
var keyType: String { get set }
```

```objc
@property (copy) NSString * keyType;
```

## Discussion

This property is equivalent to the `kSecAttrKeyType` type attribute.

## See Also

### Accessing Key Attributes
- [var keySizeInBits: Int](./keysizeinbits.md)
- [var applicationTag: Data?](./applicationtag.md)
  The private tag data.
- [var publicKeyData: Data?](./publickeydata.md)
  The public key data.
- [var publicKeyHash: Data?](./publickeyhash.md)
  The SHA1 hash of the raw public key.
- [var canDecrypt: Bool](./candecrypt.md)
  Whether the key can be used to decrypt data.
- [var canSign: Bool](./cansign.md)
  Whether the key can be used to sign data.
- [var canPerformKeyExchange: Bool](./canperformkeyexchange.md)
  Whether the key can be used to perform Diffie-Hellman style cryptographic key exchange.
- [var isSuitableForLogin: Bool](./issuitableforlogin.md)
  Whether the key can be used for system login.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/keytype)*