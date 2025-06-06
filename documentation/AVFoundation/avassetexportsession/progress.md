# progress

**Framework**: AVFoundation  
**Kind**: property

A value that indicates the progress of the export.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var progress: Float { get }
```

#### Discussion

The value of this property ranges from `0.0` to `1.0.`

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
- [var error: (any Error)?](avassetexportsession/error.md)
  An optional error object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/progress)*