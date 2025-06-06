# backgroundColor

**Framework**: AVFoundation  
**Kind**: property

The background color of the composition.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var backgroundColor: CGColor? { get }
```

#### Discussion

Only solid BGRA colors are supported; patterns and other supported colors are ignored. If the rendered pixel buffer does not have alpha, the alpha value of the background color is ignored.

If the background color is `NULL`, the video compositor uses a default background color of opaque black.

## See Also

- [var layerInstructions: [AVVideoCompositionLayerInstruction]](avvideocompositioninstruction-swift.class/layerinstructions.md)
  Instructions that specify how to layer and compose video frames from source tracks.
- [var timeRange: CMTimeRange](avvideocompositioninstruction-swift.class/timerange.md)
  The time range to which the instruction applies.
- [var enablePostProcessing: Bool](avvideocompositioninstruction-swift.class/enablepostprocessing.md)
  A Boolean value that indicates whether the instruction requires post processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/backgroundcolor)*