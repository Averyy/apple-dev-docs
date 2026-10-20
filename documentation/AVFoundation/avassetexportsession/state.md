# AVAssetExportSession.State

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the state of an export operation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum State
```

## Topics

### States
- [AVAssetExportSession.State.pending](./state/pending.md)
  An export operation is currently pending.
- [AVAssetExportSession.State.exporting(progress:)](./state/exporting%28progress%29.md)
  An export session is currently exporting media.
- [AVAssetExportSession.State.waiting](./state/waiting.md)
  An export session is currently waiting.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Monitoring export progress
- [func states(updateInterval: TimeInterval) -> some Sendable & AsyncSequence<AVAssetExportSession.State, Never>
](./states%28updateinterval%29.md)
  Monitors the progress state of an export operation.
- [AVAssetExportSession.Status](./status-swift.enum.md)
  Values that indicate the state of an export session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/state)*