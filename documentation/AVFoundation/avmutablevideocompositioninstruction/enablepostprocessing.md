# enablePostProcessing

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the instruction requires post processing.

**Availability**:
- iOS 4.0+ - Deprecated in 26.0
- iPadOS 4.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.7+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use AVVideoCompositionInstruction.Configuration instead

## Declaration

```swift
var enablePostProcessing: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL enablePostProcessing;
```

## Discussion

If no post processing is required for the whole duration of the video composition instruction, set this property to [`false`](../../Swift/false.md) to make the composition process more efficient.

The value is [`true`](../../Swift/true.md) by default.

## See Also

### Configuring the instructions
- [var backgroundColor: CGColor?](./backgroundcolor.md)
  The background color of the composition.
- [var layerInstructions: [AVVideoCompositionLayerInstruction]](./layerinstructions.md)
  Instructions that specify how to layer and compose video frames from source tracks.
- [var timeRange: CMTimeRange](./timerange.md)
  The time range to which the instruction applies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositioninstruction/enablepostprocessing)*