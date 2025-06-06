# shadowPath

**Framework**: UIKit  
**Kind**: property

The path to use for drawing the preview’s shadow.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var shadowPath: UIBezierPath? { get set }
```

#### Discussion

If `nil`, the system uses the [`visiblePath`](uipreviewparameters/visiblepath.md) to draw the shadow.

## See Also

- [var backgroundColor: UIColor!](uipreviewparameters/backgroundcolor.md)
  The background color to display behind the preview.
- [var visiblePath: UIBezierPath?](uipreviewparameters/visiblepath.md)
  The portion of the view to show in the preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewparameters/shadowpath)*