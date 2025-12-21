# enablePostProcessing

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the instruction requires post processing.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var enablePostProcessing: Bool { get }
```

#### Discussion

A value of [`false`](https://developer.apple.com/documentation/Swift/false) indicates that no post processing is required for the whole duration of the video composition instruction. The composition process is more efficient if the value is [`false`](https://developer.apple.com/documentation/Swift/false).

The value is [`true`](https://developer.apple.com/documentation/Swift/true) by default.

## See Also

- [var backgroundColor: CGColor?](avvideocompositioninstruction-swift.class/backgroundcolor.md)
  The background color of the composition.
- [var layerInstructions: [AVVideoCompositionLayerInstruction]](avvideocompositioninstruction-swift.class/layerinstructions.md)
  Instructions that specify how to layer and compose video frames from source tracks.
- [var timeRange: CMTimeRange](avvideocompositioninstruction-swift.class/timerange.md)
  The time range to which the instruction applies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/enablepostprocessing)*