# videoComposition

**Framework**: AVFoundation  
**Kind**: property

The video composition to use for the output.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
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

The value is an [`AVVideoComposition`](avvideocomposition.md) object that specifies the visual arrangement of video frames read from each source track over the timeline of the source asset.

## See Also

- [var customVideoCompositor: (any AVVideoCompositing)?](avassetreadervideocompositionoutput/customvideocompositor.md)
  A custom video compositor for the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/videocomposition)*