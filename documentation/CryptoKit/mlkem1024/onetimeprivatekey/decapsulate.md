# decapsulate(_:)

**Framework**: Apple CryptoKit  
**Kind**: method

Decapsulate a shared secret.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
consuming func decapsulate<D>(_ encapsulated: D) throws -> SymmetricKey where D : DataProtocol
```

#### Return Value

The shared secret.

## Parameters

- `encapsulated`: An encapsulated shared secret, that you get by calling [`encapsulate()`](mlkem1024/publickey/encapsulate().md) on the corresponding public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem1024/onetimeprivatekey/decapsulate(_:))*