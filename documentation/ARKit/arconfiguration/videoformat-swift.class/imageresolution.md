# imageResolution

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The size, in pixels, of video images captured in the session.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

## Declaration

```swift
var imageResolution: CGSize { get }
```

```objc
@property (nonatomic, readonly) CGSize imageResolution;
```

## Discussion

Video format sizes are relative to the native sensor orientation of the device camera, and as such are always landscape-oriented.

## See Also

### Accessing format information
- [var framesPerSecond: Int](./framespersecond.md)
  The rate at which the session captures video and provides AR frame information.
- [var isRecommendedForHighResolutionFrameCapturing: Bool](./isrecommendedforhighresolutionframecapturing.md)
  Determines whether the framework considers a format suitable for high-resolution frame capture.
- [var isVideoHDRSupported: Bool](./isvideohdrsupported.md)
  Determines whether the format supports high dynamic range (HDR).


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/videoformat-swift.class/imageresolution)*