# subscript(_:)

**Framework**: PencilKit  
**Kind**: subscript  
**Role**: Instance Subscript

Access the stroke point at the provided index.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
subscript(range: ClosedRange<CGFloat>) -> PKStrokePath { get }
```

## See Also

### Accessing and interpolating points
- [func interpolatedPoints(in: ClosedRange<CGFloat>?, by: PKStrokePath.InterpolatedSlice.Stride) -> PKStrokePath.InterpolatedSlice](./interpolatedpoints%28in,by%29.md)
  Returns the slice on-curve points using the floating point range and stride that you specify.
- [func interpolatedLocation(at: CGFloat) -> CGPoint](./interpolatedlocation%28at%29.md)
  Returns the on-curve point for the floating point parametric value.
- [func interpolatedPoint(at: CGFloat) -> PKStrokePoint](./interpolatedpoint%28at%29.md)
  Returns the on-curve point for the provided floating point parameter.
- [func parametricValue(CGFloat, offsetBy: PKStrokePath.InterpolatedSlice.Stride) -> CGFloat](./parametricvalue%28_,offsetby%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct/subscript(_:))*