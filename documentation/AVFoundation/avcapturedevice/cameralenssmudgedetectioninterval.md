# cameraLensSmudgeDetectionInterval

**Framework**: AVFoundation  
**Kind**: property

The camera lens smudge detection interval.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var cameraLensSmudgeDetectionInterval: CMTime { get }
```

#### Discussion

[`cameraLensSmudgeDetectionInterval`](avcapturedevice/cameralenssmudgedetectioninterval.md) is set by calling [`setCameraLensSmudgeDetectionEnabled(_:detectionInterval:)`](avcapturedevice/setcameralenssmudgedetectionenabled(_:detectioninterval:).md). By default, this property returns `kCMTimeInvalid`.

## See Also

- [var isCameraLensSmudgeDetectionEnabled: Bool](avcapturedevice/iscameralenssmudgedetectionenabled.md)
  Whether camera lens smudge detection is enabled.
- [func setCameraLensSmudgeDetectionEnabled(Bool, detectionInterval: CMTime)](avcapturedevice/setcameralenssmudgedetectionenabled(_:detectioninterval:).md)
  Specify whether to enable camera lens smudge detection, and the interval time between each run of detections.
- [var cameraLensSmudgeDetectionStatus: AVCaptureCameraLensSmudgeDetectionStatus](avcapturedevice/cameralenssmudgedetectionstatus.md)
  A value specifying the status of camera lens smudge detection.
- [enum AVCaptureCameraLensSmudgeDetectionStatus](avcapturecameralenssmudgedetectionstatus.md)
  Constants indicating the current camera lens smudge detection status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/cameralenssmudgedetectioninterval)*