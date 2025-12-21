# AVCaptureSession.InterruptionReason.videoDeviceNotAvailableDueToSystemPressure

**Framework**: AVFoundation  
**Kind**: case

An interruption due to system pressure, such as thermal duress.

**Availability**:
- iOS 11.1+
- iPadOS 11.1+
- Mac Catalyst 14.0+
- tvOS 11.1+
- visionOS 1.0+

## Declaration

```swift
case videoDeviceNotAvailableDueToSystemPressure
```

## See Also

- [AVCaptureSession.InterruptionReason.videoDeviceNotAvailableInBackground](avcapturesession/interruptionreason/videodevicenotavailableinbackground.md)
  An interruption caused by the app being sent to the background while using a camera.
- [AVCaptureSession.InterruptionReason.audioDeviceInUseByAnotherClient](avcapturesession/interruptionreason/audiodeviceinusebyanotherclient.md)
  An interruption caused by the audio hardware temporarily being made unavailable (for example, for a phone call or alarm).
- [AVCaptureSession.InterruptionReason.videoDeviceInUseByAnotherClient](avcapturesession/interruptionreason/videodeviceinusebyanotherclient.md)
  An interruption caused by the video device temporarily being made unavailable (for example, when used by another capture session).
- [AVCaptureSession.InterruptionReason.videoDeviceNotAvailableWithMultipleForegroundApps](avcapturesession/interruptionreason/videodevicenotavailablewithmultipleforegroundapps.md)
  An interruption caused when your app is running in Slide Over, Split View, or Picture in Picture mode on iPad.
- [AVCaptureSession.InterruptionReason.sensitiveContentMitigationActivated](avcapturesession/interruptionreason/sensitivecontentmitigationactivated.md)
  An interruption caused by a `SCVideoStreamAnalyzer` when it detects sensitive content on an associated [`AVCaptureDeviceInput`](avcapturedeviceinput.md).  To resume your capture session, call your analyzer’s `SCVideoStreamAnalyzer/continueStream` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason/videodevicenotavailableduetosystempressure)*