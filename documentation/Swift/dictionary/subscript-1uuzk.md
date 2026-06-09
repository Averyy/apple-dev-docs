# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Subscript that shadows the standard Dictionary subscript to provide path-based access. When the key contains `":"`, it is treated as a path with `":"` as the delimiter; otherwise the regular dictionary key semantics apply.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
subscript(key: String) -> USDValue? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/subscript(_:)-1uuzk)*