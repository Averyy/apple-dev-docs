# setTransformRamp(fromStart:toEnd:timeRange:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets a transform ramp to apply during a given time range.

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
func setTransformRamp(fromStart startTransform: CGAffineTransform, toEnd endTransform: CGAffineTransform, timeRange: CMTimeRange)
```

```objc
- (void) setTransformRampFromStartTransform:(CGAffineTransform) startTransform toEndTransform:(CGAffineTransform) endTransform timeRange:(CMTimeRange) timeRange;
```

#### Discussion

During a transform ramp, the affine transform is interpolated between the values set at the ramp’s start time and end time. Before the first specified time for which a transform is set, the affine transform is held constant at the value of [`CGAffineTransformIdentity`](../../CoreGraphics/cgaffinetransformidentity.md); after the last time for which a transform is set, the affine transform is held constant at that last value.

## Parameters

- `startTransform`: The transform to be applied at the starting time of `timeRange`.
- `endTransform`: The transform to be applied at the end time of `timeRange`.
- `timeRange`: The time range over which the value of the transform is interpolated between `startTransform` and `endTransform`.

## See Also

### Managing properties
- [func setOpacity(Float, at: CMTime)](./setopacity%28_,at%29.md)
  Sets the opacity value at a specific time within the time range of the instruction.
- [func setOpacityRamp(fromStartOpacity: Float, toEndOpacity: Float, timeRange: CMTimeRange)](./setopacityramp%28fromstartopacity,toendopacity,timerange%29.md)
  Sets an opacity ramp to apply during a specified time range.
- [func setTransform(CGAffineTransform, at: CMTime)](./settransform%28_,at%29.md)
  Sets the transform value at a time within the time range of the instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/settransformramp(fromstart:toend:timerange:))*