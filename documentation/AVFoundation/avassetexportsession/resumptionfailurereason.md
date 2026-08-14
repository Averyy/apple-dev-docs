# AVAssetExportSession.ResumptionFailureReason

**Framework**: AVFoundation  
**Kind**: struct

The reason that configuring the export session for resumption failed.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ResumptionFailureReason
```

## Topics

### Creating a failure reason
- [init(String)](avassetexportsession/resumptionfailurereason/init(_:).md)
- [init(rawValue: String)](avassetexportsession/resumptionfailurereason/init(rawvalue:).md)
### Failure reasons
- [static let incompatibleSessionSettings: AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason/incompatiblesessionsettings.md)
  Indicates the export session settings are incompatible with resumable export.
- [static let incompatibleTemporaryDirectoryContents: AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason/incompatibletemporarydirectorycontents.md)
  Indicates that the contents of the specified temporary files directory are inconsistent with the current resuming export.
- [static let temporaryDirectoryDoesNotExist: AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason/temporarydirectorydoesnotexist.md)
  Indicates that the specified temporary files directory doesn’t exist.
- [static let unsupportedForPresetOnPlatform: AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason/unsupportedforpresetonplatform.md)
  Indicates that resumption isn’t supported for this preset and platform combination.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func configureForResumableExport() async -> AVAssetExportSession.ResumptionState](avassetexportsession/configureforresumableexport.md)
  Configures the export session for resumable export.
- [AVAssetExportSession.ResumptionState](avassetexportsession/resumptionstate.md)
  Represents the resumption state of the export session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/resumptionfailurereason)*