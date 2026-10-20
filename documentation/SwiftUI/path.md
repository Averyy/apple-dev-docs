# Path

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The outline of a 2D shape.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct Path
```

## Topics

### Creating a path
- [init()](./path/init%28%29.md)
  Creates an empty path.
- [init(_:)](./path/init%28_%29.md)
  Creates an empty path, then executes a closure to add its initial elements.
- [init(ellipseIn: CGRect)](./path/init%28ellipsein%29.md)
  Creates a path as an ellipse within the given rectangle.
- [init(roundedRect: CGRect, cornerRadius: CGFloat, style: RoundedCornerStyle)](./path/init%28roundedrect,cornerradius,style%29.md)
  Creates a path containing a rounded rectangle.
- [init(roundedRect: CGRect, cornerSize: CGSize, style: RoundedCornerStyle)](./path/init%28roundedrect,cornersize,style%29.md)
  Creates a path containing a rounded rectangle.
- [init(roundedRect: CGRect, cornerRadii: RectangleCornerRadii, style: RoundedCornerStyle)](./path/init%28roundedrect,cornerradii,style%29.md)
  Creates a path as the given rounded rectangle, which may have uneven corner radii.
### Getting the path’s characteristics
- [var boundingRect: CGRect](./path/boundingrect.md)
  A rectangle containing all path segments.
- [var cgPath: CGPath](./path/cgpath.md)
  An immutable path representing the elements in the path.
- [func contains(CGPoint, eoFill: Bool) -> Bool](./path/contains%28_,eofill%29.md)
  Returns true if the path contains a specified point.
- [var currentPoint: CGPoint?](./path/currentpoint.md)
  Returns the last point in the path, or nil if the path contains no points.
- [var description: String](./path/description.md)
  A description of the path that may be used to recreate the path via `init?(_:)`.
- [var isEmpty: Bool](./path/isempty.md)
  A Boolean value indicating whether the path contains zero elements.
### Drawing a path
- [func move(to: CGPoint)](./path/move%28to%29.md)
  Begins a new subpath at the specified point.
- [func addArc(center: CGPoint, radius: CGFloat, startAngle: Angle, endAngle: Angle, clockwise: Bool, transform: CGAffineTransform)](./path/addarc%28center,radius,startangle,endangle,clockwise,transform%29.md)
  Adds an arc of a circle to the path, specified with a radius and angles.
- [func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat, transform: CGAffineTransform)](./path/addarc%28tangent1end,tangent2end,radius,transform%29.md)
  Adds an arc of a circle to the path, specified with a radius and two tangent lines.
- [func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)](./path/addcurve%28to,control1,control2%29.md)
  Adds a cubic Bézier curve to the path, with the specified end point and control points.
- [func addEllipse(in: CGRect, transform: CGAffineTransform)](./path/addellipse%28in,transform%29.md)
  Adds an ellipse that fits inside the specified rectangle to the path.
- [func addLine(to: CGPoint)](./path/addline%28to%29.md)
  Appends a straight line segment from the current point to the specified point.
- [func addLines([CGPoint])](./path/addlines%28_%29.md)
  Adds a sequence of connected straight-line segments to the path.
- [func addPath(Path, transform: CGAffineTransform)](./path/addpath%28_,transform%29.md)
  Appends another path value to this path.
- [func addQuadCurve(to: CGPoint, control: CGPoint)](./path/addquadcurve%28to,control%29.md)
  Adds a quadratic Bézier curve to the path, with the specified end point and control point.
- [func addRect(CGRect, transform: CGAffineTransform)](./path/addrect%28_,transform%29.md)
  Adds a rectangular subpath to the path.
- [func addRects([CGRect], transform: CGAffineTransform)](./path/addrects%28_,transform%29.md)
  Adds a set of rectangular subpaths to the path.
- [func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: Angle, delta: Angle, transform: CGAffineTransform)](./path/addrelativearc%28center,radius,startangle,delta,transform%29.md)
  Adds an arc of a circle to the path, specified with a radius and a difference in angle.
- [func addRoundedRect(in: CGRect, cornerSize: CGSize, style: RoundedCornerStyle, transform: CGAffineTransform)](./path/addroundedrect%28in,cornersize,style,transform%29.md)
  Adds a rounded rectangle to the path.
- [func closeSubpath()](./path/closesubpath%28%29.md)
  Closes and completes the current subpath.
### Transforming the path
- [func applying(CGAffineTransform) -> Path](./path/applying%28_%29.md)
  Returns a path constructed by applying the transform to all points of the path.
- [func offsetBy(dx: CGFloat, dy: CGFloat) -> Path](./path/offsetby%28dx,dy%29.md)
  Returns a path constructed by translating all its points.
- [func trimmedPath(from: CGFloat, to: CGFloat) -> Path](./path/trimmedpath%28from,to%29.md)
  Returns a partial copy of the path.
### Performing operations on the path
- [func addRoundedRect(in: CGRect, cornerSize: CGSize, style: RoundedCornerStyle, transform: CGAffineTransform)](./path/addroundedrect%28in,cornersize,style,transform%29.md)
  Adds a rounded rectangle to the path.
- [func intersection(Path, eoFill: Bool) -> Path](./path/intersection%28_,eofill%29.md)
  Returns a new path with filled regions common to both paths.
- [func lineIntersection(Path, eoFill: Bool) -> Path](./path/lineintersection%28_,eofill%29.md)
  Returns a new path with a line from this path that overlaps the filled regions of the given path.
- [func lineSubtraction(Path, eoFill: Bool) -> Path](./path/linesubtraction%28_,eofill%29.md)
  Returns a new path with a line from this path that does not overlap the filled region of the given path.
- [func normalized(eoFill: Bool) -> Path](./path/normalized%28eofill%29.md)
  Returns a new weakly-simple copy of this path.
- [func subtracting(Path, eoFill: Bool) -> Path](./path/subtracting%28_,eofill%29.md)
  Returns a new path with filled regions from this path that are not in the given path.
- [func symmetricDifference(Path, eoFill: Bool) -> Path](./path/symmetricdifference%28_,eofill%29.md)
  Returns a new path with filled regions either from this path or the given path, but not in both.
- [func union(Path, eoFill: Bool) -> Path](./path/union%28_,eofill%29.md)
  Returns a new path with filled regions in either this path or the given path.
### Operating over path elements
- [func forEach((Path.Element) -> Void)](./path/foreach%28_%29.md)
  Calls `body` with each element in the path.
- [Path.Element](./path/element.md)
  An element of a path.
### Applying a style
- [func strokedPath(StrokeStyle) -> Path](./path/strokedpath%28_%29.md)
  Returns a stroked copy of the path using `style` to define how the stroked outline is created.
### Instance Methods
- [func addRoundedRect(in: CGRect, cornerRadii: RectangleCornerRadii, style: RoundedCornerStyle, transform: CGAffineTransform)](./path/addroundedrect%28in,cornerradii,style,transform%29.md)
  Adds a rounded rectangle with uneven corners to the path.

## Relationships

### Conforms To
- [Animatable](./animatable.md)
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [LosslessStringConvertible](../Swift/losslessstringconvertible.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Shape](./shape.md)
- [View](./view.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/path)*