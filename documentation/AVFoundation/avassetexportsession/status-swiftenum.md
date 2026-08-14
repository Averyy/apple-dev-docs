# AVAssetExportSession.Status

**Framework**: AVFoundation  
**Kind**: enum

Values that indicate the state of an export session.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum Status
```

## Topics

### Status values
- [AVAssetExportSession.Status.unknown](avassetexportsession/status-swift.enum/unknown.md)
  The session status is unknown.
- [AVAssetExportSession.Status.waiting](avassetexportsession/status-swift.enum/waiting.md)
  The session is waiting to export more data.
- [AVAssetExportSession.Status.exporting](avassetexportsession/status-swift.enum/exporting.md)
  The export is in progress.
- [AVAssetExportSession.Status.completed](avassetexportsession/status-swift.enum/completed.md)
  The export completes successfully.
- [AVAssetExportSession.Status.failed](avassetexportsession/status-swift.enum/failed.md)
  The export fails.
- [AVAssetExportSession.Status.cancelled](avassetexportsession/status-swift.enum/cancelled.md)
  You canceled the export.
### Initializers
- [init?(rawValue: Int)](avassetexportsession/status-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func states(updateInterval: TimeInterval) -> some Sendable & AsyncSequence<AVAssetExportSession.State, Never>
](avassetexportsession/states(updateinterval:).md)
  Monitors the progress state of an export operation.
- [AVAssetExportSession.State](avassetexportsession/state.md)
  Constants that indicate the state of an export operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/status-swift.enum)*