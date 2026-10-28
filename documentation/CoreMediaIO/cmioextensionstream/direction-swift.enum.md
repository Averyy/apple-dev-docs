# CMIOExtensionStream.Direction

**Framework**: Core Media I/O  
**Kind**: enum  
**Role**: Enumeration

Constants that define the data-flow direction of the stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
enum Direction
```

```c
enum CMIOExtensionStreamDirection : NSInteger;
```

## Overview

A stream can be a source or sink. A source stream produces samples, and a sink stream consumes samples.

## Topics

### Directions
- [CMIOExtensionStream.Direction.source](./direction-swift.enum/source.md)
  A stream that provides sample buffers for capture.
- [CMIOExtensionStream.Direction.sink](./direction-swift.enum/sink.md)
  A stream that consumes sample buffers for playback.
### Initializers
- [init?(rawValue: Int)](./direction-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting a Stream
- [var source: (any CMIOExtensionStreamSource)?](./source.md)
  The source object for the stream.
- [var direction: CMIOExtensionStream.Direction](./direction-swift.property.md)
  The data-flow direction of the stream.
- [var clockType: CMIOExtensionStream.ClockType](./clocktype-swift.property.md)
  A clock type for the stream.
- [CMIOExtensionStream.ClockType](./clocktype-swift.enum.md)
  Constants that indicate the clock type of a stream.
- [var customClockConfiguration: CMIOExtensionStreamCustomClockConfiguration?](./customclockconfiguration.md)
  An optional custom clock configuration for a stream.
- [class CMIOExtensionStreamCustomClockConfiguration](../cmioextensionstreamcustomclockconfiguration.md)
  An object that describes the parameters to create a custom clock on the host side.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/direction-swift.enum)*