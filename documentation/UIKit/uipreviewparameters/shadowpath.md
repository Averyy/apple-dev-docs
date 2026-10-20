# shadowPath

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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
var shadowPath: UIBezierPath? { get set }
```

```objc
@property (nonatomic, copy, nullable) UIBezierPath * shadowPath;
```

#### Discussion

If `nil`, the system uses the [`visiblePath`](./visiblepath.md) to draw the shadow.

## See Also

### Configuring the preview attributes
- [var backgroundColor: UIColor!](./backgroundcolor.md)
  The background color to display behind the preview.
- [var visiblePath: UIBezierPath?](./visiblepath.md)
  The portion of the view to show in the preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewparameters/shadowpath)*