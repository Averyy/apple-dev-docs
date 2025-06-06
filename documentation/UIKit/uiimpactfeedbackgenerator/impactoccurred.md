# impactOccurred()

**Framework**: UIKit  
**Kind**: method

Triggers impact feedback.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func impactOccurred()
```

#### Discussion

This method tells the generator that an impact has occurred. In response, the generator may play the appropriate haptics based on the [`UIImpactFeedbackGenerator.FeedbackStyle`](uiimpactfeedbackgenerator/feedbackstyle.md) value passed to the generator’s [`init(style:)`](uiimpactfeedbackgenerator/init(style:).md) initializer.

For information on setting up a feedback generator, see the [`UIFeedbackGenerator`](uifeedbackgenerator.md) class.

## See Also

- [func prepare()](uifeedbackgenerator/prepare.md)
  Prepares the generator to trigger feedback.
- [func impactOccurred(intensity: CGFloat)](uiimpactfeedbackgenerator/impactoccurred(intensity:).md)
  Triggers impact feedback with a specific intensity.
- [func impactOccurred(at: CGPoint)](uiimpactfeedbackgenerator/impactoccurred(at:).md)
  Triggers impact feedback at the specified location.
- [func impactOccurred(intensity: CGFloat, at: CGPoint)](uiimpactfeedbackgenerator/impactoccurred(intensity:at:).md)
  Triggers impact feedback with a specific intensity at the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimpactfeedbackgenerator/impactoccurred())*