# SecCSDigestAlgorithm

**Framework**: Security  
**Kind**: enum

The list of digest algorithms available for code signatures.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum SecCSDigestAlgorithm
```

#### Overview

Use these values with the [`kSecCodeInfoDigestAlgorithm`](kseccodeinfodigestalgorithm.md) and [`kSecCodeInfoDigestAlgorithms`](kseccodeinfodigestalgorithms.md) keys described in [`Signing Information Dictionary Keys`](signing-information-dictionary-keys.md).

## Topics

### Enumeration Cases
- [SecCSDigestAlgorithm.codeSignatureHashSHA1](seccsdigestalgorithm/codesignaturehashsha1.md)
- [SecCSDigestAlgorithm.codeSignatureHashSHA256](seccsdigestalgorithm/codesignaturehashsha256.md)
- [SecCSDigestAlgorithm.codeSignatureHashSHA256Truncated](seccsdigestalgorithm/codesignaturehashsha256truncated.md)
- [SecCSDigestAlgorithm.codeSignatureHashSHA384](seccsdigestalgorithm/codesignaturehashsha384.md)
- [SecCSDigestAlgorithm.codeSignatureHashSHA512](seccsdigestalgorithm/codesignaturehashsha512.md)
- [SecCSDigestAlgorithm.codeSignatureNoHash](seccsdigestalgorithm/codesignaturenohash.md)
### Initializers
- [init?(rawValue: UInt32)](seccsdigestalgorithm/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccsdigestalgorithm)*