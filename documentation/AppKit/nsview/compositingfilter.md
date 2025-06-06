# compositingFilter

**Framework**: AppKit  
**Kind**: property

The Core Image filter used to composite the view’s contents with its background.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var compositingFilter: CIFilter? { get set }
```

#### Discussion

This property contains the compositing filter stored in the [`compositingFilter`](https://developer.apple.com/documentation/QuartzCore/CALayer/compositingFilter) property of the view’s layer. If the view does not have a layer, setting the value of this property has no effect.

The default value of this property is `nil`, which causes content to be rendered without any special compositing effects.

## See Also

- [var alphaValue: CGFloat](nsview/alphavalue.md)
  The opacity of the view.
- [var frameCenterRotation: CGFloat](nsview/framecenterrotation.md)
  The rotation angle of the view around the center of its layer.
- [var backgroundFilters: [CIFilter]](nsview/backgroundfilters.md)
  An array of Core Image filters to apply to the view’s background.
- [var contentFilters: [CIFilter]](nsview/contentfilters.md)
  An array of Core Image filters to apply to the contents of the view and its sublayers.
- [var shadow: NSShadow?](nsview/shadow.md)
  The shadow displayed underneath the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/compositingfilter)*