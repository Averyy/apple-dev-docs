# AVAssetExportSession.ResumptionFailureReason

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

The reason that configuring the export session for resumption failed.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ResumptionFailureReason
```

```c
typedef NSString * AVAssetExportSessionResumptionFailureReason;
```

## Topics

### Creating a failure reason
- [init(String)](./resumptionfailurereason/init%28_%29.md)
- [init(rawValue: String)](./resumptionfailurereason/init%28rawvalue%29.md)
### Failure reasons
- [static let incompatibleSessionSettings: AVAssetExportSession.ResumptionFailureReason](./resumptionfailurereason/incompatiblesessionsettings.md)
  Indicates the export session settings are incompatible with resumable export.
- [static let incompatibleTemporaryDirectoryContents: AVAssetExportSession.ResumptionFailureReason](./resumptionfailurereason/incompatibletemporarydirectorycontents.md)
  Indicates that the contents of the specified temporary files directory are inconsistent with the current resuming export.
- [static let temporaryDirectoryDoesNotExist: AVAssetExportSession.ResumptionFailureReason](./resumptionfailurereason/temporarydirectorydoesnotexist.md)
  Indicates that the specified temporary files directory doesn’t exist.
- [static let unsupportedForPresetOnPlatform: AVAssetExportSession.ResumptionFailureReason](./resumptionfailurereason/unsupportedforpresetonplatform.md)
  Indicates that resumption isn’t supported for this preset and platform combination.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring resumable export
- [func configureForResumableExport() async -> AVAssetExportSession.ResumptionState](./configureforresumableexport%28%29.md)
  Configures the export session for resumable export.
- [AVAssetExportSession.ResumptionState](./resumptionstate.md)
  Represents the resumption state of the export session.
- [- configureForResumableExportWithCompletionHandler:](./configureforresumableexportwithcompletionhandler_.md)
  Attempts to configure the export session into resumption mode.
- [AVAssetExportSessionResumptionState](../avassetexportsessionresumptionstate.md)
  The current resumption state of the export session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/resumptionfailurereason)*