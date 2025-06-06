# AVCaptureSession.InterruptionReason.videoDeviceNotAvailableInBackground

**Framework**: AVFoundation  
**Kind**: case

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

#### Discussion

Camera usage is prohibited while in the background. If you attempt to start running a camera while in the background, the capture session sends an [`wasInterruptedNotification`](avcapturesession/wasinterruptednotification.md) with this interruption reason. If you don’t explicitly call the [`stopRunning()`](avcapturesession/stoprunning().md) method, your [`startRunning()`](avcapturesession/startrunning().md) request is preserved, and when your app comes back to foreground, you receive [`interruptionEndedNotification`](avcapturesession/interruptionendednotification.md) and your session starts running.

## See Also

- [AVCaptureSession.InterruptionReason.audioDeviceInUseByAnotherClient](avcapturesession/interruptionreason/audiodeviceinusebyanotherclient.md)
  An interruption caused by the audio hardware temporarily being made unavailable (for example, for a phone call or alarm).
- [AVCaptureSession.InterruptionReason.videoDeviceInUseByAnotherClient](avcapturesession/interruptionreason/videodeviceinusebyanotherclient.md)
  An interruption caused by the video device temporarily being made unavailable (for example, when used by another capture session).
- [AVCaptureSession.InterruptionReason.videoDeviceNotAvailableWithMultipleForegroundApps](avcapturesession/interruptionreason/videodevicenotavailablewithmultipleforegroundapps.md)
  An interruption caused when your app is running in Slide Over, Split View, or Picture in Picture mode on iPad.
- [AVCaptureSession.InterruptionReason.videoDeviceNotAvailableDueToSystemPressure](avcapturesession/interruptionreason/videodevicenotavailableduetosystempressure.md)
  An interruption due to system pressure, such as thermal duress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason/videodevicenotavailableinbackground)*