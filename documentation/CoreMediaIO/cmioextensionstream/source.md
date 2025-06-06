# source

**Framework**: Core Media I/O  
**Kind**: property

The source object for the stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
weak var source: (any CMIOExtensionStreamSource)? { get }
```

## See Also

- [var direction: CMIOExtensionStream.Direction](cmioextensionstream/direction-swift.property.md)
  The data-flow direction of the stream.
- [CMIOExtensionStream.Direction](cmioextensionstream/direction-swift.enum.md)
  Constants that define the data-flow direction of the stream.
- [var clockType: CMIOExtensionStream.ClockType](cmioextensionstream/clocktype-swift.property.md)
  A clock type for the stream.
- [CMIOExtensionStream.ClockType](cmioextensionstream/clocktype-swift.enum.md)
  Constants that indicate the clock type of a stream.
- [var customClockConfiguration: CMIOExtensionStreamCustomClockConfiguration?](cmioextensionstream/customclockconfiguration.md)
  An optional custom clock configuration for a stream.
- [class CMIOExtensionStreamCustomClockConfiguration](cmioextensionstreamcustomclockconfiguration.md)
  An object that describes the parameters to create a custom clock on the host side.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/source)*