# CGMutablePath

**Framework**: Core Graphics  
**Kind**: class

A mutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CGMutablePath
```

#### Overview

Neither `CGPath` nor [`CGMutablePath`](cgmutablepath.md) define functions to draw a path. To draw a Core Graphics path to a graphics context, you add the path to the graphics context by calling [`addPath(_:)`](cgcontext/addpath(_:).md) and then call one of the context’s drawing functions—see [`CGContext`](cgcontext.md).

Each figure in the graphics path is constructed with a connected set of lines and Bézier curves, called a . A subpath has an ordered set of  that represent single steps in the construction of the subpath. (For example, a line segment from one corner of a rectangle to another corner is a path element. Every subpath includes a , which is the first point in the subpath. The path also maintains a , which is the last point in the last subpath.

To append a new subpath onto a mutable path, your application typically calls [`CGPathMoveToPoint`](cgpathmovetopoint.md) to set the subpath’s starting point and initial current point, followed by a series of “add” calls (such as [`CGPathAddLineToPoint`](cgpathaddlinetopoint.md)) to add line segments and curves to the subpath. As segments or curves are added to the subpath, the subpath’s current point is updated to point to the end of the last segment or curve to be added. The lines and curves of a subpath are always connected, but they are not required to form a closed set of lines. Your application explicitly closes a subpath by calling [`closeSubpath()`](cgmutablepath/closesubpath().md). Closing the subpath adds a line segment that terminates at the subpath’s starting point, and also changes how those lines are rendered—for more information see [`Paths`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_paths/dq_paths.html#//apple_ref/doc/uid/TP30001066-CH211) in [`Quartz 2D Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066).

## Topics

### Creating Graphics Paths
- [init()](cgmutablepath/init.md)
  Creates a mutable graphics path.
### Copying a Graphics Path
- [func mutableCopy() -> CGMutablePath?](cgpath/mutablecopy.md)
  Creates a mutable copy of an existing graphics path.
- [func mutableCopy(using: UnsafePointer<CGAffineTransform>?) -> CGMutablePath?](cgpath/mutablecopy(using:).md)
  Creates a mutable copy of a graphics path transformed by a transformation matrix.
### Constructing a Graphics Path
- [func move(to: CGPoint, transform: CGAffineTransform)](cgmutablepath/move(to:transform:).md)
  Begins a new subpath at the specified point.
- [func addLine(to: CGPoint, transform: CGAffineTransform)](cgmutablepath/addline(to:transform:).md)
  Appends a straight line segment from the current point to the specified point.
- [func addLines(between: [CGPoint], transform: CGAffineTransform)](cgmutablepath/addlines(between:transform:).md)
  Adds a sequence of connected straight-line segments to the path.
- [func addRect(CGRect, transform: CGAffineTransform)](cgmutablepath/addrect(_:transform:).md)
  Adds a rectangular subpath to the path.
- [func addRects([CGRect], transform: CGAffineTransform)](cgmutablepath/addrects(_:transform:).md)
  Adds a set of rectangular subpaths to the path.
- [func addEllipse(in: CGRect, transform: CGAffineTransform)](cgmutablepath/addellipse(in:transform:).md)
  Adds an ellipse that fits inside the specified rectangle.
- [func addRoundedRect(in: CGRect, cornerWidth: CGFloat, cornerHeight: CGFloat, transform: CGAffineTransform)](cgmutablepath/addroundedrect(in:cornerwidth:cornerheight:transform:).md)
  Adds a subpath to the path, in the shape of a rectangle with rounded corners.
- [func addArc(center: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool, transform: CGAffineTransform)](cgmutablepath/addarc(center:radius:startangle:endangle:clockwise:transform:).md)
  Adds an arc of a circle to the path, specified with a radius and angles.
- [func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat, transform: CGAffineTransform)](cgmutablepath/addarc(tangent1end:tangent2end:radius:transform:).md)
  Adds an arc of a circle to the path, specified with a radius and two tangent lines.
- [func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: CGFloat, delta: CGFloat, transform: CGAffineTransform)](cgmutablepath/addrelativearc(center:radius:startangle:delta:transform:).md)
  Adds an arc of a circle to the path, specified with a radius and a difference in angle.
- [func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint, transform: CGAffineTransform)](cgmutablepath/addcurve(to:control1:control2:transform:).md)
  Adds a cubic Bézier curve to the path, with the specified end point and control points.
- [func addQuadCurve(to: CGPoint, control: CGPoint, transform: CGAffineTransform)](cgmutablepath/addquadcurve(to:control:transform:).md)
  Adds a quadratic Bézier curve to the path, with the specified end point and control point.
- [func addPath(CGPath, transform: CGAffineTransform)](cgmutablepath/addpath(_:transform:).md)
  Appends another path object to the path.
- [func closeSubpath()](cgmutablepath/closesubpath.md)
  Closes and completes a subpath in a mutable graphics path.

## Relationships

### Inherits From
- [CGPath](cgpath.md)
### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
- [class CGContext](cgcontext.md)
  A Quartz 2D drawing environment.
- [class CGImage](cgimage.md)
  A bitmap image or image mask.
- [class CGPath](cgpath.md)
  An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [class CGLayer](cglayer.md)
  An offscreen context for reusing content drawn with Core Graphics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgmutablepath)*