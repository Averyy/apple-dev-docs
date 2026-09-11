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
consuming func decapsulate(_ encapsulated: Data) throws -> SymmetricKey
```

#### Return Value

The shared secret.

## Parameters

- `encapsulated`: An encapsulated shared secret, that you get by calling `XWingMLKEM768X25519/PublicKey/encapsulate()` on the corresponding public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/xwingmlkem768x25519/onetimeprivatekey/decapsulate(_:))*