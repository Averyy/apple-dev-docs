# animation(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Applies the given animation to this view when this view changes.

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
nonisolated
func animation(_ animation: Animation?) -> some View
```

Available when `Self` conforms to `Equatable`.

**Other overloads**:

```swift
nonisolated
func animation(_ animation: Animation?) -> some View
```

## Return Value

A view that applies `animation` to this view whenever it changes.

## Parameters

- `animation`: The animation to apply. If `animation` is `nil`, the view doesn’t animate.

## See Also

### Adding state-based animation to a view
- [func animation<V>(Animation?, value: V) -> some View](./animation%28_,value%29.md)
  Applies the given animation to this view when the specified value changes.
- [func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) -> some View](./animation%28_,body%29.md)
  Applies the given animation to all animatable values within the `body` closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/animation(_:))*