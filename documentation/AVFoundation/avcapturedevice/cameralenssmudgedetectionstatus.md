# cameraLensSmudgeDetectionStatus

**Framework**: AVFoundation  
**Kind**: property

A value specifying the status of camera lens smudge detection.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var cameraLensSmudgeDetectionStatus: AVCaptureCameraLensSmudgeDetectionStatus { get }
```

#### Discussion

During initial detection execution, [`cameraLensSmudgeDetectionStatus`](avcapturedevice/cameralenssmudgedetectionstatus.md) returns `AVCaptureCameraLensSmudgeDetectionStatusUnknown` until the detection result settles. Once a detection result is produced, [`cameraLensSmudgeDetectionStatus`](avcapturedevice/cameralenssmudgedetectionstatus.md) returns the most recent detection result. This property can be key-value observed.

## See Also

- [var isCameraLensSmudgeDetectionEnabled: Bool](avcapturedevice/iscameralenssmudgedetectionenabled.md)
  Whether camera lens smudge detection is enabled.
- [func setCameraLensSmudgeDetectionEnabled(Bool, detectionInterval: CMTime)](avcapturedevice/setcameralenssmudgedetectionenabled(_:detectioninterval:).md)
  Specify whether to enable camera lens smudge detection, and the interval time between each run of detections.
- [var cameraLensSmudgeDetectionInterval: CMTime](avcapturedevice/cameralenssmudgedetectioninterval.md)
  The camera lens smudge detection interval.
- [enum AVCaptureCameraLensSmudgeDetectionStatus](avcapturecameralenssmudgedetectionstatus.md)
  Constants indicating the current camera lens smudge detection status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/cameralenssmudgedetectionstatus)*