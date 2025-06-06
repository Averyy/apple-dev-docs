# id(_:)

**Framework**: SwiftUI  
**Kind**: method

Binds a view’s identity to the given proxy value.

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
func id<ID>(_ id: ID) -> some View where ID : Hashable
```

#### Discussion

When the proxy value specified by the `id` parameter changes, the identity of the view — for example, its state — is reset.

## See Also

- [func tag<V>(V, includeOptional: Bool) -> some View](view/tag(_:includeoptional:).md)
  Sets the unique tag value of this view.
- [func equatable() -> EquatableView<Self>](view/equatable.md)
  Prevents the view from updating its child view when its new value is the same as its old value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/id(_:))*