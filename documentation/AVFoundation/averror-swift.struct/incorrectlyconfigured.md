# incorrectlyConfigured

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The system is incorrectly configured for the requested operation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var incorrectlyConfigured: AVError.Code { get }
```

#### Discussion

The system raises this error when you attempt to perform an incorrectly configured operation. For example, HTTP Live Streaming presents only a single video and audio track at a time. If you’re using [`AVAssetWriter`](../avassetwriter.md) to generate a fragmented MPEG-4 asset for streaming, adding more that one video and audio [`AVAssetWriterInput`](../avassetwriterinput.md) to the asset writer generates an error when you start writing.

## See Also

### Error codes
- [AVError.Code](./code.md)
  An enumeration that defines the errors that framework operations can generate.
- [static var airPlayControllerRequiresInternet: AVError.Code](./airplaycontrollerrequiresinternet.md)
  The AirPlay controller requires an internet connection to function.
- [static var airPlayReceiverRequiresInternet: AVError.Code](./airplayreceiverrequiresinternet.md)
  The AirPlay receiver requires an internet connection to function.
- [static var airPlayReceiverTemporarilyUnavailable: AVError.Code](./airplayreceivertemporarilyunavailable.md)
  An AirPlay receiver is temporarily unavailable.
- [static var applicationIsNotAuthorizedToUseDevice: AVError.Code](./applicationisnotauthorizedtousedevice.md)
  The user denied this app permission to capture media.
- [static var applicationIsNotAuthorized: AVError.Code](./applicationisnotauthorized.md)
  The app isn’t authorized to play media.
- [static var autoWhiteBalanceNotLocked: AVError.Code](./autowhitebalancenotlocked.md)
- [static var compositionTrackSegmentsNotContiguous: AVError.Code](./compositiontracksegmentsnotcontiguous.md)
  The composition can’t add the source media because it contains gaps.
- [static var contentIsNotAuthorized: AVError.Code](./contentisnotauthorized.md)
  The user isn’t authorized to play the media.
- [static var contentIsProtected: AVError.Code](./contentisprotected.md)
  The app isn’t authorized to open the media.
- [static var contentIsUnavailable: AVError.Code](./contentisunavailable.md)
  The captured content is unavailable.
- [static var contentKeyRequestCancelled: AVError.Code](./contentkeyrequestcancelled.md)
  The app canceled a request to retrieve a content key.
- [static var contentNotUpdated: AVError.Code](./contentnotupdated.md)
  The system couldn’t update the captured content.
- [static var createContentKeyRequestFailed: AVError.Code](./createcontentkeyrequestfailed.md)
  The app couldn’t create a content key request.
- [static var decodeFailed: AVError.Code](./decodefailed.md)
  The system failed to decode the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/averror-swift.struct/incorrectlyconfigured)*