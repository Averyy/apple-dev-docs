# AVCaptureCameraLensSmudgeDetectionStatus

**Framework**: AVFoundation  
**Kind**: enum

Constants indicating the current camera lens smudge detection status.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
enum AVCaptureCameraLensSmudgeDetectionStatus
```

## Topics

### Status values
- [AVCaptureCameraLensSmudgeDetectionStatus.disabled](avcapturecameralenssmudgedetectionstatus/disabled.md)
  Indicates that the detection is not enabled.
- [AVCaptureCameraLensSmudgeDetectionStatus.smudgeNotDetected](avcapturecameralenssmudgedetectionstatus/smudgenotdetected.md)
  Indicates that the most recent detection found no smudge on the camera lens.
- [AVCaptureCameraLensSmudgeDetectionStatus.smudged](avcapturecameralenssmudgedetectionstatus/smudged.md)
  Indicates that the most recent detection found the camera lens to be smudged.
- [AVCaptureCameraLensSmudgeDetectionStatus.unknown](avcapturecameralenssmudgedetectionstatus/unknown.md)
  Indicates that the detection result has not settled, commonly caused by excessive camera movement or the content of the scene.
### Initializers
- [init?(rawValue: Int)](avcapturecameralenssmudgedetectionstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isCameraLensSmudgeDetectionEnabled: Bool](avcapturedevice/iscameralenssmudgedetectionenabled.md)
  Whether camera lens smudge detection is enabled.
- [func setCameraLensSmudgeDetectionEnabled(Bool, detectionInterval: CMTime)](avcapturedevice/setcameralenssmudgedetectionenabled(_:detectioninterval:).md)
  Specify whether to enable camera lens smudge detection, and the interval time between each run of detections.
- [var cameraLensSmudgeDetectionInterval: CMTime](avcapturedevice/cameralenssmudgedetectioninterval.md)
  The camera lens smudge detection interval.
- [var cameraLensSmudgeDetectionStatus: AVCaptureCameraLensSmudgeDetectionStatus](avcapturedevice/cameralenssmudgedetectionstatus.md)
  A value specifying the status of camera lens smudge detection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturecameralenssmudgedetectionstatus)*