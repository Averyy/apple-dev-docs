# isCameraLensSmudgeDetectionEnabled

**Framework**: AVFoundation  
**Kind**: property

Whether camera lens smudge detection is enabled.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var isCameraLensSmudgeDetectionEnabled: Bool { get }
```

#### Discussion

You enable lens smudge detection by calling [`setCameraLensSmudgeDetectionEnabled(_:detectionInterval:)`](avcapturedevice/setcameralenssmudgedetectionenabled(_:detectioninterval:).md). By default, this property is returns `false`.

## See Also

- [func setCameraLensSmudgeDetectionEnabled(Bool, detectionInterval: CMTime)](avcapturedevice/setcameralenssmudgedetectionenabled(_:detectioninterval:).md)
  Specify whether to enable camera lens smudge detection, and the interval time between each run of detections.
- [var cameraLensSmudgeDetectionInterval: CMTime](avcapturedevice/cameralenssmudgedetectioninterval.md)
  The camera lens smudge detection interval.
- [var cameraLensSmudgeDetectionStatus: AVCaptureCameraLensSmudgeDetectionStatus](avcapturedevice/cameralenssmudgedetectionstatus.md)
  A value specifying the status of camera lens smudge detection.
- [enum AVCaptureCameraLensSmudgeDetectionStatus](avcapturecameralenssmudgedetectionstatus.md)
  Constants indicating the current camera lens smudge detection status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/iscameralenssmudgedetectionenabled)*