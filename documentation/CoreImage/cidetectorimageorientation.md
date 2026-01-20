# CIDetectorImageOrientation

**Framework**: Core Image  
**Kind**: var

An option for the display orientation of the image whose features you want to detect.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
let CIDetectorImageOrientation: String
```

#### Discussion

The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object whose value is an integer between `1` and `8`. The TIFF and EXIF specifications define these values to indicate where the pixel coordinate origin (0,0) of the image should appear when it is displayed. The default value is `1`, indicating that the origin is in the top left corner of the image. For further details, see [`kCGImagePropertyOrientation`](https://developer.apple.com/documentation/ImageIO/kCGImagePropertyOrientation).

Core Image detects only faces whose orientation matches that of the image. You should provide a value for this key if you want to detect faces in a different orientation.

## See Also

- [let CIDetectorEyeBlink: String](cidetectoreyeblink.md)
  An option for whether Core Image will perform additional processing to recognize closed eyes in detected faces.
- [let CIDetectorSmile: String](cidetectorsmile.md)
  An option for whether Core Image will perform additional processing to recognize smiles in detected faces.
- [let CIDetectorFocalLength: String](cidetectorfocallength.md)
  An option identifying the focal length in pixels used in capturing images to be processed by the detector.
- [let CIDetectorAspectRatio: String](cidetectoraspectratio.md)
  An option specifying the aspect ratio (width divided by height) of rectangles to search for.
- [let CIDetectorReturnSubFeatures: String](cidetectorreturnsubfeatures.md)
  An option specifying whether to return feature information for components of detected features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetectorimageorientation)*