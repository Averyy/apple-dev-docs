# ScrollTransitionConfiguration.Threshold

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Describes a specific point in the progression of a target view within a container from hidden (fully outside the container) to visible.

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
struct Threshold
```

## Topics

### Getting the threshold
- [static var centered: ScrollTransitionConfiguration.Threshold](./threshold/centered.md)
  The target view is centered within the container
- [static let hidden: ScrollTransitionConfiguration.Threshold](./threshold/hidden.md)
- [static let visible: ScrollTransitionConfiguration.Threshold](./threshold/visible.md)
- [static func visible(Double) -> ScrollTransitionConfiguration.Threshold](./threshold/visible%28_%29.md)
  The target view is visible by the given amount, where zero is fully hidden, and one is fully visible.
### Modifying the threshold
- [func inset(by: Double) -> ScrollTransitionConfiguration.Threshold](./threshold/inset%28by%29.md)
  Returns a threshold that is met when the target view is closer to the center of the container by `distance`. Use negative values to move the threshold away from the center.
- [func interpolated(towards: ScrollTransitionConfiguration.Threshold, amount: Double) -> ScrollTransitionConfiguration.Threshold](./threshold/interpolated%28towards,amount%29.md)
  Creates a new threshold that combines this threshold value with another threshold, interpolated by the given amount.

## See Also

### Accessing the configuration
- [func animation(Animation) -> ScrollTransitionConfiguration](./animation%28_%29.md)
  Sets the animation with which the transition will be applied.
- [func threshold(ScrollTransitionConfiguration.Threshold) -> ScrollTransitionConfiguration](./threshold%28_%29.md)
  Sets the threshold at which the view will be considered fully visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolltransitionconfiguration/threshold)*