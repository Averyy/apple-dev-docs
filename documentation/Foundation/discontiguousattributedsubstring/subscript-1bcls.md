# subscript(_:)

**Framework**: Foundation  
**Kind**: subscript

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 1.0+
- watchOS 26.0+ (Beta)

## Declaration

```swift
subscript<K>(_: K.Type) -> K.Value? where K : AttributedStringKey, K.Value : Sendable { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/discontiguousattributedsubstring/subscript(_:)-1bcls)*