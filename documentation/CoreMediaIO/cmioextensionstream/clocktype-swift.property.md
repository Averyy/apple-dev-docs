# clockType

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

A clock type for the stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var clockType: CMIOExtensionStream.ClockType { get }
```

```objc
@property (atomic, readonly) CMIOExtensionStreamClockType clockType;
```

#### Discussion

If you created the stream with a custom clock configuration, the value of this property is [`CMIOExtensionStream.ClockType.custom`](./clocktype-swift.enum/custom.md).

## See Also

### Inspecting a Stream
- [var source: (any CMIOExtensionStreamSource)?](./source.md)
  The source object for the stream.
- [var direction: CMIOExtensionStream.Direction](./direction-swift.property.md)
  The data-flow direction of the stream.
- [CMIOExtensionStream.Direction](./direction-swift.enum.md)
  Constants that define the data-flow direction of the stream.
- [CMIOExtensionStream.ClockType](./clocktype-swift.enum.md)
  Constants that indicate the clock type of a stream.
- [var customClockConfiguration: CMIOExtensionStreamCustomClockConfiguration?](./customclockconfiguration.md)
  An optional custom clock configuration for a stream.
- [class CMIOExtensionStreamCustomClockConfiguration](../cmioextensionstreamcustomclockconfiguration.md)
  An object that describes the parameters to create a custom clock on the host side.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/clocktype-swift.property)*