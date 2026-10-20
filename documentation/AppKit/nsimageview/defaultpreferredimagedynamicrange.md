# defaultPreferredImageDynamicRange

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The default preferred image dynamic range.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class var defaultPreferredImageDynamicRange: NSImage.DynamicRange { get set }
```

```objc
@property (class) NSImageDynamicRange defaultPreferredImageDynamicRange;
```

#### Discussion

This property defaults to [`NSImage.DynamicRange.constrainedHigh`](../nsimage/dynamicrange/constrainedhigh.md) on macOS 14 and higher, and [`NSImage.DynamicRange.standard`](../nsimage/dynamicrange/standard.md) otherwise. Set this property to another [`NSImage.DynamicRange`](../nsimage/dynamicrange.md) value to change the default for all subsequently created image views in your app.

## See Also

### Specifying the dynamic range
- [var imageDynamicRange: NSImage.DynamicRange](./imagedynamicrange.md)
  The resolved dynamic range of the fully resolved image content.
- [var preferredImageDynamicRange: NSImage.DynamicRange](./preferredimagedynamicrange.md)
  The preferred dynamic range when displaying an image in the receiving image view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview/defaultpreferredimagedynamicrange)*