# init(device:)

**Framework**: AVFoundation  
**Kind**: init

Creates a slider to control the exposure bias of the specified capture device.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
init(device: AVCaptureDevice)
```

#### Discussion

You can only create an exposure bias slider with a device that support’s setting its [`exposureTargetBias`](avcapturedevice/exposuretargetbias.md) property value.

## Parameters

- `device`: The capture device to control.

## See Also

- [init(device: AVCaptureDevice, action: (Float) -> Void)](avcapturesystemexposurebiasslider/init(device:action:).md)
  Creates a slider to control the exposure bias of the specified capture device with an action to respond to exposure bias changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesystemexposurebiasslider/init(device:))*