# equatable()

**Framework**: SwiftUI  
**Kind**: method

Prevents the view from updating its child view when its new value is the same as its old value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func equatable() -> EquatableView<Self>
```

## See Also

- [func id<ID>(ID) -> some View](view/id(_:).md)
  Binds a view’s identity to the given proxy value.
- [func tag<V>(V, includeOptional: Bool) -> some View](view/tag(_:includeoptional:).md)
  Sets the unique tag value of this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/equatable())*