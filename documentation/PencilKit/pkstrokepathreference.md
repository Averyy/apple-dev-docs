# PKStrokePathReference

**Framework**: PencilKit  
**Kind**: class

A class that captures the components of a stroke and provides methods to find and interpolate points along the stroke’s path.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PKStrokePathReference
```

## Topics

### Creating a new stroke path
- [init(controlPoints: [PKStrokePoint], creationDate: Date)](pkstrokepathreference/init(controlpoints:creationdate:).md)
  Creates a stroke path with the cubic B-spline control points and a date that you specify.
### Getting the stroke path properties
- [var count: Int](pkstrokepathreference/count.md)
  The number of control points in this stroke path.
- [var creationDate: Date](pkstrokepathreference/creationdate.md)
  The time at which this stroke path starts.
### Accessing and interpolating points
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
- [subscript(Int) -> PKStrokePoint](pkstrokepathreference/subscript(_:).md)
  Returns the B-spline control point the location index that you provide.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepathreference)*