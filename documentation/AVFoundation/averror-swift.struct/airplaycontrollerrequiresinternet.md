# airPlayControllerRequiresInternet

**Framework**: AVFoundation  
**Kind**: property

The AirPlay controller requires an internet connection to function.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.3+

## Declaration

```swift
static var airPlayControllerRequiresInternet: AVError.Code { get }
```

## See Also

- [AVError.Code](averror-swift.struct/code.md)
  An enumeration that defines the errors that framework operations can generate.
- [static var airPlayReceiverRequiresInternet: AVError.Code](averror-swift.struct/airplayreceiverrequiresinternet.md)
  The AirPlay receiver requires an internet connection to function.
- [static var airPlayReceiverTemporarilyUnavailable: AVError.Code](averror-swift.struct/airplayreceivertemporarilyunavailable.md)
  An AirPlay receiver is temporarily unavailable.
- [static var applicationIsNotAuthorizedToUseDevice: AVError.Code](averror-swift.struct/applicationisnotauthorizedtousedevice.md)
  The user denied this app permission to capture media.
- [static var applicationIsNotAuthorized: AVError.Code](averror-swift.struct/applicationisnotauthorized.md)
  The app isn’t authorized to play media.
- [static var autoWhiteBalanceNotLocked: AVError.Code](averror-swift.struct/autowhitebalancenotlocked.md)
- [static var compositionTrackSegmentsNotContiguous: AVError.Code](averror-swift.struct/compositiontracksegmentsnotcontiguous.md)
  The composition can’t add the source media because it contains gaps.
- [static var contentIsNotAuthorized: AVError.Code](averror-swift.struct/contentisnotauthorized.md)
  The user isn’t authorized to play the media.
- [static var contentIsProtected: AVError.Code](averror-swift.struct/contentisprotected.md)
  The app isn’t authorized to open the media.
- [static var contentIsUnavailable: AVError.Code](averror-swift.struct/contentisunavailable.md)
  The captured content is unavailable.
- [static var contentKeyRequestCancelled: AVError.Code](averror-swift.struct/contentkeyrequestcancelled.md)
  The app canceled a request to retrieve a content key.
- [static var contentNotUpdated: AVError.Code](averror-swift.struct/contentnotupdated.md)
  The system couldn’t update the captured content.
- [static var createContentKeyRequestFailed: AVError.Code](averror-swift.struct/createcontentkeyrequestfailed.md)
  The app couldn’t create a content key request.
- [static var decodeFailed: AVError.Code](averror-swift.struct/decodefailed.md)
  The system failed to decode the media.
- [static var decoderNotFound: AVError.Code](averror-swift.struct/decodernotfound.md)
  The system can’t find a suitable decoder for the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/averror-swift.struct/airplaycontrollerrequiresinternet)*