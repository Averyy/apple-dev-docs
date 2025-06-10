# subscript(dynamicMember:)

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
subscript<S>(dynamicMember keyPath: KeyPath<AttributeScopes, S.Type>) -> ScopedAttributeContainer<S> where S : AttributeScope { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/discontiguousattributedsubstring/subscript(dynamicmember:)-89pug)*