# AVAssetExportSession.ResumptionState

**Framework**: AVFoundation  
**Kind**: enum

Represents the resumption state of the export session.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func configureForResumableExport() async -> AVAssetExportSession.ResumptionState](avassetexportsession/configureforresumableexport.md)
  Configures the export session for resumable export.
- [AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason.md)
  The reason that configuring the export session for resumption failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/resumptionstate)*