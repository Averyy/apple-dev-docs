# mediaTypes

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The kinds of media the camera captures.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+

## Declaration

```swift
var mediaTypes: Set<AVMediaType> { get }
```

```objc
@property (nonatomic, copy, readonly) NSSet<NSString *> * mediaTypes;
```

## Discussion

The set of [`AVMediaType`](../../AVFoundation/avmediatype.md) values the camera supports, such as video or audio.

## See Also

### Inspecting the device’s characteristics
- [var deviceType: AVCaptureDevice.DeviceType](./devicetype.md)
  The kind of camera, such as a wide-angle or telephoto camera.
- [var position: AVCaptureDevice.Position](./position.md)
  The physical position of the camera on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcapturedevicedescriptor/mediatypes)*