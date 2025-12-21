# AVCaptureSession.InterruptionReason

**Framework**: AVFoundation  
**Kind**: enum

Constants identifying the reason a capture session was interrupted, found in an [`wasInterruptedNotification`](avcapturesession/wasinterruptednotification.md) user info dictionary.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum InterruptionReason
```

## Topics

### Constants
- [AVCaptureSession.InterruptionReason.videoDeviceNotAvailableInBackground](avcapturesession/interruptionreason/videodevicenotavailableinbackground.md)
  An interruption caused by the app being sent to the background while using a camera.
- [AVCaptureSession.InterruptionReason.audioDeviceInUseByAnotherClient](avcapturesession/interruptionreason/audiodeviceinusebyanotherclient.md)
  An interruption caused by the audio hardware temporarily being made unavailable (for example, for a phone call or alarm).
- [AVCaptureSession.InterruptionReason.videoDeviceInUseByAnotherClient](avcapturesession/interruptionreason/videodeviceinusebyanotherclient.md)
  An interruption caused by the video device temporarily being made unavailable (for example, when used by another capture session).
- [AVCaptureSession.InterruptionReason.videoDeviceNotAvailableWithMultipleForegroundApps](avcapturesession/interruptionreason/videodevicenotavailablewithmultipleforegroundapps.md)
  An interruption caused when your app is running in Slide Over, Split View, or Picture in Picture mode on iPad.
- [AVCaptureSession.InterruptionReason.videoDeviceNotAvailableDueToSystemPressure](avcapturesession/interruptionreason/videodevicenotavailableduetosystempressure.md)
  An interruption due to system pressure, such as thermal duress.
- [AVCaptureSession.InterruptionReason.sensitiveContentMitigationActivated](avcapturesession/interruptionreason/sensitivecontentmitigationactivated.md)
  An interruption caused by a `SCVideoStreamAnalyzer` when it detects sensitive content on an associated [`AVCaptureDeviceInput`](avcapturedeviceinput.md).  To resume your capture session, call your analyzer’s `SCVideoStreamAnalyzer/continueStream` method.
### Initializers
- [init?(rawValue: Int)](avcapturesession/interruptionreason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let AVCaptureSessionInterruptionSystemPressureStateKey: String](avcapturesessioninterruptionsystempressurestatekey.md)
  A key to retrieve a state value that indicates the system pressure level and contributing factors that caused the interruption.
- [let AVCaptureSessionInterruptionReasonKey: String](avcapturesessioninterruptionreasonkey.md)
  Key to retrieve information about a capture interruption from a [`wasInterruptedNotification`](avcapturesession/wasinterruptednotification.md) user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason)*