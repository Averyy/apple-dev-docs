# contentFilters

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of Core Image filters to apply to the contents of the view and its sublayers.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var contentFilters: [CIFilter] { get set }
```

```objc
@property (copy) NSArray<__kindof CIFilter *> * contentFilters;
```

#### Discussion

This property contains an array of [`CIFilter`](../../CoreImage/cifilter-swift.class.md) objects. This array represents the filters stored in the [`filters`](../../QuartzCore/calayer/filters.md) property of the view’s layer. If the view does not have a layer, setting the value of this property has no effect.

The default value of this property is an empty array.

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
- [var shadow: NSShadow?](./shadow.md)
  The shadow displayed underneath the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/contentfilters)*