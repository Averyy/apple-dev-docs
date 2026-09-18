# forwardFacingDeviceDescriptors

**Framework**: AVKit  
**Kind**: property

Descriptions of the capture devices that face the same direction as the view.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
var forwardFacingDeviceDescriptors: [AVCaptureDeviceDescriptor] { get }
```

## Mentions

- [Choosing a camera by the direction it faces](choosing-a-camera-by-the-direction-it-faces.md)

#### Discussion

These devices capture the scene in front of the view. Each [`AVCaptureDeviceDescriptor`](avcapturedevicedescriptor.md) in the array identifies one capture device, which may be a virtual device such as a dual camera. Match its [`uniqueID`](avcapturedevicedescriptor/uniqueid.md) to obtain the corresponding [`AVCaptureDevice`](https://developer.apple.com/documentation/avfoundation/avcapturedevice). The array is empty when no capture device is available or applicable for the current configuration.

## See Also

- [var backwardFacingDeviceDescriptors: [AVCaptureDeviceDescriptor]](avcapturedevicedirectionmap/backwardfacingdevicedescriptors.md)
  Descriptions of the capture devices that face away from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcapturedevicedirectionmap/forwardfacingdevicedescriptors)*