# init(style:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates an impact feedback generator with the specified style.

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2

> **Deprecated**: Use [`init(style:view:)`](./init%28style,view%29.md) instead.

## Declaration

```swift
init(style: UIImpactFeedbackGenerator.FeedbackStyle)
```

```objc
- (instancetype) initWithStyle:(UIImpactFeedbackStyle) style;
```

#### Return Value

A newly initialized feedback generator.

#### Discussion

For more information on using feedback generators, see `Using feedback generators`.

## Parameters

- `style`: A value representing the mass of the colliding objects. For a list of valid feedback styles, see the [`UIImpactFeedbackGenerator.FeedbackStyle`](./feedbackstyle.md) enumeration.

## See Also

### Initializing the feedback generator
- [convenience init(style: UIImpactFeedbackGenerator.FeedbackStyle, view: UIView)](./init%28style,view%29.md)
  Creates an impact feedback generator with the specified style and view.
- [UIImpactFeedbackGenerator.FeedbackStyle](./feedbackstyle.md)
  The mass of the objects in the collision simulated by an impact feedback generator object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimpactfeedbackgenerator/init(style:))*