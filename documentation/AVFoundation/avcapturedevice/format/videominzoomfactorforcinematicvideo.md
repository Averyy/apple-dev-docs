# videoMinZoomFactorForCinematicVideo

**Framework**: AVFoundation  
**Kind**: property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
var videoMinZoomFactorForCinematicVideo: CGFloat { get }
```

#### Discussion

Indicates the minimum zoom factor available for the AVCaptureDevice’s videoZoomFactor property when Cinematic Video capture is enabled on the device input.

Devices support a limited zoom range when Cinematic Video capture is active. If this device format does not support Cinematic Video capture, this property returns 1.0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videominzoomfactorforcinematicvideo)*