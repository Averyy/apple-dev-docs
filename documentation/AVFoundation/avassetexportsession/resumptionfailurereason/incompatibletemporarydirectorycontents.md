# incompatibleTemporaryDirectoryContents

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

Indicates that the contents of the specified temporary files directory are inconsistent with the current resuming export.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static let incompatibleTemporaryDirectoryContents: AVAssetExportSession.ResumptionFailureReason
```

```c
extern AVAssetExportSessionResumptionFailureReason const AVAssetExportSessionResumptionFailureReasonIncompatibleTemporaryDirectoryContents;
```

#### Discussion

You’re likely aliasing two distinct exports together. Use a unique temporary files directory for each export, or clear the directory before resuming.

## See Also

### Failure reasons
- [static let incompatibleSessionSettings: AVAssetExportSession.ResumptionFailureReason](./incompatiblesessionsettings.md)
  Indicates the export session settings are incompatible with resumable export.
- [static let temporaryDirectoryDoesNotExist: AVAssetExportSession.ResumptionFailureReason](./temporarydirectorydoesnotexist.md)
  Indicates that the specified temporary files directory doesn’t exist.
- [static let unsupportedForPresetOnPlatform: AVAssetExportSession.ResumptionFailureReason](./unsupportedforpresetonplatform.md)
  Indicates that resumption isn’t supported for this preset and platform combination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/resumptionfailurereason/incompatibletemporarydirectorycontents)*