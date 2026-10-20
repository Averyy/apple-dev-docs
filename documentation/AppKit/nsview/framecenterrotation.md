# frameCenterRotation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The rotation angle of the view around the center of its layer.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var frameCenterRotation: CGFloat { get set }
```

```objc
@property CGFloat frameCenterRotation;
```

#### Discussion

This property contains the angle of rotation of the view’s frame around its center. If you changed the underlying layer’s [`anchorPoint`](../../QuartzCore/calayer/anchorpoint.md) property, the result of setting this property is undefined.

## See Also

### Managing Layer-Related Properties
- [var alphaValue: CGFloat](./alphavalue.md)
  The opacity of the view.
- [var backgroundFilters: [CIFilter]](./backgroundfilters.md)
  An array of Core Image filters to apply to the view’s background.
- [var compositingFilter: CIFilter?](./compositingfilter.md)
  The Core Image filter used to composite the view’s contents with its background.
- [var contentFilters: [CIFilter]](./contentfilters.md)
  An array of Core Image filters to apply to the contents of the view and its sublayers.
- [var shadow: NSShadow?](./shadow.md)
  The shadow displayed underneath the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/framecenterrotation)*