# timeRange

**Framework**: AVFoundation  
**Kind**: property

The time range to which the instruction applies.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var timeRange: CMTimeRange { get }
```

#### Discussion

If the time range is invalid, the video compositor will ignore it. See also the requirements of the [`timeRange`](avvideocompositioninstruction-swift.class/timerange.md) property in the array of objects implementing the [`AVVideoCompositionInstructionProtocol`](avvideocompositioninstructionprotocol.md) protocol as described in the [`AVVideoComposition`](avvideocomposition.md) class’s [`instructions`](avvideocomposition/instructions.md) property.

## See Also

- [var backgroundColor: CGColor?](avvideocompositioninstruction-swift.class/backgroundcolor.md)
  The background color of the composition.
- [var layerInstructions: [AVVideoCompositionLayerInstruction]](avvideocompositioninstruction-swift.class/layerinstructions.md)
  Instructions that specify how to layer and compose video frames from source tracks.
- [var enablePostProcessing: Bool](avvideocompositioninstruction-swift.class/enablepostprocessing.md)
  A Boolean value that indicates whether the instruction requires post processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/timerange)*