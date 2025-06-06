# SecKeySizes

**Framework**: Security  
**Kind**: enum

The supported sizes for keys of various common types.

**Availability**:
- macOS 10.9+

## Declaration

```swift
enum SecKeySizes
```

## Topics

### Constants
- [SecKeySizes.secDefaultKeySize](seckeysizes/secdefaultkeysize.md)
  The default key size for the specified type.
- [SecKeySizes.sec3DES192](seckeysizes/sec3des192.md)
  192-bit DES.
- [SecKeySizes.secAES128](seckeysizes/secaes128.md)
  128-bit AES.
- [static var secAES192: SecKeySizes](seckeysizes/secaes192.md)
  192-bit AES.
- [SecKeySizes.secAES256](seckeysizes/secaes256.md)
  256-bit AES.
- [static var secp192r1: SecKeySizes](seckeysizes/secp192r1.md)
  192-bit ECC Keys for Suite-B from RFC 4492 section 5.1.1.
- [static var secp256r1: SecKeySizes](seckeysizes/secp256r1.md)
  256-bit ECC Keys for Suite-B from RFC 4492 section 5.1.1.
- [SecKeySizes.secp384r1](seckeysizes/secp384r1.md)
  384-bit ECC Keys for Suite-B from RFC 4492 section 5.1.1.
- [SecKeySizes.secp521r1](seckeysizes/secp521r1.md)
  521-bit ECC Keys for Suite-B from RFC 4492 section 5.1.1.
- [SecKeySizes.secRSAMin](seckeysizes/secrsamin.md)
  1024 bits is the minimum size for an RSA key.
- [SecKeySizes.secRSAMax](seckeysizes/secrsamax.md)
  4096 bits is the maximum size for an RSA key.
### Initializers
- [init?(rawValue: UInt32)](seckeysizes/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeysizes)*