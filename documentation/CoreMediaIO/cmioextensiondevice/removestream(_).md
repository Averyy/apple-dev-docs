# removeStream(_:)

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Instance Method

Removes a stream from the device.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func removeStream(_ stream: CMIOExtensionStream) throws
```

```objc
- (BOOL) removeStream:(CMIOExtensionStream *) stream error:(NSError **) outError;
```

## Parameters

- `stream`: The stream to remove from the device.

## See Also

### Managing Streams
- [var streams: [CMIOExtensionStream]](./streams.md)
  An array of media streams attached to this device.
- [func addStream(CMIOExtensionStream) throws](./addstream%28_%29.md)
  Adds a stream to a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevice/removestream(_:))*