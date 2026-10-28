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
- visionOS
- watchOS 10.0+

## Declaration

```swift
var prefersHighDynamicRange: Bool { get set }
```

## Discussion

This property doesn’t affect images that only decode in either SDR or HDR. The default value depends on the system capabilities.

## See Also

### Related Documentation
- [Applying Apple HDR effect to your photos](../../../AppKit/applying-apple-hdr-effect-to-your-photos.md)
  You can decode and apply Apple’s HDR gain map to your own images.
### Configuration properties
- [var preparesImagesForDisplay: Bool](./preparesimagesfordisplay.md)
  A Boolean value that indicates whether the image reader prepares the image for display.
- [var preferredThumbnailSize: CGSize](./preferredthumbnailsize.md)
  The thumbnail size in pixels that the image reader makes the image.
- [var pixelsPerInch: Double](./pixelsperinch.md)
  The integral scale that the image reader applies to the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagereader-swift.struct/configuration-swift.struct/prefershighdynamicrange)*