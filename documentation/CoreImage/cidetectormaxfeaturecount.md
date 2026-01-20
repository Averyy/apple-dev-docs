# CIDetectorMaxFeatureCount

**Framework**: Core Image  
**Kind**: var

The key to the configuration dictionary whose value represents the maximum number of features the detector should return.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let CIDetectorMaxFeatureCount: String
```

#### Discussion

The default value is 1.  Valid values fall between 1 and 256 inclusive.

## See Also

- [let CIDetectorAccuracy: String](cidetectoraccuracy.md)
  A key used to specify the desired accuracy for the detector.
- [let CIDetectorTracking: String](cidetectortracking.md)
  A key used to enable or disable face tracking for the detector. Use this option when you want to track faces across frames in a video.
- [let CIDetectorMinFeatureSize: String](cidetectorminfeaturesize.md)
  A key used to specify the minimum size that the detector will recognize as a feature.
- [let CIDetectorNumberOfAngles: String](cidetectornumberofangles.md)
  The number of perspectives to use for detecting a face in video input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetectormaxfeaturecount)*