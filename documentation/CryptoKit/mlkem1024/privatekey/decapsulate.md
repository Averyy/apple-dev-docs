# decapsulate(_:)

**Framework**: Apple CryptoKit  
**Kind**: method

Decapsulate a shared secret.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func decapsulate<D>(_ encapsulated: D) throws -> SymmetricKey where D : DataProtocol
```

#### Return Value

The shared secret.

## Parameters

- `encapsulated`: An encapsulated shared secret, that you get by calling [`encapsulate()`](mlkem1024/publickey/encapsulate().md) on the corresponding public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem1024/privatekey/decapsulate(_:))*