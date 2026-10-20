# device

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, weak, readonly, nullable) AVCaptureDevice * device;
```

#### Discussion

The coordinator updates its [`videoRotationAngleForHorizonLevelCapture`](./videorotationangleforhorizonlevelcapture.md) property by monitoring the device’s physical rotation.

## See Also

### Inspecting a coordinator’s configuration
- [var previewLayer: CALayer?](./previewlayer.md)
  The layer that displays a camera preview the coordinator calculates a video rotation angle for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator/device)*