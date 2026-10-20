# direction

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

The data-flow direction of the stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var direction: CMIOExtensionStream.Direction { get }
```

```objc
@property (atomic, readonly) CMIOExtensionStreamDirection direction;
```

## See Also

### Inspecting a Stream
- [var source: (any CMIOExtensionStreamSource)?](./source.md)
  The source object for the stream.
- [CMIOExtensionStream.Direction](./direction-swift.enum.md)
  Constants that define the data-flow direction of the stream.
- [var clockType: CMIOExtensionStream.ClockType](./clocktype-swift.property.md)
  A clock type for the stream.
- [CMIOExtensionStream.ClockType](./clocktype-swift.enum.md)
  Constants that indicate the clock type of a stream.
- [var customClockConfiguration: CMIOExtensionStreamCustomClockConfiguration?](./customclockconfiguration.md)
  An optional custom clock configuration for a stream.
- [class CMIOExtensionStreamCustomClockConfiguration](../cmioextensionstreamcustomclockconfiguration.md)
  An object that describes the parameters to create a custom clock on the host side.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/direction-swift.property)*