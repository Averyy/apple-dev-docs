# videoComposition

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

The default value is `nil`.

This property is key-value observable.

## See Also

- [var customVideoCompositor: (any AVVideoCompositing)?](avassetexportsession/customvideocompositor.md)
  An optional custom object to use when compositing video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/videocomposition)*