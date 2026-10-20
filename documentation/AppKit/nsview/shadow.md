# shadow

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The shadow displayed underneath the view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@NSCopying
var shadow: NSShadow? { get set }
```

```objc
@property (copy, nullable) NSShadow * shadow;
```

#### Return Value

An instance of `NSShadow` that is created using the [`shadowColor`](../../QuartzCore/calayer/shadowcolor.md),[`shadowOffset`](../../QuartzCore/calayer/shadowoffset.md), [`shadowOpacity`](../../QuartzCore/calayer/shadowopacity.md), and [`shadowRadius`](../../QuartzCore/calayer/shadowradius.md) properties of the view’s layer.

#### Discussion

The default value of this property is normally `nil`. When you configure any of the shadow-related properties on the view’s layer, such as the [`shadowColor`](../../QuartzCore/calayer/shadowcolor.md),[`shadowOffset`](../../QuartzCore/calayer/shadowoffset.md), [`shadowOpacity`](../../QuartzCore/calayer/shadowopacity.md) or [`shadowRadius`](../../QuartzCore/calayer/shadowradius.md) properties, this property contains the [`NSShadow`](../nsshadow.md) object that encapsulates that information. Assigning a new shadow object to this property sets the corresponding shadow-related properties on the view’s layer.

If the view does not have a layer, setting the value of this property has no effect.

## See Also

### Managing Layer-Related Properties
- [var alphaValue: CGFloat](./alphavalue.md)
  The opacity of the view.
- [var frameCenterRotation: CGFloat](./framecenterrotation.md)
  The rotation angle of the view around the center of its layer.
- [var backgroundFilters: [CIFilter]](./backgroundfilters.md)
  An array of Core Image filters to apply to the view’s background.
- [var compositingFilter: CIFilter?](./compositingfilter.md)
  The Core Image filter used to composite the view’s contents with its background.
- [var contentFilters: [CIFilter]](./contentfilters.md)
  An array of Core Image filters to apply to the contents of the view and its sublayers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/shadow)*