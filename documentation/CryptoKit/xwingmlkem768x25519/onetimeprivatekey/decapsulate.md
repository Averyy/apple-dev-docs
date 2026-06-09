# decapsulate(_:)

**Framework**: Apple CryptoKit  
**Kind**: method

Decapsulate a shared secret.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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