# prefersHighDynamicRange

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the image reader should decode the image as HDR when the type is capable of decoding in either SDR or HDR.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@property (nonatomic, assign, readwrite) BOOL prefersHighDynamicRange;
```

#### Discussion

This property doesn’t affect images that only decode in either SDR or HDR. The default value depends on the system capabilities.

## See Also

### Related Documentation
- [Applying Apple HDR effect to your photos](../../AppKit/applying-apple-hdr-effect-to-your-photos.md)
  You can decode and apply Apple’s HDR gain map to your own images.
### Configuration properties
- [preferredThumbnailSize](./preferredthumbnailsize.md)
  The thumbnail size in pixels that the image reader makes the image.
- [preparesImagesForDisplay](./preparesimagesfordisplay.md)
  A Boolean value that indicates whether the image reader prepares the image for display.
- [pixelsPerInch](./pixelsperinch.md)
  The integral scale that the image reader applies to the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagereaderconfiguration/prefershighdynamicrange)*