# deskViewCamera

**Framework**: AVFoundation  
**Kind**: property

A virtual overhead camera that captures a user’s desk.

**Availability**:
- macOS 13.0+

## Declaration

```swift
static let deskViewCamera: AVCaptureDevice.DeviceType
```

#### Discussion

This device type provides a distortion-corrected cut out from an ultra wide camera that approximates an overhead view of a user’s physical desktop.

You can use this device type with [`AVCaptureMultiCamSession`](avcapturemulticamsession.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/deskviewcamera)*