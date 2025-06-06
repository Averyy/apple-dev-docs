# linkedDevices

**Framework**: AVFoundation  
**Kind**: property

An array of capture devices that are physically linked to a device.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var linkedDevices: [AVCaptureDevice] { get }
```

#### Discussion

For an external iSight camera, the array contains an [`AVCaptureDevice`](avcapturedevice.md) instance that represents the external iSight microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/linkeddevices)*