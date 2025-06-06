# AVAssetExportSession.State.exporting(progress:)

**Framework**: AVFoundation  
**Kind**: case

An export session is currently exporting media.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
case exporting(progress: Progress)
```

## Parameters

- `progress`: A value that indicates the completion percentage of the export operation.

## See Also

- [AVAssetExportSession.State.pending](avassetexportsession/state/pending.md)
  An export operation is currently pending.
- [AVAssetExportSession.State.waiting](avassetexportsession/state/waiting.md)
  An export session is currently waiting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/state/exporting(progress:))*