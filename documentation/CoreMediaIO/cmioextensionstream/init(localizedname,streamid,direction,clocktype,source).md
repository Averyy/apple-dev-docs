# init(localizedName:streamID:direction:clockType:source:)

**Framework**: Core Media I/O  
**Kind**: init  
**Role**: Initializer

Creates a stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
init(localizedName: String, streamID: UUID, direction: CMIOExtensionStream.Direction, clockType: CMIOExtensionStream.ClockType, source: any CMIOExtensionStreamSource)
```

```objc
- (instancetype) initWithLocalizedName:(NSString *) localizedName streamID:(NSUUID *) streamID direction:(CMIOExtensionStreamDirection) direction clockType:(CMIOExtensionStreamClockType) clockType source:(id<CMIOExtensionStreamSource>) source;
```

## Parameters

- `localizedName`: A localized name for the stream.
- `streamID`: A universally unique identifier for the stream.
- `direction`: The direction of the source, which indicates if it produces or consumes samples.
- `clockType`: A clock type for the stream.
- `source`: The stream source object.

## See Also

### Creating a Stream
- [init(localizedName: String, streamID: UUID, direction: CMIOExtensionStream.Direction, customClockConfiguration: CMIOExtensionStreamCustomClockConfiguration, source: any CMIOExtensionStreamSource)](./init%28localizedname,streamid,direction,customclockconfiguration,source%29.md)
  Creates a stream that uses a custom clock configuration.
- [+ streamWithLocalizedName:streamID:direction:clockType:source:](./streamwithlocalizedname_streamid_direction_clocktype_source_.md)
  Returns a new stream.
- [+ streamWithLocalizedName:streamID:direction:customClockConfiguration:source:](./streamwithlocalizedname_streamid_direction_customclockconfiguration_source_.md)
  Returns a new stream that uses a custom clock configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/init(localizedname:streamid:direction:clocktype:source:))*