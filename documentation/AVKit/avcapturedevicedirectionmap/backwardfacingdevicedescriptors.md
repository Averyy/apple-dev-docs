# backwardFacingDeviceDescriptors

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

Descriptions of the capture devices that face away from the view.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+

## Declaration

```swift
var backwardFacingDeviceDescriptors: [AVCaptureDeviceDescriptor] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<AVCaptureDeviceDescriptor *> * backwardFacingDeviceDescriptors;
```

## Mentions

- [Choosing a camera by the direction it faces](../choosing-a-camera-by-the-direction-it-faces.md)

#### Discussion

These devices capture the scene behind the view. Each [`AVCaptureDeviceDescriptor`](../avcapturedevicedescriptor.md) in the array identifies one capture device, which may be a virtual device such as a dual camera. Match its [`uniqueID`](../avcapturedevicedescriptor/uniqueid.md) to obtain the corresponding [`AVCaptureDevice`](../../AVFoundation/avcapturedevice.md). The array is empty when no capture device is available or applicable for the current configuration.

## See Also

### Reading the camera directions
- [var forwardFacingDeviceDescriptors: [AVCaptureDeviceDescriptor]](./forwardfacingdevicedescriptors.md)
  Descriptions of the capture devices that face the same direction as the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcapturedevicedirectionmap/backwardfacingdevicedescriptors)*