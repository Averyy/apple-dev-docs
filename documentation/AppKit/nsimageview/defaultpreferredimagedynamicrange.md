# defaultPreferredImageDynamicRange

**Framework**: AppKit  
**Kind**: property

The default preferred image dynamic range.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
class var defaultPreferredImageDynamicRange: NSImage.DynamicRange { get set }
```

#### Discussion

This property defaults to [`NSImage.DynamicRange.constrainedHigh`](nsimage/dynamicrange/constrainedhigh.md) on macOS 14 and higher, and [`NSImage.DynamicRange.standard`](nsimage/dynamicrange/standard.md) otherwise. Set this property to another [`NSImage.DynamicRange`](nsimage/dynamicrange.md) value to change the default for all subsequently created image views in your app.

## See Also

- [var imageDynamicRange: NSImage.DynamicRange](nsimageview/imagedynamicrange.md)
  The resolved dynamic range of the fully resolved image content.
- [var preferredImageDynamicRange: NSImage.DynamicRange](nsimageview/preferredimagedynamicrange.md)
  The preferred dynamic range when displaying an image in the receiving image view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview/defaultpreferredimagedynamicrange)*