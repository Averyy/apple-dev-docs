# subscript(dynamicMember:)

**Framework**: Foundation  
**Kind**: subscript

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
subscript<S>(dynamicMember keyPath: KeyPath<AttributeScopes, S.Type>) -> ScopedAttributeContainer<S> where S : AttributeScope { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/runs/run/subscript(dynamicmember:)-66vfm)*