# videoFrameRateRangeForCinematicVideo

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
var videoFrameRateRangeForCinematicVideo: AVFrameRateRange? { get }
```

#### Discussion

Indicates the minimum / maximum frame rates available when Cinematic Video capture is enabled on the device input.

Devices may support a limited frame rate range when Cinematic Video capture is active. If this device format does not support Cinematic Video capture, this property returns nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videoframeraterangeforcinematicvideo)*