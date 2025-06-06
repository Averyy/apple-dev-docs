# removeStream(_:)

**Framework**: Core Media I/O  
**Kind**: method

Removes a stream from the device.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func removeStream(_ stream: CMIOExtensionStream) throws
```

## Parameters

- `stream`: The stream to remove from the device.

## See Also

- [var streams: [CMIOExtensionStream]](cmioextensiondevice/streams.md)
  An array of media streams attached to this device.
- [func addStream(CMIOExtensionStream) throws](cmioextensiondevice/addstream(_:).md)
  Adds a stream to a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevice/removestream(_:))*