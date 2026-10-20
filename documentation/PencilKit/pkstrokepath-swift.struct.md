# PKStrokePath

**Framework**: PencilKit  
**Kind**: struct

A structure that captures the components of a stroke and provides methods to find and interpolate points along the stroke’s path.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct PKStrokePath
```

## Mentions

- [Importing Bézier path data into PencilKit](importing-external-drawing-data-into-pencilkit.md)

## Topics

### Creating a new stroke path
- [init()](pkstrokepath-swift.struct/init.md)
  Creates an empty stroke path.
- [init<T>(controlPoints: T, creationDate: Date)](pkstrokepath-swift.struct/init(controlpoints:creationdate:).md)
  Creates a stroke path with the cubic B-spline control points and a date that you specify.
- [init<T>(controlPoints: T, creationDate: Date, id: UUID)](pkstrokepath-swift.struct/init(controlpoints:creationdate:id:).md)
  Creates a stroke path with the specified cubic B-spline control points and a unique identifier.
- [init(bezierPath: CGPath, creationDate: Date, pointProvider: (PKStrokePath.ConvertedBezierPoint) -> PKStrokePoint)](pkstrokepath-swift.struct/init(bezierpath:creationdate:pointprovider:).md)
  Creates a stroke path recreating the specified Bézier path as a cubic uniform B-Spline.
- [PKStrokePath.ConvertedBezierPoint](pkstrokepath-swift.struct/convertedbezierpoint.md)
  Information about a B-spline control point converted from a Bézier path.
### Identifying the path
- [var id: UUID](pkstrokepath-swift.struct/id.md)
  The unique identity of the stroke path.
### Converting to and from Bézier paths
- [var bezierRepresentation: CGPath](pkstrokepath-swift.struct/bezierrepresentation.md)
  A Bézier path representation of the path’s curve, computed in linear time.
### Getting the stroke path properties
- [var creationDate: Date](pkstrokepath-swift.struct/creationdate.md)
  The creation date and time of this stroke path.
### Accessing and interpolating points
- [func interpolatedPoints(in: ClosedRange<CGFloat>?, by: PKStrokePath.InterpolatedSlice.Stride) -> PKStrokePath.InterpolatedSlice](pkstrokepath-swift.struct/interpolatedpoints(in:by:).md)
  Returns the slice on-curve points using the floating point range and stride that you specify.
- [func interpolatedLocation(at: CGFloat) -> CGPoint](pkstrokepath-swift.struct/interpolatedlocation(at:).md)
  Returns the on-curve point for the floating point parametric value.
- [func interpolatedPoint(at: CGFloat) -> PKStrokePoint](pkstrokepath-swift.struct/interpolatedpoint(at:).md)
  Returns the on-curve point for the provided floating point parameter.
- [func parametricValue(CGFloat, offsetBy: PKStrokePath.InterpolatedSlice.Stride) -> CGFloat](pkstrokepath-swift.struct/parametricvalue(_:offsetby:).md)
### Supporting types
- [PKStrokePath.InterpolatedSlice](pkstrokepath-swift.struct/interpolatedslice.md)
  A struct representing an interpolated slice of stroke points with a specific stride across a range of this stroke data.
### Supporting protocol requirements
- [Protocol implementations](pkstrokepath-protocol-implementations.md)
  Access the stroke path’s implementations of protocol methods.
### Using reference types
- [class PKStrokePathReference](pkstrokepathreference.md)
  A class that captures the components of a stroke and provides methods to find and interpolate points along the stroke’s path.
### Subscripts
- [subscript(ClosedRange<CGFloat>) -> PKStrokePath](pkstrokepath-swift.struct/subscript(_:).md)
  Access the stroke point at the provided index.
### Default Implementations
- [Identifiable Implementations](pkstrokepath-swift.struct/identifiable-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../swift/bidirectionalcollection.md)
- [Collection](../swift/collection.md)
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [Identifiable](../swift/identifiable.md)
- [RandomAccessCollection](../swift/randomaccesscollection.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [Sequence](../swift/sequence.md)

## See Also

- [Drawing with PencilKit](drawing-with-pencilkit.md)
  Add expressive, low-latency drawing to your app using PencilKit.
- [Customizing Scribble with Interactions](customizing-scribble-with-interactions.md)
  Enable writing on a non-text-input view by adding interactions.
- [Inspecting, Modifying, and Constructing PencilKit Drawings](inspecting-modifying-and-constructing-pencilkit-drawings.md)
  Score users’ ability to match PencilKit drawings generated from text, by accessing the strokes and points inside PencilKit drawings.
- [Importing Bézier path data into PencilKit](importing-external-drawing-data-into-pencilkit.md)
  Convert existing Bézier-based stroke data into PencilKit drawing strokes.
- [Controlling stroke rendering for animation and editing](controlling-stroke-rendering-for-animation-and-editing.md)
  Slice, animate, and blend PencilKit strokes in code, while keeping grain texture and wet ink intact.
- [class PKCanvasView](pkcanvasview.md)
  A view that captures Apple Pencil input and displays the rendered results in an iOS app.
- [struct PKDrawing](pkdrawing-swift.struct.md)
  A structure representing the drawing information captured by a canvas view.
- [struct PKStroke](pkstroke-swift.struct.md)
  A structure that represents the paths, boundaries, and other properties of a stroke drawn on a canvas.
- [struct PKStrokePoint](pkstrokepoint-swift.struct.md)
  A structure that represents the properties of a specific point along a stroke’s path.
- [struct PKInk](pkink-swift.struct.md)
  A structure that represents an ink that specifies its type, color, and width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct)*