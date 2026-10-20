# cameraLensSmudgeDetectionInterval

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) CMTime cameraLensSmudgeDetectionInterval;
```

#### Discussion

[`cameraLensSmudgeDetectionInterval`](./cameralenssmudgedetectioninterval.md) is set by calling [`setCameraLensSmudgeDetectionEnabled(_:detectionInterval:)`](./setcameralenssmudgedetectionenabled%28_,detectioninterval%29.md). By default, this property returns `kCMTimeInvalid`.

## See Also

### Configuring lens smudge detection
- [var isCameraLensSmudgeDetectionEnabled: Bool](./iscameralenssmudgedetectionenabled.md)
  Whether camera lens smudge detection is enabled.
- [func setCameraLensSmudgeDetectionEnabled(Bool, detectionInterval: CMTime)](./setcameralenssmudgedetectionenabled%28_,detectioninterval%29.md)
  Specify whether to enable camera lens smudge detection, and the interval time between each run of detections.
- [var cameraLensSmudgeDetectionStatus: AVCaptureCameraLensSmudgeDetectionStatus](./cameralenssmudgedetectionstatus.md)
  A value specifying the status of camera lens smudge detection.
- [enum AVCaptureCameraLensSmudgeDetectionStatus](../avcapturecameralenssmudgedetectionstatus.md)
  Constants indicating the current camera lens smudge detection status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/cameralenssmudgedetectioninterval)*