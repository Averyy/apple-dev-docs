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
### Initializers
- [convenience init(bezierPath: CGPath, creationDate: Date, pointProvider: (PKConvertedBezierPointReference) -> PKStrokePoint)](pkstrokepathreference/init(bezierpath:creationdate:pointprovider:).md)
  Creates a stroke path recreating the specified Bézier path as a cubic uniform B-Spline.
- [convenience init(controlPoints: [PKStrokePoint], creationDate: Date, strokePathID: UUID)](pkstrokepathreference/init(controlpoints:creationdate:strokepathid:).md)
  Creates a stroke path with the specified control points and a unique identifier.
### Instance Properties
- [var bezierRepresentation: CGPath](pkstrokepathreference/bezierrepresentation.md)
  A Bézier path representation of the path’s curve, computed in linear time.
- [var strokePathID: UUID](pkstrokepathreference/strokepathid.md)
  The unique identity of the stroke path.
### Instance Methods
- [func subpath(with: __PKFloatRange) -> PKStrokePath](pkstrokepathreference/subpath(with:).md)
  Returns a copy of the path containing the control points in the specified parametric range.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepathreference)*