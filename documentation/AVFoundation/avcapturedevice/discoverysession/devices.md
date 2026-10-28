# devices

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A list of devices that match the search criteria of the discovery session.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
var devices: [AVCaptureDevice] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVCaptureDevice *> * devices;
```

## Mentions

- [Choosing a capture device](../../choosing-a-capture-device.md)

## Discussion

Querying this property provides an array devices currently available on the system. The system sorts the device list according to the order you specified when you created the discovery session. If you created the session with a position of [`AVCaptureDevice.Position.unspecified`](../position-swift.enum/unspecified.md), the system further sorts them by position in the [`AVCaptureDevice.Position`](../position-swift.enum.md) enumeration.

Key-value observe this property to monitor changes to the device list.

## See Also

### Finding devices
- [var supportedMultiCamDeviceSets: [Set<AVCaptureDevice>]](./supportedmulticamdevicesets.md)
  Sets of capture devices that you can use simultaneously in a multi-camera session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/discoverysession/devices)*