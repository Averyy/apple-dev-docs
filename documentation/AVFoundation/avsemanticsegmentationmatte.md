# AVSemanticSegmentationMatte

**Framework**: AVFoundation  
**Kind**: class

An object that wraps a matting image for a particular semantic segmentation.

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
class AVSemanticSegmentationMatte
```

#### Overview

The matting image stores its pixel data as [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/cvpixelbuffer-q2e) objects in [`kCVPixelFormatType_OneComponent8`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_OneComponent8) format. The image file contains the semantic segmentation matte as an auxiliary image, accessible using the ImageIO framework’s [`CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)`](https://developer.apple.com/documentation/ImageIO/CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)) function.

## Topics

### Creating a segmentation matte
- [convenience init(fromImageSourceAuxiliaryDataType: CFString, dictionaryRepresentation: [AnyHashable : Any]) throws](avsemanticsegmentationmatte/init(fromimagesourceauxiliarydatatype:dictionaryrepresentation:).md)
  Returns a new semantic segmentation matte instance from auxiliary image information in an image file.
- [func replacingSemanticSegmentationMatte(with: CVPixelBuffer) throws -> Self](avsemanticsegmentationmatte/replacingsemanticsegmentationmatte(with:).md)
  Returns a semantic segmentation matte instance that wraps the replacement pixel buffer.
- [func applyingExifOrientation(CGImagePropertyOrientation) -> Self](avsemanticsegmentationmatte/applyingexiforientation(_:).md)
  Returns a new semantic segmentation matte instance with the specified Exif orientation applied.
- [func dictionaryRepresentation(forAuxiliaryDataType: AutoreleasingUnsafeMutablePointer<NSString?>?) -> [AnyHashable : Any]?](avsemanticsegmentationmatte/dictionaryrepresentation(forauxiliarydatatype:).md)
  Returns a dictionary of primitive map information to use when writing an image file with a semantic segmentation matte.
### Inspecting a segmentation matte
- [var matteType: AVSemanticSegmentationMatte.MatteType](avsemanticsegmentationmatte/mattetype-swift.property.md)
  The semantic segmentation matte image type.
- [AVSemanticSegmentationMatte.MatteType](avsemanticsegmentationmatte/mattetype-swift.struct.md)
  A structure that defines the types of segmentation matte images that you can capture along with the primary image.
- [var mattingImage: CVPixelBuffer](avsemanticsegmentationmatte/mattingimage.md)
  The semantic segmentation matte’s internal image.
- [var pixelFormatType: OSType](avsemanticsegmentationmatte/pixelformattype.md)
  The pixel format type for this object’s internal matting image.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVPortraitEffectsMatte](avportraiteffectsmatte.md)
  An auxiliary image used to separate foreground from background with high resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte)*