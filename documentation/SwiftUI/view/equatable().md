# equatable()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

Available when `Self` conforms to `Equatable`.

## See Also

### Managing the view hierarchy
- [func id<ID>(ID) -> some View](./id%28_%29.md)
  Binds a view’s identity to the given proxy value.
- [func tag<V>(V, includeOptional: Bool) -> some View](./tag%28_,includeoptional%29.md)
  Sets the unique tag value of this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/equatable())*