# animation(_:value:)

**Framework**: Journaling Suggestions  
**Kind**: method

Applies the given animation to this view when the specified value changes.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
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

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/animation(_:value:))*