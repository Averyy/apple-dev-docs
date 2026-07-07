# AVAssetExportSession.ResumptionState.notResumable(failureReason:)

**Framework**: AVFoundation  
**Kind**: case

The export session could not be configured for resumption.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case notResumable(failureReason: AVAssetExportSession.ResumptionFailureReason)
```

## Parameters

- `failureReason`: The reason why resumption was not successfully configured.

## See Also

- [AVAssetExportSession.ResumptionState.resumable(isResumingFromPreviousState:)](avassetexportsession/resumptionstate/resumable(isresumingfrompreviousstate:).md)
  The export session is successfully configured for resumption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/resumptionstate/notresumable(failurereason:))*