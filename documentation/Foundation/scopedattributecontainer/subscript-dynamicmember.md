# subscript(dynamicMember:)

**Framework**: Foundation  
**Kind**: subscript

Returns the value of the attribute that the specified key path indicates.

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
@preconcurrency
subscript<T>(dynamicMember keyPath: KeyPath<S, T>) -> T.Value? where T : AttributedStringKey, T.Value : Sendable { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scopedattributecontainer/subscript(dynamicmember:))*