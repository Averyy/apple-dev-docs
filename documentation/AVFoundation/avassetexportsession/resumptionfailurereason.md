# AVAssetExportSession.ResumptionFailureReason

**Framework**: AVFoundation  
**Kind**: struct

An enum that identifies various reasons why resumable export configuration has failed.

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
- [static let incompatiblePreset: AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason/incompatiblepreset.md)
- [static let incompatibleSessionSettings: AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason/incompatiblesessionsettings.md)
- [static let incompatibleTemporaryDirectoryContents: AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason/incompatibletemporarydirectorycontents.md)
- [static let temporaryDirectoryDoesNotExist: AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason/temporarydirectorydoesnotexist.md)
- [static let unsupportedForPresetOnPlatform: AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason/unsupportedforpresetonplatform.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func configureForResumableExport() async -> AVAssetExportSession.ResumptionState](avassetexportsession/configureforresumableexport.md)
  Configures the export session for resumable export.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/resumptionfailurereason)*