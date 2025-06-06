# pixelFormatType

**Framework**: AVFoundation  
**Kind**: property

The pixel format type for this object’s internal matting image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var pixelFormatType: OSType { get }
```

#### Discussion

Currently, the only supported pixel format type for the matting image is [`kCVPixelFormatType_OneComponent8`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_OneComponent8).

## See Also

- [var matteType: AVSemanticSegmentationMatte.MatteType](avsemanticsegmentationmatte/mattetype-swift.property.md)
  The semantic segmentation matte image type.
- [AVSemanticSegmentationMatte.MatteType](avsemanticsegmentationmatte/mattetype-swift.struct.md)
  A structure that defines the types of segmentation matte images that you can capture along with the primary image.
- [var mattingImage: CVPixelBuffer](avsemanticsegmentationmatte/mattingimage.md)
  The semantic segmentation matte’s internal image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte/pixelformattype)*