# configureForResumableExport()

**Framework**: AVFoundation  
**Kind**: method

Configures the export session for resumable export.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func configureForResumableExport() async -> AVAssetExportSession.ResumptionState
```

#### Return Value

A `ResumptionState` indicating whether resumption is available and whether the export will resume from a previous state.

#### Discussion

This method validates that the export session’s current configuration supports resumption and checks the temporary directory for any partial results from previous export attempts.

Call this method after configuring all export settings (preset, output file type, etc.) and before calling `exportAsynchronously()`.

> **Note**: Even if resumption is not available, you can still perform a normal (non-resumable) export by calling `exportAsynchronously()`.

Example usage:

```swift
let exportSession = AVAssetExportSession(asset: asset, presetName: .hevc1920x1080)!
exportSession.outputFileType = .mov
exportSession.outputURL = outputURL
exportSession.directoryForTemporaryFiles = temporaryDirectory

let state = await exportSession.configureForResumableExport()
switch state {
case .resumable(let isResuming):
    print("Export is resumable. Continuing from previous state: \(isResuming)")
case .notResumable(let reason):
    print("Cannot perform resumable export with current configuration: \(reason)")
}

try await exportSession.export(to: outputURL, as: .mov)
```

## See Also

- [AVAssetExportSession.ResumptionFailureReason](avassetexportsession/resumptionfailurereason.md)
  An enum that identifies various reasons why resumable export configuration has failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/configureforresumableexport())*