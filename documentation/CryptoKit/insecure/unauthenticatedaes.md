# Insecure.UnauthenticatedAES

**Framework**: Apple CryptoKit  
**Kind**: enum

AES-ECB (Electronic Codebook) single-block permutation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 1.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum UnauthenticatedAES
```

#### Overview

> ❗ **Important**: ECB mode is unauthenticated and reveals block-level patterns. Only use this when a higher-level protocol provides its own integrity and confidentiality guarantees, or in higher-level protocols that have received security analysis (such as QUIC header protection, RFC9001).

## Topics

### Type Methods
- [static func inversePermute(inout MutableRawSpan, key: SymmetricKey) throws](insecure/unauthenticatedaes/inversepermute(_:key:)-6rix9.md)
  Decrypts a single AES block in-place (ECB inverse permutation).
- [static func inversePermute<Payload>(inout Payload, key: SymmetricKey) throws](insecure/unauthenticatedaes/inversepermute(_:key:)-77kb3.md)
  Decrypts a single AES block in-place (ECB inverse permutation).
- [static func permute<Payload>(inout Payload, key: SymmetricKey) throws](insecure/unauthenticatedaes/permute(_:key:)-632a8.md)
  Encrypts a single AES block in-place (ECB forward permutation).
- [static func permute(inout MutableRawSpan, key: SymmetricKey) throws](insecure/unauthenticatedaes/permute(_:key:)-6qom3.md)
  Encrypts a single AES block in-place (ECB forward permutation).

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/insecure/unauthenticatedaes)*