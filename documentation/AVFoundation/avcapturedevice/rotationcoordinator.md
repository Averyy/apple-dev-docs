# AVCaptureDevice.RotationCoordinator

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

A class that monitors the physical orientation of a capture device and provides adjustment angles to keep images level, relative to gravity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
class RotationCoordinator
```

```objc
@interface AVCaptureDeviceRotationCoordinator : NSObject
```

#### Overview

Correctly rotate the photos and movies your app captures, and optionally, a live camera preview, by applying a coordinator’s [`videoRotationAngleForHorizonLevelCapture`](./rotationcoordinator/videorotationangleforhorizonlevelcapture.md) and [`videoRotationAngleForHorizonLevelPreview`](./rotationcoordinator/videorotationangleforhorizonlevelpreview.md) properties, respectively. Each rotation coordinator instance updates its properties so that your app can observe them and immediately apply them to the relevant components.

## Topics

### Creating a rotation coordinator
- [init(device: AVCaptureDevice, previewLayer: CALayer?)](./rotationcoordinator/init%28device,previewlayer%29.md)
  Creates a coordinator that provides separate compensation angles for content your app takes with a capture device, and for your app’s camera preview.
### Compensating for a device’s rotation
- [var videoRotationAngleForHorizonLevelCapture: CGFloat](./rotationcoordinator/videorotationangleforhorizonlevelcapture.md)
  An angle the coordinator provides your app to apply to photos or videos it captures with the device so that they’re level relative to gravity.
- [var videoRotationAngleForHorizonLevelPreview: CGFloat](./rotationcoordinator/videorotationangleforhorizonlevelpreview.md)
  An angle the coordinator provides your app to apply to the preview layer so that it’s level relative to gravity.
- [func videoRotationAngleRelative(toDeviceOrientation: AVCaptureVideoOrientation) -> CGFloat](./rotationcoordinator/videorotationanglerelative%28todeviceorientation%29.md)
  An angle the coordinator provides your app to apply to photos or videos it takes with the capture device so that they’re upright relative to an orientation your app provides.
### Inspecting a coordinator’s configuration
- [var device: AVCaptureDevice?](./rotationcoordinator/device.md)
  The capture device the coordinator monitors to track its physical rotation.
- [var previewLayer: CALayer?](./rotationcoordinator/previewlayer.md)
  The layer that displays a camera preview the coordinator calculates a video rotation angle for.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator)*