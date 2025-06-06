# interpolatedLocation(at:)

**Framework**: PencilKit  
**Kind**: method

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

#### Return Value

A [`CGPoint`](https://developer.apple.com/documentation/CoreFoundation/CGPoint) interpolated from the supplied `parametricValue`.

## Parameters

- `parametricValue`: The on-curve location   where interpolation occurs.

## See Also

- [func interpolatedPoints(in: ClosedRange<CGFloat>?, by: PKStrokePath.InterpolatedSlice.Stride) -> PKStrokePath.InterpolatedSlice](pkstrokepath-swift.struct/interpolatedpoints(in:by:).md)
  Returns the slice on-curve points using the floating point range and stride that you specify.
- [func interpolatedPoint(at: CGFloat) -> PKStrokePoint](pkstrokepath-swift.struct/interpolatedpoint(at:).md)
  Returns the on-curve point for the provided floating point parameter.
- [func parametricValue(CGFloat, offsetBy: PKStrokePath.InterpolatedSlice.Stride) -> CGFloat](pkstrokepath-swift.struct/parametricvalue(_:offsetby:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct/interpolatedlocation(at:))*