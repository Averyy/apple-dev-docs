# videoComposition

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An optional object that provides instructions for how to composite frames of video.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var videoComposition: AVVideoComposition? { get set }
```

```objc
@property (nonatomic, copy, nullable) AVVideoComposition * videoComposition;
```

#### Discussion

The default value is `nil`.

This property is key-value observable.

## See Also

### Configuring video output
- [var customVideoCompositor: (any AVVideoCompositing)?](./customvideocompositor.md)
  An optional custom object to use when compositing video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/videocomposition)*