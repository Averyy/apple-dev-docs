# shadow

**Framework**: AppKit  
**Kind**: property

The shadow displayed underneath the view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@NSCopying
var shadow: NSShadow? { get set }
```

#### Return Value

An instance of `NSShadow` that is created using the [`shadowColor`](https://developer.apple.com/documentation/quartzcore/calayer/shadowcolor),[`shadowOffset`](https://developer.apple.com/documentation/quartzcore/calayer/shadowoffset), [`shadowOpacity`](https://developer.apple.com/documentation/quartzcore/calayer/shadowopacity), and [`shadowRadius`](https://developer.apple.com/documentation/quartzcore/calayer/shadowradius) properties of the view’s layer.

#### Discussion

The default value of this property is normally `nil`. When you configure any of the shadow-related properties on the view’s layer, such as the [`shadowColor`](https://developer.apple.com/documentation/quartzcore/calayer/shadowcolor),[`shadowOffset`](https://developer.apple.com/documentation/quartzcore/calayer/shadowoffset), [`shadowOpacity`](https://developer.apple.com/documentation/quartzcore/calayer/shadowopacity) or [`shadowRadius`](https://developer.apple.com/documentation/quartzcore/calayer/shadowradius) properties, this property contains the [`NSShadow`](nsshadow.md) object that encapsulates that information. Assigning a new shadow object to this property sets the corresponding shadow-related properties on the view’s layer.

If the view does not have a layer, setting the value of this property has no effect.

## See Also

- [var alphaValue: CGFloat](nsview/alphavalue.md)
  The opacity of the view.
- [var frameCenterRotation: CGFloat](nsview/framecenterrotation.md)
  The rotation angle of the view around the center of its layer.
- [var backgroundFilters: [CIFilter]](nsview/backgroundfilters.md)
  An array of Core Image filters to apply to the view’s background.
- [var compositingFilter: CIFilter?](nsview/compositingfilter.md)
  The Core Image filter used to composite the view’s contents with its background.
- [var contentFilters: [CIFilter]](nsview/contentfilters.md)
  An array of Core Image filters to apply to the contents of the view and its sublayers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/shadow)*