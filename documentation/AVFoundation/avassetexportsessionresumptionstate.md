# AVAssetExportSessionResumptionState

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

The current resumption state of the export session.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
@interface AVAssetExportSessionResumptionState : NSObject
```

#### Overview

Configure a resumable export session with [`configureForResumableExportWithCompletionHandler:`](./avassetexportsession/configureforresumableexportwithcompletionhandler_.md).

## Topics

### Inspecting the resumption state
- [resumptionConfigured](./avassetexportsessionresumptionstate/resumptionconfigured.md)
  A Boolean value that indicates whether the export session is configured as resumable.
- [resumingFromPreviousState](./avassetexportsessionresumptionstate/resumingfrompreviousstate.md)
  A Boolean value that indicates whether or not a resuming export is continuing from a previous state.
- [configurationFailureReason](./avassetexportsessionresumptionstate/configurationfailurereason.md)
  The reason that the export session couldn’t be configured as resumable.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Configuring resumable export
- [- configureForResumableExportWithCompletionHandler:](./avassetexportsession/configureforresumableexportwithcompletionhandler_.md)
  Attempts to configure the export session into resumption mode.
- [AVAssetExportSession.ResumptionFailureReason](./avassetexportsession/resumptionfailurereason.md)
  The reason that configuring the export session for resumption failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsessionresumptionstate)*