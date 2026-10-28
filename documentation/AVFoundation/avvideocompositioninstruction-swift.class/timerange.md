# timeRange

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) CMTimeRange timeRange;
```

## Discussion

If the time range is invalid, the video compositor will ignore it. See also the requirements of the [`timeRange`](./timerange.md) property in the array of objects implementing the [`AVVideoCompositionInstructionProtocol`](../avvideocompositioninstructionprotocol.md) protocol as described in the [`AVVideoComposition`](../avvideocomposition.md) class’s [`instructions`](../avvideocomposition/instructions.md) property.

## See Also

### Inspecting the instruction
- [var backgroundColor: CGColor?](./backgroundcolor.md)
  The background color of the composition.
- [var layerInstructions: [AVVideoCompositionLayerInstruction]](./layerinstructions.md)
  Instructions that specify how to layer and compose video frames from source tracks.
- [var enablePostProcessing: Bool](./enablepostprocessing.md)
  A Boolean value that indicates whether the instruction requires post processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/timerange)*