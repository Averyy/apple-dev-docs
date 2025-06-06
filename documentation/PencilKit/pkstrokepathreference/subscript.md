# subscript(_:)

**Framework**: PencilKit  
**Kind**: subscript

Returns the B-spline control point the location index that you provide.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
subscript(i: Int) -> PKStrokePoint { get }
```

#### Return Value

The [`PKStrokePointReference`](pkstrokepointreference.md) at control point subscript location i.

## Parameters

- `i`: A control point index.

## See Also

- [func enumerateInterpolatedPoints(in: __PKFloatRange, strideByDistance: CGFloat, using: (PKStrokePoint, UnsafeMutablePointer<ObjCBool>) -> Void)](pkstrokepathreference/enumerateinterpolatedpoints(in:stridebydistance:using:).md)
  Executes a given block using each point in a range with a distance step.
- [func enumerateInterpolatedPoints(in: __PKFloatRange, strideByParametricStep: CGFloat, using: (PKStrokePoint, UnsafeMutablePointer<ObjCBool>) -> Void)](pkstrokepathreference/enumerateinterpolatedpoints(in:stridebyparametricstep:using:).md)
  Executes a given block using each point in a range with a parametric step.
- [func enumerateInterpolatedPoints(in: __PKFloatRange, strideByTime: TimeInterval, using: (PKStrokePoint, UnsafeMutablePointer<ObjCBool>) -> Void)](pkstrokepathreference/enumerateinterpolatedpoints(in:stridebytime:using:).md)
  Executes a given block using each point in a range with a time step.
- [func interpolatedLocation(at: CGFloat) -> CGPoint](pkstrokepathreference/interpolatedlocation(at:).md)
  Returns the on-curve point for the floating point parametric value.
- [func interpolatedPoint(at: CGFloat) -> PKStrokePoint](pkstrokepathreference/interpolatedpoint(at:).md)
  Returns the on-curve point for the provided floating point parameter.
- [func parametricValue(CGFloat, offsetByDistance: CGFloat) -> CGFloat](pkstrokepathreference/parametricvalue(_:offsetbydistance:).md)
  Returns a parametric value on the B-spline that’s a specified distance from the given parametric value.
- [func parametricValue(CGFloat, offsetByTime: TimeInterval) -> CGFloat](pkstrokepathreference/parametricvalue(_:offsetbytime:).md)
  Returns a parametric value on the B-spline that’s a specified time from the given parametric value.
- [func point(at: Int) -> PKStrokePoint](pkstrokepathreference/point(at:).md)
  Returns the B-spline control point at an index point that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepathreference/subscript(_:))*