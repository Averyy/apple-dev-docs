# alphaValue

**Framework**: AppKit  
**Kind**: property

The opacity of the view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var alphaValue: CGFloat { get set }
```

#### Discussion

This property contains the [`opacity`](https://developer.apple.com/documentation/QuartzCore/CALayer/opacity) value from the view’s layer. The acceptable range of values for this property are between `0.0` (transparent) and `1.0` (opaque). The default value of this property is `1.0`.

## See Also

- [var frameCenterRotation: CGFloat](nsview/framecenterrotation.md)
  The rotation angle of the view around the center of its layer.
- [var backgroundFilters: [CIFilter]](nsview/backgroundfilters.md)
  An array of Core Image filters to apply to the view’s background.
- [var compositingFilter: CIFilter?](nsview/compositingfilter.md)
  The Core Image filter used to composite the view’s contents with its background.
- [var contentFilters: [CIFilter]](nsview/contentfilters.md)
  An array of Core Image filters to apply to the contents of the view and its sublayers.
- [var shadow: NSShadow?](nsview/shadow.md)
  The shadow displayed underneath the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/alphavalue)*