# streams

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

An array of media streams attached to this device.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var streams: [CMIOExtensionStream] { get }
```

```objc
@property (atomic, copy, readonly) NSArray<CMIOExtensionStream *> * streams;
```

#### Discussion

This property isn’t key-value observable.

## See Also

### Managing Streams
- [func addStream(CMIOExtensionStream) throws](./addstream%28_%29.md)
  Adds a stream to a device.
- [func removeStream(CMIOExtensionStream) throws](./removestream%28_%29.md)
  Removes a stream from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevice/streams)*