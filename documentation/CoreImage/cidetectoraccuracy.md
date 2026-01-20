# CIDetectorAccuracy

**Framework**: Core Image  
**Kind**: var

A key used to specify the desired accuracy for the detector.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
let CIDetectorAccuracy: String
```

#### Discussion

The value associated with the key should be one of the values found in [`Detector Accuracy Options`](detector-accuracy-options.md).

## See Also

- [let CIDetectorTracking: String](cidetectortracking.md)
  A key used to enable or disable face tracking for the detector. Use this option when you want to track faces across frames in a video.
- [let CIDetectorMinFeatureSize: String](cidetectorminfeaturesize.md)
  A key used to specify the minimum size that the detector will recognize as a feature.
- [let CIDetectorNumberOfAngles: String](cidetectornumberofangles.md)
  The number of perspectives to use for detecting a face in video input.
- [let CIDetectorMaxFeatureCount: String](cidetectormaxfeaturecount.md)
  The key to the configuration dictionary whose value represents the maximum number of features the detector should return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetectoraccuracy)*