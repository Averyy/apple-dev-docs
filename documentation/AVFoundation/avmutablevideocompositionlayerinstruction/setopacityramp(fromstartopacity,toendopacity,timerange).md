# setOpacityRamp(fromStartOpacity:toEndOpacity:timeRange:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets an opacity ramp to apply during a specified time range.

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
func setOpacityRamp(fromStartOpacity startOpacity: Float, toEndOpacity endOpacity: Float, timeRange: CMTimeRange)
```

```objc
- (void) setOpacityRampFromStartOpacity:(float) startOpacity toEndOpacity:(float) endOpacity timeRange:(CMTimeRange) timeRange;
```

## Discussion

During an opacity ramp, opacity is computed using a linear interpolation. Before the first time for which an opacity is set, the opacity is held constant at `1.0`; after the last specified time, the opacity is held constant at the last value.

## Parameters

- `startOpacity`: The opacity to be applied at the start time of `timeRange`. The value must be between `0.0` and `1.0`.
- `endOpacity`: The opacity to be applied at the end time of `timeRange`. The value must be between `0.0` and `1.0`.
- `timeRange`: The time range over which the value of the opacity is interpolated between `startOpacity` and `endOpacity`.

## See Also

### Managing properties
- [func setOpacity(Float, at: CMTime)](./setopacity%28_,at%29.md)
  Sets the opacity value at a specific time within the time range of the instruction.
- [func setTransform(CGAffineTransform, at: CMTime)](./settransform%28_,at%29.md)
  Sets the transform value at a time within the time range of the instruction.
- [func setTransformRamp(fromStart: CGAffineTransform, toEnd: CGAffineTransform, timeRange: CMTimeRange)](./settransformramp%28fromstart,toend,timerange%29.md)
  Sets a transform ramp to apply during a given time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/setopacityramp(fromstartopacity:toendopacity:timerange:))*