# visiblePath

**Framework**: UIKit  
**Kind**: property

The portion of the view to show in the preview.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var visiblePath: UIBezierPath? { get set }
```

#### Discussion

Specify the path information in the coordinate space of the view being animated.

## See Also

- [var backgroundColor: UIColor!](uipreviewparameters/backgroundcolor.md)
  The background color to display behind the preview.
- [var shadowPath: UIBezierPath?](uipreviewparameters/shadowpath.md)
  The path to use for drawing the preview’s shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewparameters/visiblepath)*