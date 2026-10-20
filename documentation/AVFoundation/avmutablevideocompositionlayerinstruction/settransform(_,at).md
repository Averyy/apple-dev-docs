# setTransform(_:at:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets the transform value at a time within the time range of the instruction.

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
func setTransform(_ transform: CGAffineTransform, at time: CMTime)
```

```objc
- (void) setTransform:(CGAffineTransform) transform atTime:(CMTime) time;
```

#### Discussion

Sets a fixed transform to apply from the specified time until the next time at which a transform is set. This is the same as setting a flat ramp for that time range. Before the first specified time for which a transform is set, the affine transform is held constant at the value of [`CGAffineTransformIdentity`](../../CoreGraphics/cgaffinetransformidentity.md); after the last time for which a transform is set, the affine transform is held constant at that last value.

## Parameters

- `transform`: The transform to be applied at `time`.
- `time`: A time value within the time range of the composition instruction.

## See Also

### Managing properties
- [func setOpacity(Float, at: CMTime)](./setopacity%28_,at%29.md)
  Sets the opacity value at a specific time within the time range of the instruction.
- [func setOpacityRamp(fromStartOpacity: Float, toEndOpacity: Float, timeRange: CMTimeRange)](./setopacityramp%28fromstartopacity,toendopacity,timerange%29.md)
  Sets an opacity ramp to apply during a specified time range.
- [func setTransformRamp(fromStart: CGAffineTransform, toEnd: CGAffineTransform, timeRange: CMTimeRange)](./settransformramp%28fromstart,toend,timerange%29.md)
  Sets a transform ramp to apply during a given time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/settransform(_:at:))*