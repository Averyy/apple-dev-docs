# temporaryDirectoryDoesNotExist

**Framework**: AVFoundation  
**Kind**: property

Indicates that the specified temporary files directory doesn’t exist.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static let temporaryDirectoryDoesNotExist: AVAssetExportSession.ResumptionFailureReason
```

#### Discussion

Create the temporary files directory and call [`configureForResumableExportWithCompletionHandler:`](avassetexportsession/configureforresumableexportwithcompletionhandler:.md) again.

## See Also

- [static let incompatibleSessionSettings: AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason/incompatiblesessionsettings.md)
  Indicates the export session settings are incompatible with resumable export.
- [static let incompatibleTemporaryDirectoryContents: AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason/incompatibletemporarydirectorycontents.md)
  Indicates that the contents of the specified temporary files directory are inconsistent with the current resuming export.
- [static let unsupportedForPresetOnPlatform: AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason/unsupportedforpresetonplatform.md)
  Indicates that resumption isn’t supported for this preset and platform combination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/resumptionfailurereason/temporarydirectorydoesnotexist)*