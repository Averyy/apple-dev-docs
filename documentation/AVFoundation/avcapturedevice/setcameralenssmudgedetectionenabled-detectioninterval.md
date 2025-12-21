# setCameraLensSmudgeDetectionEnabled(_:detectionInterval:)

**Framework**: AVFoundation  
**Kind**: method

Specify whether to enable camera lens smudge detection, and the interval time between each run of detections.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
func setCameraLensSmudgeDetectionEnabled(_ cameraLensSmudgeDetectionEnabled: Bool, detectionInterval: CMTime)
```

#### Discussion

Each run of detection processes frames over a short period, and produces one detection result. Use `detectionInterval` to specify the interval time between each run of detections. For example, when [`isCameraLensSmudgeDetectionEnabled`](avcapturedevice/iscameralenssmudgedetectionenabled.md) is set to `true` and `detectionInterval` is set to 1 minute, detection runs once per minute, and updates [`AVCaptureCameraLensSmudgeDetectionStatus`](avcapturecameralenssmudgedetectionstatus.md). If `detectionInterval` is set to `kCMTimeInvalid`, detection runs only once after the session starts. If `detectionInterval` is set to `kCMTimeZero`, detection runs continuously.

[`AVCaptureDevice`](avcapturedevice.md) throws an `NSInvalidArgumentException` if the [`isCameraLensSmudgeDetectionSupported`](avcapturedevice/format/iscameralenssmudgedetectionsupported.md) property on the current active format returns `false`. Enabling detection requires a lengthy reconfiguration of the capture render pipeline, so you should enable detection before calling [`startRunning()`](avcapturesession/startrunning().md) or within [`beginConfiguration()`](avcapturesession/beginconfiguration().md) and [`commitConfiguration()`](avcapturesession/commitconfiguration().md) while running.

## Parameters

- `cameraLensSmudgeDetectionEnabled`: Specify whether camera lens smudge detection should be enabled.
- `detectionInterval`: The detection running interval if detection is enabled.

## See Also

- [var isCameraLensSmudgeDetectionEnabled: Bool](avcapturedevice/iscameralenssmudgedetectionenabled.md)
  Whether camera lens smudge detection is enabled.
- [var cameraLensSmudgeDetectionInterval: CMTime](avcapturedevice/cameralenssmudgedetectioninterval.md)
  The camera lens smudge detection interval.
- [var cameraLensSmudgeDetectionStatus: AVCaptureCameraLensSmudgeDetectionStatus](avcapturedevice/cameralenssmudgedetectionstatus.md)
  A value specifying the status of camera lens smudge detection.
- [enum AVCaptureCameraLensSmudgeDetectionStatus](avcapturecameralenssmudgedetectionstatus.md)
  Constants indicating the current camera lens smudge detection status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/setcameralenssmudgedetectionenabled(_:detectioninterval:))*