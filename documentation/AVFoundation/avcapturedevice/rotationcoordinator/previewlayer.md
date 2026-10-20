# previewLayer

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, weak, readonly, nullable) CALayer * previewLayer;
```

#### Discussion

The coordinator updates its [`videoRotationAngleForHorizonLevelPreview`](./videorotationangleforhorizonlevelpreview.md) property by monitoring the layer and the physical rotation of [`device`](./device.md).

## See Also

### Inspecting a coordinator’s configuration
- [var device: AVCaptureDevice?](./device.md)
  The capture device the coordinator monitors to track its physical rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator/previewlayer)*