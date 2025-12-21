# SCVideoStreamAnalyzer.StreamDirection

**Framework**: SensitiveContentAnalysis  
**Kind**: enum

Options for the different types of analyzed video streams.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
enum StreamDirection
```

#### Overview

Pass this enum into the [`init(participantUUID:streamDirection:)`](scvideostreamanalyzer/init(participantuuid:streamdirection:).md) initializer when creating an [`SCVideoStreamAnalyzer`](scvideostreamanalyzer.md) to analyze video streams.

## Topics

### Identifying a stream direction
- [SCVideoStreamAnalyzer.StreamDirection.incoming](scvideostreamanalyzer/streamdirection/incoming.md)
  An option that refers to a video stream from another device.
- [SCVideoStreamAnalyzer.StreamDirection.outgoing](scvideostreamanalyzer/streamdirection/outgoing.md)
  An option that refers to a video stream sent to another device.
### Initializing a stream direction
- [init?(rawValue: Int)](scvideostreamanalyzer/streamdirection/init(rawvalue:).md)
  Initializes a stream direction with the given raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(participantUUID: String, streamDirection: SCVideoStreamAnalyzer.StreamDirection) throws](scvideostreamanalyzer/init(participantuuid:streamdirection:).md)
  Creates a video stream analyzer for the given call participant and stream option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer/streamdirection)*