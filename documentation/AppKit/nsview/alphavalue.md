# alphaValue

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The opacity of the view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var alphaValue: CGFloat { get set }
```

```objc
@property CGFloat alphaValue;
```

## Discussion

This property contains the [`opacity`](../../QuartzCore/calayer/opacity.md) value from the view’s layer. The acceptable range of values for this property are between `0.0` (transparent) and `1.0` (opaque). The default value of this property is `1.0`.

## See Also

### Managing Layer-Related Properties
- [var frameCenterRotation: CGFloat](./framecenterrotation.md)
  The rotation angle of the view around the center of its layer.
- [var backgroundFilters: [CIFilter]](./backgroundfilters.md)
  An array of Core Image filters to apply to the view’s background.
- [var compositingFilter: CIFilter?](./compositingfilter.md)
  The Core Image filter used to composite the view’s contents with its background.
- [var contentFilters: [CIFilter]](./contentfilters.md)
  An array of Core Image filters to apply to the contents of the view and its sublayers.
- [var shadow: NSShadow?](./shadow.md)
  The shadow displayed underneath the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/alphavalue)*