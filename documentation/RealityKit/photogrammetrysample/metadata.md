# metadata

**Framework**: RealityKit  
**Kind**: property

An image’s EXIF metadata.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var metadata: [String : Any] { get set }
```

#### Discussion

You can provide EXIF metadata captured by your digital camera to assist in the object-creation process. During object creation, RealityKit can use data from the EXIF keys listed below.

- `TIFFMake`
- `TIFFModel`
- `TIFFOrientation`
- `ExifBodySerialNumber`
- `ExifLensMake`
- `ExifLensModel`
- `ExifLensSerialNumber`
- `ExifFocalLength`
- `ExifFocalLengthIn35mmFilm`
- `GPSAltitude`
- `GPSAltitudeRef`
- `GPSLatitude`
- `GPSLatitudeRef`
- `GPSLongitude`
- `GPSLongitudeRef`

## See Also

- [let image: CVPixelBuffer](photogrammetrysample/image.md)
  The image data for this sample.
- [var depthDataMap: CVPixelBuffer?](photogrammetrysample/depthdatamap.md)
  The image’s depth data.
- [var gravity: CMAcceleration?](photogrammetrysample/gravity.md)
  An image’s gravity vector.
- [var objectMask: CVPixelBuffer?](photogrammetrysample/objectmask.md)
  The image’s object mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysample/metadata)*