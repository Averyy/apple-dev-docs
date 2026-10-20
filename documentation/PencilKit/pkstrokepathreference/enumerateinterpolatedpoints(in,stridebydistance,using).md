# enumerateInterpolatedPoints(in:strideByDistance:using:)

**Framework**: PencilKit  
**Kind**: method  
**Role**: Instance Method

Executes a given block using each point in a range with a distance step.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use `PKStrokePath.interpolatedPoints(in:by:)`

## Declaration

```swift
func enumerateInterpolatedPoints(in range: __PKFloatRange, strideByDistance distanceStep: CGFloat, using block: @escaping (PKStrokePoint, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateInterpolatedPointsInRange:(PKFloatRange *) range strideByDistance:(CGFloat) distanceStep usingBlock:(void (^)(PKStrokePoint *point, BOOL *stop)) block;
```

## Parameters

- `range`: The parametric range to enumerate points in.
- `distanceStep`: The distance to step between points.
- `block`: The block to execute for each point. This block takes two parameters:

  - `point` —The interpolated point on the spline.
  - `stop` —A reference to a Boolean value. Setting the value to `YES` within the block stops further enumeration, but the that block continues to run until it’s finished.

## See Also

### Accessing and interpolating points
- [func enumerateInterpolatedPoints(in: __PKFloatRange, strideByParametricStep: CGFloat, using: (PKStrokePoint, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateinterpolatedpoints%28in,stridebyparametricstep,using%29.md)
  Executes a given block using each point in a range with a parametric step.
- [func enumerateInterpolatedPoints(in: __PKFloatRange, strideByTime: TimeInterval, using: (PKStrokePoint, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateinterpolatedpoints%28in,stridebytime,using%29.md)
  Executes a given block using each point in a range with a time step.
- [func interpolatedLocation(at: CGFloat) -> CGPoint](./interpolatedlocation%28at%29.md)
  Returns the on-curve point for the floating point parametric value.
- [func interpolatedPoint(at: CGFloat) -> PKStrokePoint](./interpolatedpoint%28at%29.md)
  Returns the on-curve point for the provided floating point parameter.
- [func parametricValue(CGFloat, offsetByDistance: CGFloat) -> CGFloat](./parametricvalue%28_,offsetbydistance%29.md)
  Returns a parametric value on the B-spline that’s a specified distance from the given parametric value.
- [func parametricValue(CGFloat, offsetByTime: TimeInterval) -> CGFloat](./parametricvalue%28_,offsetbytime%29.md)
  Returns a parametric value on the B-spline that’s a specified time from the given parametric value.
- [func point(at: Int) -> PKStrokePoint](./point%28at%29.md)
  Returns the B-spline control point at an index point that you provide.
- [subscript(Int) -> PKStrokePoint](./subscript%28_%29.md)
  Returns the B-spline control point the location index that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepathreference/enumerateinterpolatedpoints(in:stridebydistance:using:))*