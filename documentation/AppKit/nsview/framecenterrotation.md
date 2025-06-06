# frameCenterRotation

**Framework**: AppKit  
**Kind**: property

The rotation angle of the view around the center of its layer.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var frameCenterRotation: CGFloat { get set }
```

#### Discussion

This property contains the angle of rotation of the view’s frame around its center. If you changed the underlying layer’s [`anchorPoint`](https://developer.apple.com/documentation/QuartzCore/CALayer/anchorPoint) property, the result of setting this property is undefined.

## See Also

- [var alphaValue: CGFloat](nsview/alphavalue.md)
  The opacity of the view.
- [var backgroundFilters: [CIFilter]](nsview/backgroundfilters.md)
  An array of Core Image filters to apply to the view’s background.
- [var compositingFilter: CIFilter?](nsview/compositingfilter.md)
  The Core Image filter used to composite the view’s contents with its background.
- [var contentFilters: [CIFilter]](nsview/contentfilters.md)
  An array of Core Image filters to apply to the contents of the view and its sublayers.
- [var shadow: NSShadow?](nsview/shadow.md)
  The shadow displayed underneath the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/framecenterrotation)*