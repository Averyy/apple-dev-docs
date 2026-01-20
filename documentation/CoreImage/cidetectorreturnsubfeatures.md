# CIDetectorReturnSubFeatures

**Framework**: Core Image  
**Kind**: var

An option specifying whether to return feature information for components of detected features.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let CIDetectorReturnSubFeatures: String
```

#### Discussion

The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object with a Boolean value. Use this option with the [`CIDetectorTypeText`](cidetectortypetext.md) detector type to choose whether to detect only regions likely to contain text ([`false`](https://developer.apple.com/documentation/Swift/false), the default) or to also identify sub-regions likely to contain individual characters of text ([`true`](https://developer.apple.com/documentation/Swift/true)).

## See Also

- [let CIDetectorImageOrientation: String](cidetectorimageorientation.md)
  An option for the display orientation of the image whose features you want to detect.
- [let CIDetectorEyeBlink: String](cidetectoreyeblink.md)
  An option for whether Core Image will perform additional processing to recognize closed eyes in detected faces.
- [let CIDetectorSmile: String](cidetectorsmile.md)
  An option for whether Core Image will perform additional processing to recognize smiles in detected faces.
- [let CIDetectorFocalLength: String](cidetectorfocallength.md)
  An option identifying the focal length in pixels used in capturing images to be processed by the detector.
- [let CIDetectorAspectRatio: String](cidetectoraspectratio.md)
  An option specifying the aspect ratio (width divided by height) of rectangles to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetectorreturnsubfeatures)*