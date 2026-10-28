# visiblePath

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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
var visiblePath: UIBezierPath? { get set }
```

```objc
@property (nonatomic, copy, nullable) UIBezierPath * visiblePath;
```

## Discussion

Specify the path information in the coordinate space of the view being animated.

## See Also

### Configuring the preview attributes
- [var backgroundColor: UIColor!](./backgroundcolor.md)
  The background color to display behind the preview.
- [var shadowPath: UIBezierPath?](./shadowpath.md)
  The path to use for drawing the preview’s shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewparameters/visiblepath)*