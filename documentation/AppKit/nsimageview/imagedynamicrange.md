# imageDynamicRange

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The resolved dynamic range of the fully resolved image content.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var imageDynamicRange: NSImage.DynamicRange { get }
```

```objc
@property (readonly) NSImageDynamicRange imageDynamicRange;
```

#### Discussion

This property returns [`NSImage.DynamicRange.unspecified`](../nsimage/dynamicrange/unspecified.md) if the image view can’t resolve the image content or the image view hasn’t displayed.

## See Also

### Specifying the dynamic range
- [var preferredImageDynamicRange: NSImage.DynamicRange](./preferredimagedynamicrange.md)
  The preferred dynamic range when displaying an image in the receiving image view.
- [class var defaultPreferredImageDynamicRange: NSImage.DynamicRange](./defaultpreferredimagedynamicrange.md)
  The default preferred image dynamic range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview/imagedynamicrange)*