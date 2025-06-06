# streams

**Framework**: Core Media I/O  
**Kind**: property

An array of media streams attached to this device.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var streams: [CMIOExtensionStream] { get }
```

#### Discussion

This property isn’t key-value observable.

## See Also

- [func addStream(CMIOExtensionStream) throws](cmioextensiondevice/addstream(_:).md)
  Adds a stream to a device.
- [func removeStream(CMIOExtensionStream) throws](cmioextensiondevice/removestream(_:).md)
  Removes a stream from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevice/streams)*