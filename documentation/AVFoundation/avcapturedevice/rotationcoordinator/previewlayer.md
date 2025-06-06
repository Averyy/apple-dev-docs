# previewLayer

**Framework**: AVFoundation  
**Kind**: property

The layer that displays a camera preview the coordinator calculates a video rotation angle for.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
weak var previewLayer: CALayer? { get }
```

#### Discussion

The coordinator updates its [`videoRotationAngleForHorizonLevelPreview`](avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelpreview.md) property by monitoring the layer and the physical rotation of [`device`](avcapturedevice/rotationcoordinator/device.md).

## See Also

- [var device: AVCaptureDevice?](avcapturedevice/rotationcoordinator/device.md)
  The capture device the coordinator monitors to track its physical rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator/previewlayer)*