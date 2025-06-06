# parametricValue(_:offsetBy:)

**Framework**: PencilKit  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func parametricValue(_ parametricValue: CGFloat, offsetBy step: PKStrokePath.InterpolatedSlice.Stride) -> CGFloat
```

## See Also

- [func interpolatedPoints(in: ClosedRange<CGFloat>?, by: PKStrokePath.InterpolatedSlice.Stride) -> PKStrokePath.InterpolatedSlice](pkstrokepath-swift.struct/interpolatedpoints(in:by:).md)
  Returns the slice on-curve points using the floating point range and stride that you specify.
- [func interpolatedLocation(at: CGFloat) -> CGPoint](pkstrokepath-swift.struct/interpolatedlocation(at:).md)
  Returns the on-curve point for the floating point parametric value.
- [func interpolatedPoint(at: CGFloat) -> PKStrokePoint](pkstrokepath-swift.struct/interpolatedpoint(at:).md)
  Returns the on-curve point for the provided floating point parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct/parametricvalue(_:offsetby:))*