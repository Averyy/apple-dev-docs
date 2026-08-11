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
static func inversePermute(_ payload: inout MutableRawSpan, key: SymmetricKey) throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/insecure/unauthenticatedaes/inversepermute(_:key:)-6rix9)*