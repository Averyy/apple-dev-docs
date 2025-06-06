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

A [`CGPoint`](https://developer.apple.com/documentation/CoreFoundation/CGPoint) interpolated from supplied `parametricValue`.

## Parameters

- `parametricValue`: The on-curve location   where interpolation occurs.

## See Also

- [func enumerateInterpolatedPoints(in: __PKFloatRange, strideByDistance: CGFloat, using: (PKStrokePoint, UnsafeMutablePointer<ObjCBool>) -> Void)](pkstrokepathreference/enumerateinterpolatedpoints(in:stridebydistance:using:).md)
  Executes a given block using each point in a range with a distance step.
- [func enumerateInterpolatedPoints(in: __PKFloatRange, strideByParametricStep: CGFloat, using: (PKStrokePoint, UnsafeMutablePointer<ObjCBool>) -> Void)](pkstrokepathreference/enumerateinterpolatedpoints(in:stridebyparametricstep:using:).md)
  Executes a given block using each point in a range with a parametric step.
- [func enumerateInterpolatedPoints(in: __PKFloatRange, strideByTime: TimeInterval, using: (PKStrokePoint, UnsafeMutablePointer<ObjCBool>) -> Void)](pkstrokepathreference/enumerateinterpolatedpoints(in:stridebytime:using:).md)
  Executes a given block using each point in a range with a time step.
- [func interpolatedPoint(at: CGFloat) -> PKStrokePoint](pkstrokepathreference/interpolatedpoint(at:).md)
  Returns the on-curve point for the provided floating point parameter.
- [func parametricValue(CGFloat, offsetByDistance: CGFloat) -> CGFloat](pkstrokepathreference/parametricvalue(_:offsetbydistance:).md)
  Returns a parametric value on the B-spline that’s a specified distance from the given parametric value.
- [func parametricValue(CGFloat, offsetByTime: TimeInterval) -> CGFloat](pkstrokepathreference/parametricvalue(_:offsetbytime:).md)
  Returns a parametric value on the B-spline that’s a specified time from the given parametric value.
- [func point(at: Int) -> PKStrokePoint](pkstrokepathreference/point(at:).md)
  Returns the B-spline control point at an index point that you provide.
- [subscript(Int) -> PKStrokePoint](pkstrokepathreference/subscript(_:).md)
  Returns the B-spline control point the location index that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepathreference/interpolatedlocation(at:))*