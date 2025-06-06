# setTransformRamp(fromStart:toEnd:timeRange:)

**Framework**: AVFoundation  
**Kind**: method

Sets a transform ramp to apply during a given time range.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setTransformRamp(fromStart startTransform: CGAffineTransform, toEnd endTransform: CGAffineTransform, timeRange: CMTimeRange)
```

#### Discussion

During a transform ramp, the affine transform is interpolated between the values set at the ramp’s start time and end time. Before the first specified time for which a transform is set, the affine transform is held constant at the value of [`CGAffineTransformIdentity`](https://developer.apple.com/documentation/CoreGraphics/CGAffineTransformIdentity); after the last time for which a transform is set, the affine transform is held constant at that last value.

## Parameters

- `startTransform`: The transform to be applied at the starting time of  .
- `endTransform`: The transform to be applied at the end time of  .
- `timeRange`: The time range over which the value of the transform is interpolated between   and  .

## See Also

- [func setOpacity(Float, at: CMTime)](avmutablevideocompositionlayerinstruction/setopacity(_:at:).md)
  Sets the opacity value at a specific time within the time range of the instruction.
- [func setOpacityRamp(fromStartOpacity: Float, toEndOpacity: Float, timeRange: CMTimeRange)](avmutablevideocompositionlayerinstruction/setopacityramp(fromstartopacity:toendopacity:timerange:).md)
  Sets an opacity ramp to apply during a specified time range.
- [func setTransform(CGAffineTransform, at: CMTime)](avmutablevideocompositionlayerinstruction/settransform(_:at:).md)
  Sets the transform value at a time within the time range of the instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/settransformramp(fromstart:toend:timerange:))*