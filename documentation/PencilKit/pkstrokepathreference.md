# PKStrokePathReference

**Framework**: PencilKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface PKStrokePath : NSObject
```

## Topics

### Creating a new stroke path
- [init(controlPoints: [PKStrokePoint], creationDate: Date)](./pkstrokepathreference/init%28controlpoints,creationdate%29.md)
  Creates a stroke path with the cubic B-spline control points and a date that you specify.
### Getting the stroke path properties
- [var count: Int](./pkstrokepathreference/count.md)
  The number of control points in this stroke path.
- [var creationDate: Date](./pkstrokepathreference/creationdate.md)
  The time at which this stroke path starts.
### Accessing and interpolating points
- [func enumerateInterpolatedPoints(in: __PKFloatRange, strideByDistance: CGFloat, using: (PKStrokePoint, UnsafeMutablePointer<ObjCBool>) -> Void)](./pkstrokepathreference/enumerateinterpolatedpoints%28in,stridebydistance,using%29.md)
  Executes a given block using each point in a range with a distance step.
- [func enumerateInterpolatedPoints(in: __PKFloatRange, strideByParametricStep: CGFloat, using: (PKStrokePoint, UnsafeMutablePointer<ObjCBool>) -> Void)](./pkstrokepathreference/enumerateinterpolatedpoints%28in,stridebyparametricstep,using%29.md)
  Executes a given block using each point in a range with a parametric step.
- [func enumerateInterpolatedPoints(in: __PKFloatRange, strideByTime: TimeInterval, using: (PKStrokePoint, UnsafeMutablePointer<ObjCBool>) -> Void)](./pkstrokepathreference/enumerateinterpolatedpoints%28in,stridebytime,using%29.md)
  Executes a given block using each point in a range with a time step.
- [func interpolatedLocation(at: CGFloat) -> CGPoint](./pkstrokepathreference/interpolatedlocation%28at%29.md)
  Returns the on-curve point for the floating point parametric value.
- [func interpolatedPoint(at: CGFloat) -> PKStrokePoint](./pkstrokepathreference/interpolatedpoint%28at%29.md)
  Returns the on-curve point for the provided floating point parameter.
- [func parametricValue(CGFloat, offsetByDistance: CGFloat) -> CGFloat](./pkstrokepathreference/parametricvalue%28_,offsetbydistance%29.md)
  Returns a parametric value on the B-spline that’s a specified distance from the given parametric value.
- [func parametricValue(CGFloat, offsetByTime: TimeInterval) -> CGFloat](./pkstrokepathreference/parametricvalue%28_,offsetbytime%29.md)
  Returns a parametric value on the B-spline that’s a specified time from the given parametric value.
- [func point(at: Int) -> PKStrokePoint](./pkstrokepathreference/point%28at%29.md)
  Returns the B-spline control point at an index point that you provide.
- [subscript(Int) -> PKStrokePoint](./pkstrokepathreference/subscript%28_%29.md)
  Returns the B-spline control point the location index that you provide.
### Initializers
- [convenience init(bezierPath: CGPath, creationDate: Date, pointProvider: (PKConvertedBezierPointReference) -> PKStrokePoint)](./pkstrokepathreference/init%28bezierpath,creationdate,pointprovider%29.md)
  Creates a stroke path recreating the specified Bézier path as a cubic uniform B-Spline.
- [convenience init(controlPoints: [PKStrokePoint], creationDate: Date, strokePathID: UUID)](./pkstrokepathreference/init%28controlpoints,creationdate,strokepathid%29.md)
  Creates a stroke path with the specified control points and a unique identifier.
### Instance Properties
- [var bezierRepresentation: CGPath](./pkstrokepathreference/bezierrepresentation.md)
  A Bézier path representation of the path’s curve, computed in linear time.
- [var strokePathID: UUID](./pkstrokepathreference/strokepathid.md)
  The unique identity of the stroke path.
### Instance Methods
- [func subpath(with: __PKFloatRange) -> PKStrokePath](./pkstrokepathreference/subpath%28with%29.md)
  Returns a copy of the path containing the control points in the specified parametric range.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Canvas
- [Drawing with PencilKit](./drawing-with-pencilkit.md)
  Add expressive, low-latency drawing to your app using PencilKit.
- [Customizing Scribble with Interactions](./customizing-scribble-with-interactions.md)
  Enable writing on a non-text-input view by adding interactions.
- [Inspecting, Modifying, and Constructing PencilKit Drawings](./inspecting-modifying-and-constructing-pencilkit-drawings.md)
  Score users’ ability to match PencilKit drawings generated from text, by accessing the strokes and points inside PencilKit drawings.
- [Importing Bézier path data into PencilKit](./importing-external-drawing-data-into-pencilkit.md)
  Convert existing Bézier-based stroke data into PencilKit drawing strokes.
- [Controlling stroke rendering for animation and editing](./controlling-stroke-rendering-for-animation-and-editing.md)
  Slice, animate, and blend PencilKit strokes in code, while keeping grain texture and wet ink intact.
- [PKCanvasView](./pkcanvasview.md)
  A view that captures Apple Pencil input and displays the rendered results in an iOS app.
- [PKDrawing](./pkdrawingreference.md)
  A data structure that contains the drawing information captured by a canvas view.
- [PKStroke](./pkstrokereference.md)
  A class that represents the paths, boundaries and other properties of a stroke drawn on a canvas.
- [PKStrokePoint](./pkstrokepointreference.md)
  A class that represents the properties of a specific point along a stroke’s path.
- [PKInk](./pkinkreference.md)
  Provides a description of the creation and rendering of marks on a canvas.
- [PKStrokeRenderState](./pkstrokerenderstatereference.md)
  An object that captures the render-time state of a stroke, such as grain texture position.
- [PKConvertedBezierPoint](./pkconvertedbezierpointreference.md)
  An object that provides information about a B-spline control point converted from a Bézier path.
- [PKFloatRange](./pkfloatrange.md)
  A utility class that represents range components of a stroke.
- [PKInkTypeReed](./pkinktypereed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepathreference)*