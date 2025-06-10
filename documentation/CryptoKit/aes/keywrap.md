# AES.KeyWrap

**Framework**: Apple CryptoKit  
**Kind**: enum

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
- [static func wrap(SymmetricKey, using: SymmetricKey) throws -> Data](aes/keywrap/wrap(_:using:).md)
  Wraps a key using the AES wrap algorithm.
### Unwrapping an AES key
- [static func unwrap<WrappedKey>(WrappedKey, using: SymmetricKey) throws -> SymmetricKey](aes/keywrap/unwrap(_:using:).md)
  Unwraps a key using the AES wrap algorithm.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/aes/keywrap)*