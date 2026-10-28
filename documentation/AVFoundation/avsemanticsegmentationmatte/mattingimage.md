# mattingImage

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The semantic segmentation matte’s internal image.

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
var mattingImage: CVPixelBuffer { get }
```

```objc
@property (readonly) CVPixelBufferRef mattingImage;
```

## Discussion

You can determine the pixel buffer’s format type using the [`pixelFormatType`](./pixelformattype.md) property.

## See Also

### Inspecting a segmentation matte
- [var matteType: AVSemanticSegmentationMatte.MatteType](./mattetype-swift.property.md)
  The semantic segmentation matte image type.
- [AVSemanticSegmentationMatte.MatteType](./mattetype-swift.struct.md)
  A structure that defines the types of segmentation matte images that you can capture along with the primary image.
- [var pixelFormatType: OSType](./pixelformattype.md)
  The pixel format type for this object’s internal matting image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte/mattingimage)*