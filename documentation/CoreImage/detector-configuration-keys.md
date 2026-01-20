# Detector Configuration Keys

**Framework**: Core Image

Keys used in the options dictionary to configure a detector.

## Topics

### Constants
- [let CIDetectorAccuracy: String](cidetectoraccuracy.md)
  A key used to specify the desired accuracy for the detector.
- [let CIDetectorTracking: String](cidetectortracking.md)
  A key used to enable or disable face tracking for the detector. Use this option when you want to track faces across frames in a video.
- [let CIDetectorMinFeatureSize: String](cidetectorminfeaturesize.md)
  A key used to specify the minimum size that the detector will recognize as a feature.
- [let CIDetectorNumberOfAngles: String](cidetectornumberofangles.md)
  The number of perspectives to use for detecting a face in video input.
- [let CIDetectorMaxFeatureCount: String](cidetectormaxfeaturecount.md)
  The key to the configuration dictionary whose value represents the maximum number of features the detector should return.

## See Also

- [Detector Types](detector-types.md)
  Strings used to declare the detector for which you are interested.
- [Detector Accuracy Options](detector-accuracy-options.md)
  Value options used to specify the desired accuracy of the detector.
- [Feature Detection Keys](feature-detection-keys.md)
  Keys used in the options dictionary for [`features(in:options:)`](cidetector/features(in:options:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/detector-configuration-keys)*