# SCVideoStreamAnalyzer.StreamDirection

**Framework**: Sensitive Content Analysis  
**Kind**: enum  
**Role**: Enumeration

Options for the different types of analyzed video streams.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum StreamDirection
```

```c
enum SCVideoStreamAnalyzerStreamDirection : NSInteger;
```

## Overview

Pass this enum into the [`init(participantUUID:streamDirection:)`](./init%28participantuuid,streamdirection%29.md) initializer when creating an [`SCVideoStreamAnalyzer`](../scvideostreamanalyzer.md) to analyze video streams.

## Topics

### Identifying a stream direction
- [SCVideoStreamAnalyzer.StreamDirection.incoming](./streamdirection/incoming.md)
  An option that refers to a video stream from another device.
- [SCVideoStreamAnalyzer.StreamDirection.outgoing](./streamdirection/outgoing.md)
  An option that refers to a video stream sent to another device.
### Initializing a stream direction
- [init?(rawValue: Int)](./streamdirection/init%28rawvalue%29.md)
  Initializes a stream direction with the given raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a video stream analyzer
- [init(participantUUID: String, streamDirection: SCVideoStreamAnalyzer.StreamDirection) throws](./init%28participantuuid,streamdirection%29.md)
  Creates a video stream analyzer for the given call participant and stream option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer/streamdirection)*