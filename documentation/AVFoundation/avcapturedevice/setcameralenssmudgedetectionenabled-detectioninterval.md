# setCameraLensSmudgeDetectionEnabled(_:detectionInterval:)

**Framework**: AVFoundation  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
func setCameraLensSmudgeDetectionEnabled(_ cameraLensSmudgeDetectionEnabled: Bool, detectionInterval: CMTime)
```

#### Discussion

Specify whether to enable camera lens smudge detection, and the interval time between each run of detections.

Each run of detection processes frames over a short period, and produces one detection result. Use `detectionInterval` to specify the interval time between each run of detections. For example, when `cameraLensSmudgeDetectionEnabled` is set to YES and `detectionInterval` is set to 1 minute, detection runs once per minute, and updates `AVCaptureCameraLensSmudgeDetectionStatus`. If `detectionInterval` is set to `kCMTimeInvalid`, detection will only run once after the session starts. If `detectionInterval` is set to `kCMTimeZero`, detection will run continuously.

AVCaptureDevice throws an NSInvalidArgumentException if `cameraLensSmudgeDetectionSupported` property on the current active format returns NO. From disabled (or stopped) to enabling requires a lengthy reconfiguration of the capture render pipeline, so if you intend to enable this feature, you should enable this detection before calling -[AVCaptureSession startRunning] or within -[AVCaptureSession beginConfiguration] and -[AVCaptureSession commitConfiguration] while running.

## Parameters

- `cameraLensSmudgeDetectionEnabled`: Specify whether camera lens smudge detection should be enabled.
- `detectionInterval`: The detection running interval if detection is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/setcameralenssmudgedetectionenabled(_:detectioninterval:))*