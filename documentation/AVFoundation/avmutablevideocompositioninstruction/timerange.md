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
var timeRange: CMTimeRange { get set }
```

#### Discussion

If the time range is invalid, the video compositor ignores it.

## See Also

- [var backgroundColor: CGColor?](avmutablevideocompositioninstruction/backgroundcolor.md)
  The background color of the composition.
- [var layerInstructions: [AVVideoCompositionLayerInstruction]](avmutablevideocompositioninstruction/layerinstructions.md)
  Instructions that specify how to layer and compose video frames from source tracks.
- [var enablePostProcessing: Bool](avmutablevideocompositioninstruction/enablepostprocessing.md)
  A Boolean value that indicates whether the instruction requires post processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositioninstruction/timerange)*