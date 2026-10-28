# preparesImagesForDisplay

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the image reader prepares the image for display.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@property (nonatomic, assign, readwrite) BOOL preparesImagesForDisplay;
```

## Discussion

The default value is [`false`](../../Swift/false.md).

## See Also

### Configuration properties
- [prefersHighDynamicRange](./prefershighdynamicrange.md)
  A Boolean value that indicates whether the image reader should decode the image as HDR when the type is capable of decoding in either SDR or HDR.
- [preferredThumbnailSize](./preferredthumbnailsize.md)
  The thumbnail size in pixels that the image reader makes the image.
- [pixelsPerInch](./pixelsperinch.md)
  The integral scale that the image reader applies to the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagereaderconfiguration/preparesimagesfordisplay)*