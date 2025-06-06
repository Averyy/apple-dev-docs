# unwrap(_:using:)

**Framework**: Apple CryptoKit  
**Kind**: method

Unwraps a key using the AES wrap algorithm.

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
static func unwrap<WrappedKey>(_ wrappedKey: WrappedKey, using kek: SymmetricKey) throws -> SymmetricKey where WrappedKey : DataProtocol
```

#### Return Value

The unwrapped key.

#### Discussion

Wrap is an implementation of the AES key wrap algorithm as specified in IETF RFC 3394. The method throws an error is the key was incorrectly wrapped.

## Parameters

- `wrappedKey`: The key to unwrap.
- `kek`: The key encryption key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/aes/keywrap/unwrap(_:using:))*