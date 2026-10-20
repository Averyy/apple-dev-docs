# animation(_:value:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Applies the given animation to this view when the specified value changes.

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
func animation<V>(_ animation: Animation?, value: V) -> some View where V : Equatable
```

## Mentions

- [Managing user interface state](../managing-user-interface-state.md)

#### Return Value

A view that applies `animation` to this view whenever `value` changes.

## Parameters

- `animation`: The animation to apply. If `animation` is `nil`, the view doesn’t animate.
- `value`: A value to monitor for changes.

## See Also

### Adding state-based animation to a view
- [func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) -> some View](./animation%28_,body%29.md)
  Applies the given animation to all animatable values within the `body` closure.
- [func animation(_:)](./animation%28_%29.md)
  Applies the given animation to this view when this view changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/animation(_:value:))*