# pixelFormatType

**Framework**: AVFoundation  
**Kind**: property

The pixel format type of this portrait effects matte’s internal image.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var pixelFormatType: OSType { get }
```

#### Discussion

The only supported pixel format type for the matting image is [`kCVPixelFormatType_OneComponent8`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_OneComponent8).

## See Also

- [Extracting Portrait Effects matte image data from a photo](extracting-portrait-effects-matte-image-data-from-a-photo.md)
  Check for portrait effects matte metadata in existing images.
- [var mattingImage: CVPixelBuffer](avportraiteffectsmatte/mattingimage.md)
  The portrait effects matte’s internal image, formatted as a pixel buffer.
- [func dictionaryRepresentation(forAuxiliaryDataType: AutoreleasingUnsafeMutablePointer<NSString?>?) -> [AnyHashable : Any]?](avportraiteffectsmatte/dictionaryrepresentation(forauxiliarydatatype:).md)
  A dictionary of primitive map information used for writing an image file with a portrait effects matte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avportraiteffectsmatte/pixelformattype)*