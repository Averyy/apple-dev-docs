# inversePermute(_:key:)

**Framework**: Apple CryptoKit  
**Kind**: method

Decrypts a single AES block in-place (ECB inverse permutation).

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
static func inversePermute<Payload>(_ payload: inout Payload, key: SymmetricKey) throws where Payload : MutableCollection, Payload.Element == UInt8
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/insecure/unauthenticatedaes/inversepermute(_:key:)-77kb3)*