# threshold(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the threshold at which the view will be considered fully visible.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func threshold(_ threshold: ScrollTransitionConfiguration.Threshold) -> ScrollTransitionConfiguration
```

#### Return Value

A copy of this configuration with the threshold set to the given value.

## Parameters

- `threshold`: The threshold specifying how much of the view must intersect with the container before it is treated as visible.

## See Also

### Accessing the configuration
- [func animation(Animation) -> ScrollTransitionConfiguration](./animation%28_%29.md)
  Sets the animation with which the transition will be applied.
- [ScrollTransitionConfiguration.Threshold](./threshold.md)
  Describes a specific point in the progression of a target view within a container from hidden (fully outside the container) to visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolltransitionconfiguration/threshold(_:))*