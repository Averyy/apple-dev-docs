# setOpacityRamp(fromStartOpacity:toEndOpacity:timeRange:)

**Framework**: AVFoundation  
**Kind**: method

Sets an opacity ramp to apply during a specified time range.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setOpacityRamp(fromStartOpacity startOpacity: Float, toEndOpacity endOpacity: Float, timeRange: CMTimeRange)
```

#### Discussion

During an opacity ramp, opacity is computed using a linear interpolation. Before the first time for which an opacity is set, the opacity is held constant at `1.0`; after the last specified time, the opacity is held constant at the last value.

## Parameters

- `startOpacity`: The opacity to be applied at the start time of  . The value must be between   and  .
- `endOpacity`: The opacity to be applied at the end time of  . The value must be between   and  .
- `timeRange`: The time range over which the value of the opacity is interpolated between   and  .

## See Also

- [func setOpacity(Float, at: CMTime)](avmutablevideocompositionlayerinstruction/setopacity(_:at:).md)
  Sets the opacity value at a specific time within the time range of the instruction.
- [func setTransform(CGAffineTransform, at: CMTime)](avmutablevideocompositionlayerinstruction/settransform(_:at:).md)
  Sets the transform value at a time within the time range of the instruction.
- [func setTransformRamp(fromStart: CGAffineTransform, toEnd: CGAffineTransform, timeRange: CMTimeRange)](avmutablevideocompositionlayerinstruction/settransformramp(fromstart:toend:timerange:).md)
  Sets a transform ramp to apply during a given time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/setopacityramp(fromstartopacity:toendopacity:timerange:))*