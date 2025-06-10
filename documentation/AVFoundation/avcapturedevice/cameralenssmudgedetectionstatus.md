# cameraLensSmudgeDetectionStatus

**Framework**: AVFoundation  
**Kind**: property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
var cameraLensSmudgeDetectionStatus: AVCaptureCameraLensSmudgeDetectionStatus { get }
```

#### Discussion

A value specifying the status of camera lens smudge detection.

During the initial detection execution, `cameraLensSmudgeDetectionStatus` is `AVCaptureCameraLensSmudgeDetectionStatusUnknown` before detection result is settled. Once a detection result is produced, `cameraLensSmudgeDetectionStatus` is the most recent detection result. This property can be key-value observed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/cameralenssmudgedetectionstatus)*