# timeRange

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The time range to which the instruction applies.

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
var timeRange: CMTimeRange { get set }
```

```objc
@property (nonatomic, assign) CMTimeRange timeRange;
```

#### Discussion

If the time range is invalid, the video compositor ignores it.

## See Also

### Configuring the instructions
- [var backgroundColor: CGColor?](./backgroundcolor.md)
  The background color of the composition.
- [var layerInstructions: [AVVideoCompositionLayerInstruction]](./layerinstructions.md)
  Instructions that specify how to layer and compose video frames from source tracks.
- [var enablePostProcessing: Bool](./enablepostprocessing.md)
  A Boolean value that indicates whether the instruction requires post processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositioninstruction/timerange)*