# isRecommendedForHighResolutionFrameCapturing

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

Determines whether the framework considers a format suitable for high-resolution frame capture.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
var isRecommendedForHighResolutionFrameCapturing: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isRecommendedForHighResolutionFrameCapturing;
```

## See Also

### Accessing format information
- [var framesPerSecond: Int](./framespersecond.md)
  The rate at which the session captures video and provides AR frame information.
- [var imageResolution: CGSize](./imageresolution.md)
  The size, in pixels, of video images captured in the session.
- [var isVideoHDRSupported: Bool](./isvideohdrsupported.md)
  Determines whether the format supports high dynamic range (HDR).


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/videoformat-swift.class/isrecommendedforhighresolutionframecapturing)*