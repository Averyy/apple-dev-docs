# inset(by:)

**Framework**: SwiftUI  
**Kind**: method

Returns a threshold that is met when the target view is closer to the center of the container by `distance`. Use negative values to move the threshold away from the center.

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
func inset(by distance: Double) -> ScrollTransitionConfiguration.Threshold
```

## See Also

- [func interpolated(towards: ScrollTransitionConfiguration.Threshold, amount: Double) -> ScrollTransitionConfiguration.Threshold](scrolltransitionconfiguration/threshold/interpolated(towards:amount:).md)
  Creates a new threshold that combines this threshold value with another threshold, interpolated by the given amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolltransitionconfiguration/threshold/inset(by:))*