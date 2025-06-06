# AVCaptureDevice.RotationCoordinator

**Framework**: AVFoundation  
**Kind**: class

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

#### Overview

Correctly rotate the photos and movies your app captures, and optionally, a live camera preview, by applying a coordinator’s [`videoRotationAngleForHorizonLevelCapture`](avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelcapture.md) and [`videoRotationAngleForHorizonLevelPreview`](avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelpreview.md) properties, respectively. Each rotation coordinator instance updates its properties so that your app can observe them and immediately apply them to the relevant components.

## Topics

### Creating a rotation coordinator
- [init(device: AVCaptureDevice, previewLayer: CALayer?)](avcapturedevice/rotationcoordinator/init(device:previewlayer:).md)
  Creates a coordinator that provides separate compensation angles for content your app takes with a capture device, and for your app’s camera preview.
### Compensating for a device’s rotation
- [var videoRotationAngleForHorizonLevelCapture: CGFloat](avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelcapture.md)
  An angle the coordinator provides your app to apply to photos or videos it captures with the device so that they’re level relative to gravity.
- [var videoRotationAngleForHorizonLevelPreview: CGFloat](avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelpreview.md)
  An angle the coordinator provides your app to apply to the preview layer so that it’s level relative to gravity.
### Inspecting a coordinator’s configuration
- [var device: AVCaptureDevice?](avcapturedevice/rotationcoordinator/device.md)
  The capture device the coordinator monitors to track its physical rotation.
- [var previewLayer: CALayer?](avcapturedevice/rotationcoordinator/previewlayer.md)
  The layer that displays a camera preview the coordinator calculates a video rotation angle for.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator)*