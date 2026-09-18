# uniqueID

**Framework**: AVKit  
**Kind**: property

An identifier that uniquely identifies the device’s camera.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
var uniqueID: String { get }
```

#### Discussion

This value matches the [`uniqueID`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/uniqueid) of the camera it describes. Pass it to [`init(uniqueID:)`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/init(uniqueid:)) on a background actor to get the camera itself.

## See Also

- [var localizedName: String](avcapturedevicedescriptor/localizedname.md)
  A name for the camera that’s suitable for display in your interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcapturedevicedescriptor/uniqueid)*