# customVideoCompositor

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An optional custom object to use when compositing video frames.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var customVideoCompositor: (any AVVideoCompositing)? { get }
```

```objc
@property (nonatomic, readonly, nullable) id<AVVideoCompositing> customVideoCompositor;
```

## See Also

### Configuring video output
- [var videoComposition: AVVideoComposition?](./videocomposition.md)
  An optional object that provides instructions for how to composite frames of video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/customvideocompositor)*