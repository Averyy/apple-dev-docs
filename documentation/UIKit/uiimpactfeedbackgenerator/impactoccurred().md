# impactOccurred()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Triggers impact feedback.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func impactOccurred()
```

```objc
- (void) impactOccurred;
```

## Discussion

This method tells the generator that an impact has occurred. In response, the generator may play the appropriate haptics based on the [`UIImpactFeedbackGenerator.FeedbackStyle`](./feedbackstyle.md) value passed to the generator’s [`init(style:)`](./init%28style%29.md) initializer.

For information on setting up a feedback generator, see the [`UIFeedbackGenerator`](../uifeedbackgenerator.md) class.

## See Also

### Related Documentation
- [func prepare()](../uifeedbackgenerator/prepare%28%29.md)
  Prepares the generator to trigger feedback.
### Reporting impacts
- [func impactOccurred(intensity: CGFloat)](./impactoccurred%28intensity%29.md)
  Triggers impact feedback with a specific intensity.
- [func impactOccurred(at: CGPoint)](./impactoccurred%28at%29.md)
  Triggers impact feedback at the specified location.
- [func impactOccurred(intensity: CGFloat, at: CGPoint)](./impactoccurred%28intensity,at%29.md)
  Triggers impact feedback with a specific intensity at the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimpactfeedbackgenerator/impactoccurred())*