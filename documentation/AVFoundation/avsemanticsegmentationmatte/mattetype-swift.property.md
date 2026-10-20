# matteType

**Framework**: AVFoundation  
**Kind**: property

The semantic segmentation matte image type.

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
var matteType: AVSemanticSegmentationMatte.MatteType { get }
```

#### Discussion

A semantic segmentation matte’s [`matteType`](avsemanticsegmentationmatte/mattetype-swift.property.md) is immutable for the life of the object.

## See Also

- [AVSemanticSegmentationMatte.MatteType](avsemanticsegmentationmatte/mattetype-swift.struct.md)
  A structure that defines the types of segmentation matte images that you can capture along with the primary image.
- [var mattingImage: CVPixelBuffer](avsemanticsegmentationmatte/mattingimage.md)
  The semantic segmentation matte’s internal image.
- [var pixelFormatType: OSType](avsemanticsegmentationmatte/pixelformattype.md)
  The pixel format type for this object’s internal matting image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte/mattetype-swift.property)*