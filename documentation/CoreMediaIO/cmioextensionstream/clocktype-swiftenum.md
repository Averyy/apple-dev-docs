# CMIOExtensionStream.ClockType

**Framework**: Core Media I/O  
**Kind**: enum

Constants that indicate the clock type of a stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
enum ClockType
```

## Topics

### Clock Types
- [CMIOExtensionStream.ClockType.hostTime](cmioextensionstream/clocktype-swift.enum/hosttime.md)
  Indicates that the stream uses the host time clock.
- [CMIOExtensionStream.ClockType.linkedCoreAudioDeviceUID](cmioextensionstream/clocktype-swift.enum/linkedcoreaudiodeviceuid.md)
  Indicates that the stream uses the clock of the linked Core Audio device.
- [CMIOExtensionStream.ClockType.custom](cmioextensionstream/clocktype-swift.enum/custom.md)
  Indicates that the stream’s clock is specific to the device hosting the stream.
### Initializers
- [init?(rawValue: Int)](cmioextensionstream/clocktype-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var source: (any CMIOExtensionStreamSource)?](cmioextensionstream/source.md)
  The source object for the stream.
- [var direction: CMIOExtensionStream.Direction](cmioextensionstream/direction-swift.property.md)
  The data-flow direction of the stream.
- [CMIOExtensionStream.Direction](cmioextensionstream/direction-swift.enum.md)
  Constants that define the data-flow direction of the stream.
- [var clockType: CMIOExtensionStream.ClockType](cmioextensionstream/clocktype-swift.property.md)
  A clock type for the stream.
- [var customClockConfiguration: CMIOExtensionStreamCustomClockConfiguration?](cmioextensionstream/customclockconfiguration.md)
  An optional custom clock configuration for a stream.
- [class CMIOExtensionStreamCustomClockConfiguration](cmioextensionstreamcustomclockconfiguration.md)
  An object that describes the parameters to create a custom clock on the host side.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/clocktype-swift.enum)*