# CIDetectorMinFeatureSize

**Framework**: Core Image  
**Kind**: var

A key used to specify the minimum size that the detector will recognize as a feature.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
let CIDetectorMinFeatureSize: String
```

#### Discussion

The value for this key is an `NSNumber` object ranging from 0.0 through 1.0 that represents a fraction of the minor dimension of the image.

## See Also

- [let CIDetectorAccuracy: String](cidetectoraccuracy.md)
  A key used to specify the desired accuracy for the detector.
- [let CIDetectorTracking: String](cidetectortracking.md)
  A key used to enable or disable face tracking for the detector. Use this option when you want to track faces across frames in a video.
- [let CIDetectorNumberOfAngles: String](cidetectornumberofangles.md)
  The number of perspectives to use for detecting a face in video input.
- [let CIDetectorMaxFeatureCount: String](cidetectormaxfeaturecount.md)
  The key to the configuration dictionary whose value represents the maximum number of features the detector should return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetectorminfeaturesize)*