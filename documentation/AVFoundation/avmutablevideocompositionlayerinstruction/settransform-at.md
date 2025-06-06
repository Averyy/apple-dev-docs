# setTransform(_:at:)

**Framework**: AVFoundation  
**Kind**: method

Sets the transform value at a time within the time range of the instruction.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setTransform(_ transform: CGAffineTransform, at time: CMTime)
```

#### Discussion

Sets a fixed transform to apply from the specified time until the next time at which a transform is set. This is the same as setting a flat ramp for that time range. Before the first specified time for which a transform is set, the affine transform is held constant at the value of [`CGAffineTransformIdentity`](https://developer.apple.com/documentation/CoreGraphics/CGAffineTransformIdentity); after the last time for which a transform is set, the affine transform is held constant at that last value.

## Parameters

- `transform`: The transform to be applied at  .
- `time`: A time value within the time range of the composition instruction.

## See Also

- [func setOpacity(Float, at: CMTime)](avmutablevideocompositionlayerinstruction/setopacity(_:at:).md)
  Sets the opacity value at a specific time within the time range of the instruction.
- [func setOpacityRamp(fromStartOpacity: Float, toEndOpacity: Float, timeRange: CMTimeRange)](avmutablevideocompositionlayerinstruction/setopacityramp(fromstartopacity:toendopacity:timerange:).md)
  Sets an opacity ramp to apply during a specified time range.
- [func setTransformRamp(fromStart: CGAffineTransform, toEnd: CGAffineTransform, timeRange: CMTimeRange)](avmutablevideocompositionlayerinstruction/settransformramp(fromstart:toend:timerange:).md)
  Sets a transform ramp to apply during a given time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/settransform(_:at:))*