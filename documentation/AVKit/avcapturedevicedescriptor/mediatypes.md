# mediaTypes

**Framework**: AVKit  
**Kind**: property

The kinds of media the camera captures.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
var mediaTypes: Set<AVMediaType> { get }
```

#### Discussion

The set of [`AVMediaType`](https://developer.apple.com/documentation/avfoundation/avmediatype) values the camera supports, such as video or audio.

## See Also

- [var deviceType: AVCaptureDevice.DeviceType](avcapturedevicedescriptor/devicetype.md)
  The kind of camera, such as a wide-angle or telephoto camera.
- [var position: AVCaptureDevice.Position](avcapturedevicedescriptor/position.md)
  The physical position of the camera on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcapturedevicedescriptor/mediatypes)*