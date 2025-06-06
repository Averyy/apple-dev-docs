# init(device:action:)

**Framework**: AVFoundation  
**Kind**: init

Creates a slider to control the exposure bias of the specified capture device with an action to respond to exposure bias changes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
init(device: AVCaptureDevice, action: @escaping @MainActor (Float) -> Void)
```

#### Discussion

The system only calls the specified action when the exposure bias slider changes the device’s [`videoZoomFactor`](avcapturedevice/videozoomfactor.md) property value. If you need to react to other sources of changes to the exposure target bias, use key-value observation instead.

> ❗ **Important**:  Don’t change the capture device’s exposure target bias when the system calls the action.

 Don’t change the capture device’s exposure target bias when the system calls the action.

## Parameters

- `device`: The capture device to control.
- `action`: An action the system calls on the main actor to handle changes to the device’s   property.

## See Also

- [init(device: AVCaptureDevice)](avcapturesystemexposurebiasslider/init(device:).md)
  Creates a slider to control the exposure bias of the specified capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesystemexposurebiasslider/init(device:action:))*