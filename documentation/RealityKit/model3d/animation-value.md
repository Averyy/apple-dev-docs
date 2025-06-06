# animation(_:value:)

**Framework**: RealityKit  
**Kind**: method

Applies the given animation to this view when the specified value changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func animation<V>(_ animation: Animation?, value: V) -> some View where V : Equatable
```

#### Return Value

A view that applies `animation` to this view whenever `value` changes.

## Parameters

- `animation`: The animation to apply. If   is  , the view   doesn’t animate.
- `value`: A value to monitor for changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/animation(_:value:))*