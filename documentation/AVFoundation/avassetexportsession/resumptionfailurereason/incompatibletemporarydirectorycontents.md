# incompatibleTemporaryDirectoryContents

**Framework**: AVFoundation  
**Kind**: property

Indicates that the contents of the specified temporary files directory are inconsistent with the current resuming export.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static let incompatibleTemporaryDirectoryContents: AVAssetExportSession.ResumptionFailureReason
```

#### Discussion

You’re likely aliasing two distinct exports together. Use a unique temporary files directory for each export, or clear the directory before resuming.

## See Also

- [static let incompatibleSessionSettings: AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason/incompatiblesessionsettings.md)
  Indicates the export session settings are incompatible with resumable export.
- [static let temporaryDirectoryDoesNotExist: AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason/temporarydirectorydoesnotexist.md)
  Indicates that the specified temporary files directory doesn’t exist.
- [static let unsupportedForPresetOnPlatform: AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason/unsupportedforpresetonplatform.md)
  Indicates that resumption isn’t supported for this preset and platform combination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/resumptionfailurereason/incompatibletemporarydirectorycontents)*