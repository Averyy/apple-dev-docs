# init(device:)

**Framework**: AVFoundation  
**Kind**: init

Creates a slider to control the video zoom factor of a capture device.

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

You can only create a zoom slider with a device that support’s setting its [`videoZoomFactor`](avcapturedevice/videozoomfactor.md) property value.

## Parameters

- `device`: The capture device to control.

## See Also

- [init(device: AVCaptureDevice, action: (CGFloat) -> Void)](avcapturesystemzoomslider/init(device:action:).md)
  Creates a slider to control the zoom level of the specified capture device with an action to respond to zoom changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesystemzoomslider/init(device:))*