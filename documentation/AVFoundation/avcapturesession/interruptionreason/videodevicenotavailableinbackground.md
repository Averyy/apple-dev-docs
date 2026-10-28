# AVCaptureSession.InterruptionReason.videoDeviceNotAvailableInBackground

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

An interruption caused by the app being sent to the background while using a camera.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case videoDeviceNotAvailableInBackground
```

```c
AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableInBackground
```

## Discussion

Camera usage is prohibited while in the background. If you attempt to start running a camera while in the background, the capture session sends an [`wasInterruptedNotification`](../wasinterruptednotification.md) with this interruption reason. If you don’t explicitly call the [`stopRunning()`](../stoprunning%28%29.md) method, your [`startRunning()`](../startrunning%28%29.md) request is preserved, and when your app comes back to foreground, you receive [`interruptionEndedNotification`](../interruptionendednotification.md) and your session starts running.

## See Also

### Constants
- [AVCaptureSession.InterruptionReason.audioDeviceInUseByAnotherClient](./audiodeviceinusebyanotherclient.md)
  An interruption caused by the audio hardware temporarily being made unavailable (for example, for a phone call or alarm).
- [AVCaptureSession.InterruptionReason.videoDeviceInUseByAnotherClient](./videodeviceinusebyanotherclient.md)
  An interruption caused by the video device temporarily being made unavailable (for example, when used by another capture session).
- [AVCaptureSession.InterruptionReason.videoDeviceNotAvailableWithMultipleForegroundApps](./videodevicenotavailablewithmultipleforegroundapps.md)
  An interruption caused when your app is running in Slide Over, Split View, or Picture in Picture mode on iPad.
- [AVCaptureSession.InterruptionReason.videoDeviceNotAvailableDueToSystemPressure](./videodevicenotavailableduetosystempressure.md)
  An interruption due to system pressure, such as thermal duress.
- [AVCaptureSession.InterruptionReason.sensitiveContentMitigationActivated](./sensitivecontentmitigationactivated.md)
  An interruption caused by a `SCVideoStreamAnalyzer` when it detects sensitive content on an associated [`AVCaptureDeviceInput`](../../avcapturedeviceinput.md).  To resume your capture session, call your analyzer’s `SCVideoStreamAnalyzer/continueStream` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason/videodevicenotavailableinbackground)*