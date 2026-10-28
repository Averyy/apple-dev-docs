# setOpacity(_:at:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets the opacity value at a specific time within the time range of the instruction.

**Availability**:
- iOS 4.0+ - Deprecated in 26.0
- iPadOS 4.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.7+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use AVVideoCompositionLayerInstruction.Configuration instead

## Declaration

```swift
func setOpacity(_ opacity: Float, at time: CMTime)
```

```objc
- (void) setOpacity:(float) opacity atTime:(CMTime) time;
```

## Discussion

Sets a fixed opacity to apply from the specified time until the next time at which an opacity is set; this is the same as setting a flat ramp for that time range. Before the first time for which an opacity is set, the opacity is held constant at `1.0`; after the last specified time, the opacity is held constant at the last value.

## Parameters

- `opacity`: The opacity to be applied at `time`. The value must be between `0.0` and `1.0`.
- `time`: A time value within the time range of the composition instruction.

## See Also

### Managing properties
- [func setOpacityRamp(fromStartOpacity: Float, toEndOpacity: Float, timeRange: CMTimeRange)](./setopacityramp%28fromstartopacity,toendopacity,timerange%29.md)
  Sets an opacity ramp to apply during a specified time range.
- [func setTransform(CGAffineTransform, at: CMTime)](./settransform%28_,at%29.md)
  Sets the transform value at a time within the time range of the instruction.
- [func setTransformRamp(fromStart: CGAffineTransform, toEnd: CGAffineTransform, timeRange: CMTimeRange)](./settransformramp%28fromstart,toend,timerange%29.md)
  Sets a transform ramp to apply during a given time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/setopacity(_:at:))*