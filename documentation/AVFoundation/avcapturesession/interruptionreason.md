# AVCaptureSession.InterruptionReason

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants identifying the reason a capture session was interrupted, found in an [`wasInterruptedNotification`](./wasinterruptednotification.md) user info dictionary.

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

```c
enum AVCaptureSessionInterruptionReason : NSInteger;
```

## Topics

### Constants
- [AVCaptureSession.InterruptionReason.videoDeviceNotAvailableInBackground](./interruptionreason/videodevicenotavailableinbackground.md)
  An interruption caused by the app being sent to the background while using a camera.
- [AVCaptureSession.InterruptionReason.audioDeviceInUseByAnotherClient](./interruptionreason/audiodeviceinusebyanotherclient.md)
  An interruption caused by the audio hardware temporarily being made unavailable (for example, for a phone call or alarm).
- [AVCaptureSession.InterruptionReason.videoDeviceInUseByAnotherClient](./interruptionreason/videodeviceinusebyanotherclient.md)
  An interruption caused by the video device temporarily being made unavailable (for example, when used by another capture session).
- [AVCaptureSession.InterruptionReason.videoDeviceNotAvailableWithMultipleForegroundApps](./interruptionreason/videodevicenotavailablewithmultipleforegroundapps.md)
  An interruption caused when your app is running in Slide Over, Split View, or Picture in Picture mode on iPad.
- [AVCaptureSession.InterruptionReason.videoDeviceNotAvailableDueToSystemPressure](./interruptionreason/videodevicenotavailableduetosystempressure.md)
  An interruption due to system pressure, such as thermal duress.
- [AVCaptureSession.InterruptionReason.sensitiveContentMitigationActivated](./interruptionreason/sensitivecontentmitigationactivated.md)
  An interruption caused by a `SCVideoStreamAnalyzer` when it detects sensitive content on an associated [`AVCaptureDeviceInput`](../avcapturedeviceinput.md).  To resume your capture session, call your analyzer’s `SCVideoStreamAnalyzer/continueStream` method.
### Initializers
- [init?(rawValue: Int)](./interruptionreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### User-infomation keys
- [let AVCaptureSessionInterruptionSystemPressureStateKey: String](../avcapturesessioninterruptionsystempressurestatekey.md)
  A key to retrieve a state value that indicates the system pressure level and contributing factors that caused the interruption.
- [let AVCaptureSessionInterruptionReasonKey: String](../avcapturesessioninterruptionreasonkey.md)
  Key to retrieve information about a capture interruption from a [`wasInterruptedNotification`](./wasinterruptednotification.md) user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason)*