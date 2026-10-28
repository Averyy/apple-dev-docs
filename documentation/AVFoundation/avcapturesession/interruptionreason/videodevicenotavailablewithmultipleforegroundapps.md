# AVCaptureSession.InterruptionReason.videoDeviceNotAvailableWithMultipleForegroundApps

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

An interruption caused when your app is running in Slide Over, Split View, or Picture in Picture mode on iPad.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case videoDeviceNotAvailableWithMultipleForegroundApps
```

```c
AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableWithMultipleForegroundApps
```

## Discussion

If your capture session configuration disallows accessing the camera while multitasking, the system interrupts it with this reason when a user switches to a multitasking mode like Split View. The system doesn’t interrupt your capture session with this reason if [`isMultitaskingCameraAccessEnabled`](../ismultitaskingcameraaccessenabled.md) is [`true`](../../../Swift/true.md).

## See Also

### Constants
- [AVCaptureSession.InterruptionReason.videoDeviceNotAvailableInBackground](./videodevicenotavailableinbackground.md)
  An interruption caused by the app being sent to the background while using a camera.
- [AVCaptureSession.InterruptionReason.audioDeviceInUseByAnotherClient](./audiodeviceinusebyanotherclient.md)
  An interruption caused by the audio hardware temporarily being made unavailable (for example, for a phone call or alarm).
- [AVCaptureSession.InterruptionReason.videoDeviceInUseByAnotherClient](./videodeviceinusebyanotherclient.md)
  An interruption caused by the video device temporarily being made unavailable (for example, when used by another capture session).
- [AVCaptureSession.InterruptionReason.videoDeviceNotAvailableDueToSystemPressure](./videodevicenotavailableduetosystempressure.md)
  An interruption due to system pressure, such as thermal duress.
- [AVCaptureSession.InterruptionReason.sensitiveContentMitigationActivated](./sensitivecontentmitigationactivated.md)
  An interruption caused by a `SCVideoStreamAnalyzer` when it detects sensitive content on an associated [`AVCaptureDeviceInput`](../../avcapturedeviceinput.md).  To resume your capture session, call your analyzer’s `SCVideoStreamAnalyzer/continueStream` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason/videodevicenotavailablewithmultipleforegroundapps)*