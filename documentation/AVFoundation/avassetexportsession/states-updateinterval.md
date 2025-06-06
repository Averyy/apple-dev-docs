# states(updateInterval:)

**Framework**: AVFoundation  
**Kind**: method

Monitors the progress state of an export operation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func states(updateInterval: TimeInterval = .infinity) -> some Sendable & AsyncSequence<AVAssetExportSession.State, Never>
```

#### Return Value

An asynchronous sequence of states.

## Parameters

- `updateInterval`: The time interval between updates. The value must be greater than  .

## See Also

- [AVAssetExportSession.State](avassetexportsession/state.md)
  Constants that indicate the state of an export operation.
- [var status: AVAssetExportSession.Status](avassetexportsession/status-swift.property.md)
  The status of the export session.
- [AVAssetExportSession.Status](avassetexportsession/status-swift.enum.md)
  Values that indicate the state of an export session.
- [var progress: Float](avassetexportsession/progress.md)
  A value that indicates the progress of the export.
- [var error: (any Error)?](avassetexportsession/error.md)
  An optional error object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/states(updateinterval:))*