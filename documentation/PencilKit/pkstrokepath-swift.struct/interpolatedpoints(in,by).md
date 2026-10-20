# interpolatedPoints(in:by:)

**Framework**: PencilKit  
**Kind**: method  
**Role**: Instance Method

Returns the slice on-curve points using the floating point range and stride that you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func interpolatedPoints(in range: ClosedRange<CGFloat>? = nil, by stride: PKStrokePath.InterpolatedSlice.Stride) -> PKStrokePath.InterpolatedSlice
```

#### Return Value

An interpolated slice whose points are within the specified `range`.

## Parameters

- `range`: The floating point range for the points of interest.
- `stride`: The stride component of the current slice.

## See Also

### Accessing and interpolating points
- [func interpolatedLocation(at: CGFloat) -> CGPoint](./interpolatedlocation%28at%29.md)
  Returns the on-curve point for the floating point parametric value.
- [func interpolatedPoint(at: CGFloat) -> PKStrokePoint](./interpolatedpoint%28at%29.md)
  Returns the on-curve point for the provided floating point parameter.
- [func parametricValue(CGFloat, offsetBy: PKStrokePath.InterpolatedSlice.Stride) -> CGFloat](./parametricvalue%28_,offsetby%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct/interpolatedpoints(in:by:))*