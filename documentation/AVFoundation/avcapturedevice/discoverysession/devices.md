# devices

**Framework**: AVFoundation  
**Kind**: property

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

## Mentions

- [Choosing a Capture Device](choosing-a-capture-device.md)

#### Discussion

Querying this property provides an array devices currently available on the system. The system sorts the device list according to the order you specified when you created the discovery session. If you created the session with a position of [`AVCaptureDevice.Position.unspecified`](avcapturedevice/position-swift.enum/unspecified.md), the system further sorts them by position in the [`AVCaptureDevice.Position`](avcapturedevice/position-swift.enum.md) enumeration.

Key-value observe this property to monitor changes to the device list.

## See Also

- [var supportedMultiCamDeviceSets: [Set<AVCaptureDevice>]](avcapturedevice/discoverysession/supportedmulticamdevicesets.md)
  Sets of capture devices that you can use simultaneously in a multi-camera session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/discoverysession/devices)*