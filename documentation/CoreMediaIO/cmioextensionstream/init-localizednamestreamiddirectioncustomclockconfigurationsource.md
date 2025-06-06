# init(localizedName:streamID:direction:customClockConfiguration:source:)

**Framework**: Core Media I/O  
**Kind**: init

Creates a stream that uses a custom clock configuration.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
init(localizedName: String, streamID: UUID, direction: CMIOExtensionStream.Direction, customClockConfiguration: CMIOExtensionStreamCustomClockConfiguration, source: any CMIOExtensionStreamSource)
```

## Parameters

- `localizedName`: A localized name for the stream.
- `streamID`: A universally unique identifier for the stream.
- `direction`: The direction of the source, which indicates if it produces or consumes samples.
- `customClockConfiguration`: A custom clock configuration for the stream to use.
- `source`: The stream source object.

## See Also

- [init(localizedName: String, streamID: UUID, direction: CMIOExtensionStream.Direction, clockType: CMIOExtensionStream.ClockType, source: any CMIOExtensionStreamSource)](cmioextensionstream/init(localizedname:streamid:direction:clocktype:source:).md)
  Creates a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/init(localizedname:streamid:direction:customclockconfiguration:source:))*