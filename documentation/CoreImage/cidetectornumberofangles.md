# CIDetectorNumberOfAngles

**Framework**: Core Image  
**Kind**: var

The number of perspectives to use for detecting a face in video input.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let CIDetectorNumberOfAngles: String
```

#### Discussion

The value for this key is an `NSNumber` object containing the number 1, 3, 5, 7, 9, or 11. At higher numbers of angles, face detection in video becomes more accurate, but at a higher computational cost.

## See Also

- [let CIDetectorAccuracy: String](cidetectoraccuracy.md)
  A key used to specify the desired accuracy for the detector.
- [let CIDetectorTracking: String](cidetectortracking.md)
  A key used to enable or disable face tracking for the detector. Use this option when you want to track faces across frames in a video.
- [let CIDetectorMinFeatureSize: String](cidetectorminfeaturesize.md)
  A key used to specify the minimum size that the detector will recognize as a feature.
- [let CIDetectorMaxFeatureCount: String](cidetectormaxfeaturecount.md)
  The key to the configuration dictionary whose value represents the maximum number of features the detector should return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetectornumberofangles)*