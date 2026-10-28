# AVAssetExportSession.ResumptionState

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

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

## Overview

After calling `configureForResumableExport()`, this returned state details whether the export is successfully configured as resumable or not, and provides additional relevant information.

## Topics

### Resumption states
- [AVAssetExportSession.ResumptionState.resumable(isResumingFromPreviousState:)](./resumptionstate/resumable%28isresumingfrompreviousstate%29.md)
  The export session is successfully configured for resumption.
- [case notResumable(failureReason: AVAssetExportSession.ResumptionFailureReason)](./resumptionstate/notresumable%28failurereason%29.md)
  The export session could not be configured for resumption.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring resumable export
- [func configureForResumableExport() async -> AVAssetExportSession.ResumptionState](./configureforresumableexport%28%29.md)
  Configures the export session for resumable export.
- [AVAssetExportSession.ResumptionFailureReason](./resumptionfailurereason.md)
  The reason that configuring the export session for resumption failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/resumptionstate)*