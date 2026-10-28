# interpolatedLocation(at:)

**Framework**: PencilKit  
**Kind**: method  
**Role**: Instance Method

Returns the on-curve point for the floating point parametric value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func interpolatedLocation(at parametricValue: CGFloat) -> CGPoint
```

## Return Value

A [`CGPoint`](../../CoreFoundation/cgpoint.md) interpolated from the supplied `parametricValue`.

## Parameters

- `parametricValue`: The on-curve location `[0, count-1]` where interpolation occurs.

## See Also

### Accessing and interpolating points
- [func interpolatedPoints(in: ClosedRange<CGFloat>?, by: PKStrokePath.InterpolatedSlice.Stride) -> PKStrokePath.InterpolatedSlice](./interpolatedpoints%28in,by%29.md)
  Returns the slice on-curve points using the floating point range and stride that you specify.
- [func interpolatedPoint(at: CGFloat) -> PKStrokePoint](./interpolatedpoint%28at%29.md)
  Returns the on-curve point for the provided floating point parameter.
- [func parametricValue(CGFloat, offsetBy: PKStrokePath.InterpolatedSlice.Stride) -> CGFloat](./parametricvalue%28_,offsetby%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct/interpolatedlocation(at:))*