# imageDynamicRange

**Framework**: AppKit  
**Kind**: property

The resolved dynamic range of the fully resolved image content.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
var imageDynamicRange: NSImage.DynamicRange { get }
```

#### Discussion

This property returns [`NSImage.DynamicRange.unspecified`](nsimage/dynamicrange/unspecified.md) if the image view can’t resolve the image content or the image view hasn’t displayed.

## See Also

- [var preferredImageDynamicRange: NSImage.DynamicRange](nsimageview/preferredimagedynamicrange.md)
  The preferred dynamic range when displaying an image in the receiving image view.
- [class var defaultPreferredImageDynamicRange: NSImage.DynamicRange](nsimageview/defaultpreferredimagedynamicrange.md)
  The default preferred image dynamic range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview/imagedynamicrange)*