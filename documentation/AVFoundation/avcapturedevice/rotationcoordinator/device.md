# device

**Framework**: AVFoundation  
**Kind**: property

The capture device the coordinator monitors to track its physical rotation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
weak var device: AVCaptureDevice? { get }
```

#### Discussion

The coordinator updates its [`videoRotationAngleForHorizonLevelCapture`](avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelcapture.md) property by monitoring the device’s physical rotation.

## See Also

- [var previewLayer: CALayer?](avcapturedevice/rotationcoordinator/previewlayer.md)
  The layer that displays a camera preview the coordinator calculates a video rotation angle for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator/device)*