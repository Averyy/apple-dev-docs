# CMIOExtensionStream.ClockType

**Framework**: Core Media I/O  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the clock type of a stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
enum ClockType
```

```c
enum CMIOExtensionStreamClockType : NSInteger;
```

## Topics

### Clock Types
- [CMIOExtensionStream.ClockType.hostTime](./clocktype-swift.enum/hosttime.md)
  Indicates that the stream uses the host time clock.
- [CMIOExtensionStream.ClockType.linkedCoreAudioDeviceUID](./clocktype-swift.enum/linkedcoreaudiodeviceuid.md)
  Indicates that the stream uses the clock of the linked Core Audio device.
- [CMIOExtensionStream.ClockType.custom](./clocktype-swift.enum/custom.md)
  Indicates that the stream’s clock is specific to the device hosting the stream.
### Initializers
- [init?(rawValue: Int)](./clocktype-swift.enum/init%28rawvalue%29.md)

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
- [CMIOExtensionStream.Direction](./direction-swift.enum.md)
  Constants that define the data-flow direction of the stream.
- [var clockType: CMIOExtensionStream.ClockType](./clocktype-swift.property.md)
  A clock type for the stream.
- [var customClockConfiguration: CMIOExtensionStreamCustomClockConfiguration?](./customclockconfiguration.md)
  An optional custom clock configuration for a stream.
- [class CMIOExtensionStreamCustomClockConfiguration](../cmioextensionstreamcustomclockconfiguration.md)
  An object that describes the parameters to create a custom clock on the host side.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/clocktype-swift.enum)*