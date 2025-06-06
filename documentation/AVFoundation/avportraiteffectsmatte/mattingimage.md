# mattingImage

**Framework**: AVFoundation  
**Kind**: property

The portrait effects matte’s internal image, formatted as a pixel buffer.

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
var mattingImage: CVPixelBuffer { get }
```

#### Discussion

Query the pixel format using the [`pixelFormatType`](avportraiteffectsmatte/pixelformattype.md) property.

## See Also

- [Extracting Portrait Effects Matte Image Data from a Photo](extracting-portrait-effects-matte-image-data-from-a-photo.md)
  Check for portrait effects matte metadata in existing images.
- [var pixelFormatType: OSType](avportraiteffectsmatte/pixelformattype.md)
  The pixel format type of this portrait effects matte’s internal image.
- [func dictionaryRepresentation(forAuxiliaryDataType: AutoreleasingUnsafeMutablePointer<NSString?>?) -> [AnyHashable : Any]?](avportraiteffectsmatte/dictionaryrepresentation(forauxiliarydatatype:).md)
  A dictionary of primitive map information used for writing an image file with a portrait effects matte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avportraiteffectsmatte/mattingimage)*