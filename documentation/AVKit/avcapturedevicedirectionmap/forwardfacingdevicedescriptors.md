# forwardFacingDeviceDescriptors

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

Descriptions of the capture devices that face the same direction as the view.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+

## Declaration

```swift
var forwardFacingDeviceDescriptors: [AVCaptureDeviceDescriptor] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<AVCaptureDeviceDescriptor *> * forwardFacingDeviceDescriptors;
```

## Mentions

- [Choosing a camera by the direction it faces](../choosing-a-camera-by-the-direction-it-faces.md)

## Discussion

These devices capture the scene in front of the view. Each [`AVCaptureDeviceDescriptor`](../avcapturedevicedescriptor.md) in the array identifies one capture device, which may be a virtual device such as a dual camera. Match its [`uniqueID`](../avcapturedevicedescriptor/uniqueid.md) to obtain the corresponding [`AVCaptureDevice`](../../AVFoundation/avcapturedevice.md). The array is empty when no capture device is available or applicable for the current configuration.

## See Also

### Reading the camera directions
- [var backwardFacingDeviceDescriptors: [AVCaptureDeviceDescriptor]](./backwardfacingdevicedescriptors.md)
  Descriptions of the capture devices that face away from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcapturedevicedirectionmap/forwardfacingdevicedescriptors)*