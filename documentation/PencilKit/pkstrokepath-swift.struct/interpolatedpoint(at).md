# interpolatedPoint(at:)

**Framework**: PencilKit  
**Kind**: method  
**Role**: Instance Method

Returns the on-curve point for the provided floating point parameter.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func interpolatedPoint(at parametricValue: CGFloat) -> PKStrokePoint
```

#### Return Value

A [`PKStrokePoint`](../pkstrokepoint-swift.struct.md) interpolated from the supplied `parametricValue.`

## Parameters

- `parametricValue`: The on-curve location `[0, count-1]` where interpolation occurs.

## See Also

### Accessing and interpolating points
- [func interpolatedPoints(in: ClosedRange<CGFloat>?, by: PKStrokePath.InterpolatedSlice.Stride) -> PKStrokePath.InterpolatedSlice](./interpolatedpoints%28in,by%29.md)
  Returns the slice on-curve points using the floating point range and stride that you specify.
- [func interpolatedLocation(at: CGFloat) -> CGPoint](./interpolatedlocation%28at%29.md)
  Returns the on-curve point for the floating point parametric value.
- [func parametricValue(CGFloat, offsetBy: PKStrokePath.InterpolatedSlice.Stride) -> CGFloat](./parametricvalue%28_,offsetby%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct/interpolatedpoint(at:))*