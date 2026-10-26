# AVError.Code.deviceIsNotAvailableInBackground

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

You attempted to start a capture session in the background, which isn’t allowed in iOS.

**Availability**:
- iOS 4.3+ - Deprecated in 9.0
- iPadOS 4.3+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 9.0+ - Deprecated in 9.0

> **Deprecated**: AVCaptureSession no longer produces an AVCaptureSessionRuntimeErrorNotification with this error. See AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableInBackground.

## Declaration

```swift
case deviceIsNotAvailableInBackground
```

```c
AVErrorDeviceIsNotAvailableInBackground
```

## See Also

### Error codes
- [AVError.Code.airPlayControllerRequiresInternet](./airplaycontrollerrequiresinternet.md)
  The AirPlay controller requires an internet connection to function.
- [AVError.Code.airPlayReceiverRequiresInternet](./airplayreceiverrequiresinternet.md)
  The AirPlay receiver requires an internet connection to function.
- [AVError.Code.airPlayReceiverTemporarilyUnavailable](./airplayreceivertemporarilyunavailable.md)
  An AirPlay receiver is temporarily unavailable.
- [AVError.Code.applicationIsNotAuthorized](./applicationisnotauthorized.md)
  The app isn’t authorized to play media.
- [AVError.Code.applicationIsNotAuthorizedToUseDevice](./applicationisnotauthorizedtousedevice.md)
  The user denied this app permission to capture media.
- [AVError.Code.autoWhiteBalanceNotLocked](./autowhitebalancenotlocked.md)
- [AVError.Code.compositionTrackSegmentsNotContiguous](./compositiontracksegmentsnotcontiguous.md)
  The composition can’t add the source media because it contains gaps.
- [AVError.Code.contentIsNotAuthorized](./contentisnotauthorized.md)
  The user isn’t authorized to play the media.
- [AVError.Code.contentIsProtected](./contentisprotected.md)
  The app isn’t authorized to open the media.
- [AVError.Code.contentIsUnavailable](./contentisunavailable.md)
  The captured content is unavailable.
- [AVError.Code.contentKeyRequestCancelled](./contentkeyrequestcancelled.md)
  The app canceled a request to retrieve a content key.
- [AVError.Code.contentNotUpdated](./contentnotupdated.md)
  The system couldn’t update the captured content.
- [AVError.Code.createContentKeyRequestFailed](./createcontentkeyrequestfailed.md)
  The app couldn’t create a content key request.
- [AVError.Code.decodeFailed](./decodefailed.md)
  The system failed to decode the media.
- [AVError.Code.decoderNotFound](./decodernotfound.md)
  The system can’t find a suitable decoder for the media.
- [AVErrorContentKeyInvalid](../../averror-c.enum/averrorcontentkeyinvalid.md)
- [AVErrorContentKeyRequestPlaybackDestinationDoesNotSupportDeviceIdentifierRandomization](../../averror-c.enum/averrorcontentkeyrequestplaybackdestinationdoesnotsupportdeviceidentifierrandomization.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/averror-swift.struct/code/deviceisnotavailableinbackground)*