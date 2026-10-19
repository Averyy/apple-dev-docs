# init(style:)

**Framework**: UIKit  
**Kind**: init

Creates an impact feedback generator with the specified style.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(style: UIImpactFeedbackGenerator.FeedbackStyle)
```

#### Return Value

A newly initialized feedback generator.

#### Discussion

For more information on using feedback generators, see `Using feedback generators`.

## Parameters

- `style`: A value representing the mass of the colliding objects. For a list of valid feedback styles, see the [`UIImpactFeedbackGenerator.FeedbackStyle`](uiimpactfeedbackgenerator/feedbackstyle.md) enumeration.

## See Also

- [convenience init(style: UIImpactFeedbackGenerator.FeedbackStyle, view: UIView)](uiimpactfeedbackgenerator/init(style:view:).md)
  Creates an impact feedback generator with the specified style and view.
- [UIImpactFeedbackGenerator.FeedbackStyle](uiimpactfeedbackgenerator/feedbackstyle.md)
  The mass of the objects in the collision simulated by an impact feedback generator object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimpactfeedbackgenerator/init(style:))*