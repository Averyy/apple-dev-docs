# AVAssetExportSession.ResumptionState.resumable(isResumingFromPreviousState:)

**Framework**: AVFoundation  
**Kind**: case

The export session is successfully configured for resumption.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case resumable(isResumingFromPreviousState: Bool)
```

## Parameters

- `isResumingFromPreviousState`: `true` if the export will continue from a previously interrupted state; `false` if starting/restarting from beginning.

## See Also

- [case notResumable(failureReason: AVAssetExportSession.ResumptionFailureReason)](avassetexportsession/resumptionstate/notresumable(failurereason:).md)
  The export session could not be configured for resumption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/resumptionstate/resumable(isresumingfrompreviousstate:))*