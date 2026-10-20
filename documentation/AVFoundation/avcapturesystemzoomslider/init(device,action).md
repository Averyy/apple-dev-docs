# init(device:action:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a slider to control the zoom level of the specified capture device with an action to respond to zoom changes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
init(device: AVCaptureDevice, action: @escaping @MainActor @Sendable (CGFloat) -> Void)
```

```objc
- (instancetype) initWithDevice:(AVCaptureDevice *) device action:(void (^)(double)) action;
```

#### Discussion

The system calls the specified action only when the zoom slider changes the device’s [`videoZoomFactor`](../avcapturedevice/videozoomfactor.md) property value. If your app needs to react to other sources of video zoom factor changes like [`ramp(toVideoZoomFactor:withRate:)`](../avcapturedevice/ramp%28tovideozoomfactor,withrate%29.md), use key-value observation instead.

> ❗ **Important**:  Don’t change the capture device’s video zoom factor when the system calls the action.

## Parameters

- `device`: The capture device to control.
- `action`: An action the system calls on the main actor to respond to changes to the device’s [`videoZoomFactor`](../avcapturedevice/videozoomfactor.md) property.

## See Also

### Creating a zoom slider
- [init(device: AVCaptureDevice)](./init%28device%29.md)
  Creates a slider to control the video zoom factor of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesystemzoomslider/init(device:action:))*