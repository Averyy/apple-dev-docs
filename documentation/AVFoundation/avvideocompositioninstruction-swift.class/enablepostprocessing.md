# enablePostProcessing

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) BOOL enablePostProcessing;
```

#### Discussion

A value of [`false`](../../Swift/false.md) indicates that no post processing is required for the whole duration of the video composition instruction. The composition process is more efficient if the value is [`false`](../../Swift/false.md).

The value is [`true`](../../Swift/true.md) by default.

## See Also

### Inspecting the instruction
- [var backgroundColor: CGColor?](./backgroundcolor.md)
  The background color of the composition.
- [var layerInstructions: [AVVideoCompositionLayerInstruction]](./layerinstructions.md)
  Instructions that specify how to layer and compose video frames from source tracks.
- [var timeRange: CMTimeRange](./timerange.md)
  The time range to which the instruction applies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/enablepostprocessing)*