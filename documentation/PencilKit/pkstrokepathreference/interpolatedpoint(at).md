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

```objc
- (PKStrokePoint *) interpolatedPointAt:(CGFloat) parametricValue;
```

## Return Value

A [`PKStrokePointReference`](../pkstrokepointreference.md) interpolated from supplied `parametricValue.`

## Parameters

- `parametricValue`: The on-curve location `[0, count-1] `where interpolation occurs.

## See Also

### Accessing and interpolating points
- [func enumerateInterpolatedPoints(in: __PKFloatRange, strideByDistance: CGFloat, using: (PKStrokePoint, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateinterpolatedpoints%28in,stridebydistance,using%29.md)
  Executes a given block using each point in a range with a distance step.
- [func enumerateInterpolatedPoints(in: __PKFloatRange, strideByParametricStep: CGFloat, using: (PKStrokePoint, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateinterpolatedpoints%28in,stridebyparametricstep,using%29.md)
  Executes a given block using each point in a range with a parametric step.
- [func enumerateInterpolatedPoints(in: __PKFloatRange, strideByTime: TimeInterval, using: (PKStrokePoint, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateinterpolatedpoints%28in,stridebytime,using%29.md)
  Executes a given block using each point in a range with a time step.
- [func interpolatedLocation(at: CGFloat) -> CGPoint](./interpolatedlocation%28at%29.md)
  Returns the on-curve point for the floating point parametric value.
- [func parametricValue(CGFloat, offsetByDistance: CGFloat) -> CGFloat](./parametricvalue%28_,offsetbydistance%29.md)
  Returns a parametric value on the B-spline that’s a specified distance from the given parametric value.
- [func parametricValue(CGFloat, offsetByTime: TimeInterval) -> CGFloat](./parametricvalue%28_,offsetbytime%29.md)
  Returns a parametric value on the B-spline that’s a specified time from the given parametric value.
- [func point(at: Int) -> PKStrokePoint](./point%28at%29.md)
  Returns the B-spline control point at an index point that you provide.
- [subscript(Int) -> PKStrokePoint](./subscript%28_%29.md)
  Returns the B-spline control point the location index that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepathreference/interpolatedpoint(at:))*