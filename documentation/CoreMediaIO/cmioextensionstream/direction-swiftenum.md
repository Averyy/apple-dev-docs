# CMIOExtensionStream.Direction

**Framework**: Core Media I/O  
**Kind**: enum

Constants that define the data-flow direction of the stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
enum Direction
```

#### Overview

A stream can be a source or sink. A source stream produces samples, and a sink stream consumes samples.

## Topics

### Directions
- [CMIOExtensionStream.Direction.source](cmioextensionstream/direction-swift.enum/source.md)
  A stream that provides sample buffers for capture.
- [CMIOExtensionStream.Direction.sink](cmioextensionstream/direction-swift.enum/sink.md)
  A stream that consumes sample buffers for playback.
### Initializers
- [init?(rawValue: Int)](cmioextensionstream/direction-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var source: (any CMIOExtensionStreamSource)?](cmioextensionstream/source.md)
  The source object for the stream.
- [var direction: CMIOExtensionStream.Direction](cmioextensionstream/direction-swift.property.md)
  The data-flow direction of the stream.
- [var clockType: CMIOExtensionStream.ClockType](cmioextensionstream/clocktype-swift.property.md)
  A clock type for the stream.
- [CMIOExtensionStream.ClockType](cmioextensionstream/clocktype-swift.enum.md)
  Constants that indicate the clock type of a stream.
- [var customClockConfiguration: CMIOExtensionStreamCustomClockConfiguration?](cmioextensionstream/customclockconfiguration.md)
  An optional custom clock configuration for a stream.
- [class CMIOExtensionStreamCustomClockConfiguration](cmioextensionstreamcustomclockconfiguration.md)
  An object that describes the parameters to create a custom clock on the host side.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/direction-swift.enum)*