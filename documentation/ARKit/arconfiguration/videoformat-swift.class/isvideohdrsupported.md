# isVideoHDRSupported

**Framework**: ARKit  
**Kind**: property

Determines whether the format supports high dynamic range (HDR).

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var isVideoHDRSupported: Bool { get }
```

#### Discussion

Call this function before setting [`videoHDRAllowed`](arconfiguration/videohdrallowed.md) to `true` to first check whether a video format supports HDR.

## See Also

- [var framesPerSecond: Int](arconfiguration/videoformat-swift.class/framespersecond.md)
  The rate at which the session captures video and provides AR frame information.
- [var imageResolution: CGSize](arconfiguration/videoformat-swift.class/imageresolution.md)
  The size, in pixels, of video images captured in the session.
- [var isRecommendedForHighResolutionFrameCapturing: Bool](arconfiguration/videoformat-swift.class/isrecommendedforhighresolutionframecapturing.md)
  Determines whether the framework considers a format suitable for high-resolution frame capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/videoformat-swift.class/isvideohdrsupported)*