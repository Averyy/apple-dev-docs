# streamWithLocalizedName:streamID:direction:customClockConfiguration:source:

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Type Method

Returns a new stream that uses a custom clock configuration.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```objc
+ (instancetype) streamWithLocalizedName:(NSString *) localizedName streamID:(NSUUID *) streamID direction:(CMIOExtensionStreamDirection) direction customClockConfiguration:(CMIOExtensionStreamCustomClockConfiguration *) customClockConfiguration source:(id<CMIOExtensionStreamSource>) source;
```

#### Return Value

A new stream object.

## Parameters

- `localizedName`: A localized name for the stream.
- `streamID`: A universally unique identifier for the stream.
- `direction`: The direction of the source, which indicates if it produces or consumes samples.
- `customClockConfiguration`: A custom clock configuration for the stream to use.
- `source`: The stream source object.

## See Also

### Creating a Stream
- [+ streamWithLocalizedName:streamID:direction:clockType:source:](./streamwithlocalizedname_streamid_direction_clocktype_source_.md)
  Returns a new stream.
- [init(localizedName: String, streamID: UUID, direction: CMIOExtensionStream.Direction, clockType: CMIOExtensionStream.ClockType, source: any CMIOExtensionStreamSource)](./init%28localizedname,streamid,direction,clocktype,source%29.md)
  Creates a stream.
- [init(localizedName: String, streamID: UUID, direction: CMIOExtensionStream.Direction, customClockConfiguration: CMIOExtensionStreamCustomClockConfiguration, source: any CMIOExtensionStreamSource)](./init%28localizedname,streamid,direction,customclockconfiguration,source%29.md)
  Creates a stream that uses a custom clock configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/streamwithlocalizedname:streamid:direction:customclockconfiguration:source:)*