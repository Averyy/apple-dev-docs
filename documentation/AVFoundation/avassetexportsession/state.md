# AVAssetExportSession.State

**Framework**: AVFoundation  
**Kind**: enum

Constants that indicate the state of an export operation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum State
```

## Topics

### States
- [AVAssetExportSession.State.pending](avassetexportsession/state/pending.md)
  An export operation is currently pending.
- [AVAssetExportSession.State.exporting(progress:)](avassetexportsession/state/exporting(progress:).md)
  An export session is currently exporting media.
- [AVAssetExportSession.State.waiting](avassetexportsession/state/waiting.md)
  An export session is currently waiting.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func states(updateInterval: TimeInterval) -> some Sendable & AsyncSequence<AVAssetExportSession.State, Never>
](avassetexportsession/states(updateinterval:).md)
  Monitors the progress state of an export operation.
- [var status: AVAssetExportSession.Status](avassetexportsession/status-swift.property.md)
  The status of the export session.
- [AVAssetExportSession.Status](avassetexportsession/status-swift.enum.md)
  Values that indicate the state of an export session.
- [var progress: Float](avassetexportsession/progress.md)
  A value that indicates the progress of the export.
- [var error: (any Error)?](avassetexportsession/error.md)
  An optional error object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/state)*