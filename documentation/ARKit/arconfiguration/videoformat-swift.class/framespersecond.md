# framesPerSecond

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The rate at which the session captures video and provides AR frame information.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

## Declaration

```swift
var framesPerSecond: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger framesPerSecond;
```

## See Also

### Accessing format information
- [var imageResolution: CGSize](./imageresolution.md)
  The size, in pixels, of video images captured in the session.
- [var isRecommendedForHighResolutionFrameCapturing: Bool](./isrecommendedforhighresolutionframecapturing.md)
  Determines whether the framework considers a format suitable for high-resolution frame capture.
- [var isVideoHDRSupported: Bool](./isvideohdrsupported.md)
  Determines whether the format supports high dynamic range (HDR).


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/videoformat-swift.class/framespersecond)*