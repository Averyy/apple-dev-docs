# error

**Framework**: AVFoundation  
**Kind**: property

An optional error object.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var error: (any Error)? { get }
```

#### Discussion

The default value of this property is `nil`. The export session sets it to an error object if its status changes to [`AVAssetExportSession.Status.failed`](avassetexportsession/status-swift.enum/failed.md) or [`AVAssetExportSession.Status.cancelled`](avassetexportsession/status-swift.enum/cancelled.md).

## See Also

- [func states(updateInterval: TimeInterval) -> some Sendable & AsyncSequence<AVAssetExportSession.State, Never>
](avassetexportsession/states(updateinterval:).md)
  Monitors the progress state of an export operation.
- [AVAssetExportSession.State](avassetexportsession/state.md)
  Constants that indicate the state of an export operation.
- [var status: AVAssetExportSession.Status](avassetexportsession/status-swift.property.md)
  The status of the export session.
- [AVAssetExportSession.Status](avassetexportsession/status-swift.enum.md)
  Values that indicate the state of an export session.
- [var progress: Float](avassetexportsession/progress.md)
  A value that indicates the progress of the export.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/error)*