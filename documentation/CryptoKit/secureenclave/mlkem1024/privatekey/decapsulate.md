# decapsulate(_:)

**Framework**: Apple CryptoKit  
**Kind**: method

Decapsulates the encapsulated shared secret

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func decapsulate<D>(_ encapsulated: D) throws -> SymmetricKey where D : DataProtocol
```

#### Return Value

The decapsulated shared secret

## Parameters

- `encapsulated`: The encapsulated shared secret


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/mlkem1024/privatekey/decapsulate(_:))*