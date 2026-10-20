# states(updateInterval:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Monitors the progress state of an export operation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
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

- `updateInterval`: The time interval between updates. The value must be greater than `0`.

## See Also

### Monitoring export progress
- [AVAssetExportSession.State](./state.md)
  Constants that indicate the state of an export operation.
- [AVAssetExportSession.Status](./status-swift.enum.md)
  Values that indicate the state of an export session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/states(updateinterval:))*