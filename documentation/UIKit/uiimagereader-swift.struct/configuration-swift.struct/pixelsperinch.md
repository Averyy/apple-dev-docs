# pixelsPerInch

**Framework**: UIKit  
**Kind**: property

The integral scale that the image reader applies to the image.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
var pixelsPerInch: Double { get set }
```

#### Discussion

The default value is `0` which indicates a `1.0` scale.

## See Also

- [var prefersHighDynamicRange: Bool](uiimagereader-swift.struct/configuration-swift.struct/prefershighdynamicrange.md)
  A Boolean value that indicates whether the image reader should decode the image as HDR when the type is capable of decoding in either SDR or HDR.
- [var preparesImagesForDisplay: Bool](uiimagereader-swift.struct/configuration-swift.struct/preparesimagesfordisplay.md)
  A Boolean value that indicates whether the image reader prepares the image for display.
- [var preferredThumbnailSize: CGSize](uiimagereader-swift.struct/configuration-swift.struct/preferredthumbnailsize.md)
  The thumbnail size in pixels that the image reader makes the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagereader-swift.struct/configuration-swift.struct/pixelsperinch)*