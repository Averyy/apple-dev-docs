# customClockConfiguration

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

An optional custom clock configuration for a stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var customClockConfiguration: CMIOExtensionStreamCustomClockConfiguration? { get }
```

```objc
@property (atomic, strong, readonly, nullable) CMIOExtensionStreamCustomClockConfiguration * customClockConfiguration;
```

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
- [CMIOExtensionStream.ClockType](./clocktype-swift.enum.md)
  Constants that indicate the clock type of a stream.
- [class CMIOExtensionStreamCustomClockConfiguration](../cmioextensionstreamcustomclockconfiguration.md)
  An object that describes the parameters to create a custom clock on the host side.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/customclockconfiguration)*