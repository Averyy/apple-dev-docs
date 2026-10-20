# AES.KeyWrap

**Framework**: Apple CryptoKit  
**Kind**: enum  
**Role**: Enumeration

An implementation of AES Key Wrapping in accordance with the IETF RFC 3394 specification.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum KeyWrap
```

## Topics

### Wrapping an AES key
- [static func wrap(SymmetricKey, using: SymmetricKey) throws -> Data](./keywrap/wrap%28_,using%29.md)
  Wraps a key using the AES wrap algorithm.
### Unwrapping an AES key
- [static func unwrap<WrappedKey>(WrappedKey, using: SymmetricKey) throws -> SymmetricKey](./keywrap/unwrap%28_,using%29.md)
  Unwraps a key using the AES wrap algorithm.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/aes/keywrap)*