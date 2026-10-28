# matteType

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) AVSemanticSegmentationMatteType matteType;
```

## Discussion

A semantic segmentation matte’s [`matteType`](./mattetype-swift.property.md) is immutable for the life of the object.

## See Also

### Inspecting a segmentation matte
- [AVSemanticSegmentationMatte.MatteType](./mattetype-swift.struct.md)
  A structure that defines the types of segmentation matte images that you can capture along with the primary image.
- [var mattingImage: CVPixelBuffer](./mattingimage.md)
  The semantic segmentation matte’s internal image.
- [var pixelFormatType: OSType](./pixelformattype.md)
  The pixel format type for this object’s internal matting image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte/mattetype-swift.property)*