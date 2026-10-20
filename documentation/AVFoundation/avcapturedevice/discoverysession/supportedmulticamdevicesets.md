# supportedMultiCamDeviceSets

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Sets of capture devices that you can use simultaneously in a multi-camera session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 2.1+

## Declaration

```swift
var supportedMultiCamDeviceSets: [Set<AVCaptureDevice>] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSSet<AVCaptureDevice *> *> * supportedMultiCamDeviceSets;
```

#### Discussion

You may use multiple cameras as device inputs to an [`AVCaptureMultiCamSession`](../../avcapturemulticamsession.md), as long as one of the supported multi-camera device sets includes the device.

## See Also

### Finding devices
- [var devices: [AVCaptureDevice]](./devices.md)
  A list of devices that match the search criteria of the discovery session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/discoverysession/supportedmulticamdevicesets)*