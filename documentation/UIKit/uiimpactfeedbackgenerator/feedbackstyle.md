# UIImpactFeedbackGenerator.FeedbackStyle

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The mass of the objects in the collision simulated by an impact feedback generator object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum FeedbackStyle
```

```c
enum UIImpactFeedbackStyle : NSInteger;
```

## Topics

### Constants
- [UIImpactFeedbackGenerator.FeedbackStyle.heavy](./feedbackstyle/heavy.md)
  A collision between large, heavy user interface elements.
- [UIImpactFeedbackGenerator.FeedbackStyle.light](./feedbackstyle/light.md)
  A collision between small, light user interface elements.
- [UIImpactFeedbackGenerator.FeedbackStyle.medium](./feedbackstyle/medium.md)
  A collision between moderately sized user interface elements.
- [UIImpactFeedbackGenerator.FeedbackStyle.rigid](./feedbackstyle/rigid.md)
  A collision between user interface elements that are rigid, exhibiting a small amount of compression or elasticity.
- [UIImpactFeedbackGenerator.FeedbackStyle.soft](./feedbackstyle/soft.md)
  A collision between user interface elements that are soft, exhibiting a large amount of compression or elasticity.
### Initializers
- [init?(rawValue: Int)](./feedbackstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Initializing the feedback generator
- [convenience init(style: UIImpactFeedbackGenerator.FeedbackStyle, view: UIView)](./init%28style,view%29.md)
  Creates an impact feedback generator with the specified style and view.
- [init(style: UIImpactFeedbackGenerator.FeedbackStyle)](./init%28style%29.md)
  Creates an impact feedback generator with the specified style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimpactfeedbackgenerator/feedbackstyle)*