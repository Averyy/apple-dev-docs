# unsupportedForPresetOnPlatform

**Framework**: AVFoundation  
**Kind**: property

Indicates that resumption isn’t supported for this preset and platform combination.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static let unsupportedForPresetOnPlatform: AVAssetExportSession.ResumptionFailureReason
```

#### Discussion

You can continue the export, but it runs as a non-resumable (default) export.

## See Also

- [static let incompatibleSessionSettings: AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason/incompatiblesessionsettings.md)
  Indicates the export session settings are incompatible with resumable export.
- [static let incompatibleTemporaryDirectoryContents: AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason/incompatibletemporarydirectorycontents.md)
  Indicates that the contents of the specified temporary files directory are inconsistent with the current resuming export.
- [static let temporaryDirectoryDoesNotExist: AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason/temporarydirectorydoesnotexist.md)
  Indicates that the specified temporary files directory doesn’t exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/resumptionfailurereason/unsupportedforpresetonplatform)*