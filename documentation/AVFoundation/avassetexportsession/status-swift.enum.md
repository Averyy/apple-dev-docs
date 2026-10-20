# AVAssetExportSession.Status

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Values that indicate the state of an export session.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum Status
```

```c
enum AVAssetExportSessionStatus : NSInteger;
```

## Topics

### Status values
- [AVAssetExportSession.Status.unknown](./status-swift.enum/unknown.md)
  The session status is unknown.
- [AVAssetExportSession.Status.waiting](./status-swift.enum/waiting.md)
  The session is waiting to export more data.
- [AVAssetExportSession.Status.exporting](./status-swift.enum/exporting.md)
  The export is in progress.
- [AVAssetExportSession.Status.completed](./status-swift.enum/completed.md)
  The export completes successfully.
- [AVAssetExportSession.Status.failed](./status-swift.enum/failed.md)
  The export fails.
- [AVAssetExportSession.Status.cancelled](./status-swift.enum/cancelled.md)
  You canceled the export.
### Initializers
- [init?(rawValue: Int)](./status-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Monitoring export progress
- [func states(updateInterval: TimeInterval) -> some Sendable & AsyncSequence<AVAssetExportSession.State, Never>
](./states%28updateinterval%29.md)
  Monitors the progress state of an export operation.
- [AVAssetExportSession.State](./state.md)
  Constants that indicate the state of an export operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/status-swift.enum)*