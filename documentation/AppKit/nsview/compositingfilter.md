# compositingFilter

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The Core Image filter used to composite the view’s contents with its background.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var compositingFilter: CIFilter? { get set }
```

```objc
@property (strong, nullable) CIFilter * compositingFilter;
```

## Discussion

This property contains the compositing filter stored in the [`compositingFilter`](../../QuartzCore/calayer/compositingfilter.md) property of the view’s layer. If the view does not have a layer, setting the value of this property has no effect.

The default value of this property is `nil`, which causes content to be rendered without any special compositing effects.

## See Also

### Managing Layer-Related Properties
- [var alphaValue: CGFloat](./alphavalue.md)
  The opacity of the view.
- [var frameCenterRotation: CGFloat](./framecenterrotation.md)
  The rotation angle of the view around the center of its layer.
- [var backgroundFilters: [CIFilter]](./backgroundfilters.md)
  An array of Core Image filters to apply to the view’s background.
- [var contentFilters: [CIFilter]](./contentfilters.md)
  An array of Core Image filters to apply to the contents of the view and its sublayers.
- [var shadow: NSShadow?](./shadow.md)
  The shadow displayed underneath the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/compositingfilter)*