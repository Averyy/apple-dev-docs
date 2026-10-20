# addStream(_:)

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Instance Method

Adds a stream to a device.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func addStream(_ stream: CMIOExtensionStream) throws
```

```objc
- (BOOL) addStream:(CMIOExtensionStream *) stream error:(NSError **) outError;
```

## Parameters

- `stream`: A stream to add to a device.

## See Also

### Managing Streams
- [var streams: [CMIOExtensionStream]](./streams.md)
  An array of media streams attached to this device.
- [func removeStream(CMIOExtensionStream) throws](./removestream%28_%29.md)
  Removes a stream from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevice/addstream(_:))*