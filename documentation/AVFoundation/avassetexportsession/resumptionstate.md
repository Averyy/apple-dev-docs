# AVAssetExportSession.ResumptionState

**Framework**: AVFoundation  
**Kind**: enum

Represents the resumption state of the export session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum ResumptionState
```

#### Overview

After calling `configureForResumableExport()`, this returned state details whether the export is successfully configured as resumable or not, and provides additional relevant information.

## Topics

### Resumption states
- [AVAssetExportSession.ResumptionState.resumable(isResumingFromPreviousState:)](avassetexportsession/resumptionstate/resumable(isresumingfrompreviousstate:).md)
  The export session is successfully configured for resumption.
- [case notResumable(failureReason: AVAssetExportSession.ResumptionFailureReason)](avassetexportsession/resumptionstate/notresumable(failurereason:).md)
  The export session could not be configured for resumption.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func configureForResumableExport() async -> AVAssetExportSession.ResumptionState](avassetexportsession/configureforresumableexport.md)
  Configures the export session for resumable export.
- [AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason.md)
  An enum that identifies various reasons why resumable export configuration has failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/resumptionstate)*