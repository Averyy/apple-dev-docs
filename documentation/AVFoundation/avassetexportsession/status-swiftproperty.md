# status

**Framework**: AVFoundation  
**Kind**: property

The status of the export session.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var status: AVAssetExportSession.Status { get }
```

#### Discussion

For possible values, see [`AVAssetExportSession.Status`](avassetexportsession/status-swift.enum.md).

This value is key-value observable.

## See Also

- [func states(updateInterval: TimeInterval) -> some Sendable & AsyncSequence<AVAssetExportSession.State, Never>
](avassetexportsession/states(updateinterval:).md)
  Monitors the progress state of an export operation.
- [AVAssetExportSession.State](avassetexportsession/state.md)
  Constants that indicate the state of an export operation.
- [AVAssetExportSession.Status](avassetexportsession/status-swift.enum.md)
  Values that indicate the state of an export session.
- [var progress: Float](avassetexportsession/progress.md)
  A value that indicates the progress of the export.
- [var error: (any Error)?](avassetexportsession/error.md)
  An optional error object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/status-swift.property)*