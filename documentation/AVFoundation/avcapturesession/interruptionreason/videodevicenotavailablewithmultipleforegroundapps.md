# AVCaptureSession.InterruptionReason.videoDeviceNotAvailableWithMultipleForegroundApps

**Framework**: AVFoundation  
**Kind**: case

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

#### Discussion

If your capture session configuration disallows accessing the camera while multitasking, the system interrupts it with this reason when a user switches to a multitasking mode like Split View. The system doesn’t interrupt your capture session with this reason if [`isMultitaskingCameraAccessEnabled`](avcapturesession/ismultitaskingcameraaccessenabled.md) is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [AVCaptureSession.InterruptionReason.videoDeviceNotAvailableInBackground](avcapturesession/interruptionreason/videodevicenotavailableinbackground.md)
  An interruption caused by the app being sent to the background while using a camera.
- [AVCaptureSession.InterruptionReason.audioDeviceInUseByAnotherClient](avcapturesession/interruptionreason/audiodeviceinusebyanotherclient.md)
  An interruption caused by the audio hardware temporarily being made unavailable (for example, for a phone call or alarm).
- [AVCaptureSession.InterruptionReason.videoDeviceInUseByAnotherClient](avcapturesession/interruptionreason/videodeviceinusebyanotherclient.md)
  An interruption caused by the video device temporarily being made unavailable (for example, when used by another capture session).
- [AVCaptureSession.InterruptionReason.videoDeviceNotAvailableDueToSystemPressure](avcapturesession/interruptionreason/videodevicenotavailableduetosystempressure.md)
  An interruption due to system pressure, such as thermal duress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason/videodevicenotavailablewithmultipleforegroundapps)*