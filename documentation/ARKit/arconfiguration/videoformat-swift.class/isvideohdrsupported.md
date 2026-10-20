# isVideoHDRSupported

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

Determines whether the format supports high dynamic range (HDR).

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
var isVideoHDRSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isVideoHDRSupported) BOOL videoHDRSupported;
```

#### Discussion

Call this function before setting [`videoHDRAllowed`](../videohdrallowed.md) to `true` to first check whether a video format supports HDR.

## See Also

### Accessing format information
- [var framesPerSecond: Int](./framespersecond.md)
  The rate at which the session captures video and provides AR frame information.
- [var imageResolution: CGSize](./imageresolution.md)
  The size, in pixels, of video images captured in the session.
- [var isRecommendedForHighResolutionFrameCapturing: Bool](./isrecommendedforhighresolutionframecapturing.md)
  Determines whether the framework considers a format suitable for high-resolution frame capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/videoformat-swift.class/isvideohdrsupported)*