# permute(_:key:)

**Framework**: Apple CryptoKit  
**Kind**: method

Encrypts a single AES block in-place (ECB forward permutation).

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
static func permute<Payload>(_ payload: inout Payload, key: SymmetricKey) throws where Payload : MutableCollection, Payload.Element == UInt8
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/insecure/unauthenticatedaes/permute(_:key:)-632a8)*