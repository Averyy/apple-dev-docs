# CGMutablePath

**Framework**: Core Graphics  
**Kind**: class  
**Role**: Class

A mutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class CGMutablePath
```

```c
typedef struct CGPath * CGMutablePathRef;
```

## Overview

Neither `CGPath` nor [`CGMutablePath`](./cgmutablepath.md) define functions to draw a path. To draw a Core Graphics path to a graphics context, you add the path to the graphics context by calling [`addPath(_:)`](./cgcontext/addpath%28_%29.md) and then call one of the context’s drawing functions—see [`CGContext`](./cgcontext.md).

Each figure in the graphics path is constructed with a connected set of lines and Bézier curves, called a *subpath*. A subpath has an ordered set of *path elements* that represent single steps in the construction of the subpath. (For example, a line segment from one corner of a rectangle to another corner is a path element. Every subpath includes a *starting point*, which is the first point in the subpath. The path also maintains a *current point*, which is the last point in the last subpath.

To append a new subpath onto a mutable path, your application typically calls [`CGPathMoveToPoint`](./cgpathmovetopoint.md) to set the subpath’s starting point and initial current point, followed by a series of “add” calls (such as [`CGPathAddLineToPoint`](./cgpathaddlinetopoint.md)) to add line segments and curves to the subpath. As segments or curves are added to the subpath, the subpath’s current point is updated to point to the end of the last segment or curve to be added. The lines and curves of a subpath are always connected, but they are not required to form a closed set of lines. Your application explicitly closes a subpath by calling [`closeSubpath()`](./cgmutablepath/closesubpath%28%29.md). Closing the subpath adds a line segment that terminates at the subpath’s starting point, and also changes how those lines are rendered—for more information see [Paths](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_paths/dq_paths.html#//apple_ref/doc/uid/TP30001066-CH211) in [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066).

## Topics

### Creating Graphics Paths
- [init()](./cgmutablepath/init%28%29.md)
  Creates a mutable graphics path.
### Copying a Graphics Path
- [func mutableCopy() -> CGMutablePath?](./cgpath/mutablecopy%28%29.md)
  Creates a mutable copy of an existing graphics path.
- [func mutableCopy(using: UnsafePointer<CGAffineTransform>?) -> CGMutablePath?](./cgpath/mutablecopy%28using%29.md)
  Creates a mutable copy of a graphics path transformed by a transformation matrix.
### Constructing a Graphics Path
- [func move(to: CGPoint, transform: CGAffineTransform)](./cgmutablepath/move%28to,transform%29.md)
  Begins a new subpath at the specified point.
- [func addLine(to: CGPoint, transform: CGAffineTransform)](./cgmutablepath/addline%28to,transform%29.md)
  Appends a straight line segment from the current point to the specified point.
- [func addLines(between: [CGPoint], transform: CGAffineTransform)](./cgmutablepath/addlines%28between,transform%29.md)
  Adds a sequence of connected straight-line segments to the path.
- [func addRect(CGRect, transform: CGAffineTransform)](./cgmutablepath/addrect%28_,transform%29.md)
  Adds a rectangular subpath to the path.
- [func addRects([CGRect], transform: CGAffineTransform)](./cgmutablepath/addrects%28_,transform%29.md)
  Adds a set of rectangular subpaths to the path.
- [func addEllipse(in: CGRect, transform: CGAffineTransform)](./cgmutablepath/addellipse%28in,transform%29.md)
  Adds an ellipse that fits inside the specified rectangle.
- [func addRoundedRect(in: CGRect, cornerWidth: CGFloat, cornerHeight: CGFloat, transform: CGAffineTransform)](./cgmutablepath/addroundedrect%28in,cornerwidth,cornerheight,transform%29.md)
  Adds a subpath to the path, in the shape of a rectangle with rounded corners.
- [func addArc(center: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool, transform: CGAffineTransform)](./cgmutablepath/addarc%28center,radius,startangle,endangle,clockwise,transform%29.md)
  Adds an arc of a circle to the path, specified with a radius and angles.
- [func addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat, transform: CGAffineTransform)](./cgmutablepath/addarc%28tangent1end,tangent2end,radius,transform%29.md)
  Adds an arc of a circle to the path, specified with a radius and two tangent lines.
- [func addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: CGFloat, delta: CGFloat, transform: CGAffineTransform)](./cgmutablepath/addrelativearc%28center,radius,startangle,delta,transform%29.md)
  Adds an arc of a circle to the path, specified with a radius and a difference in angle.
- [func addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint, transform: CGAffineTransform)](./cgmutablepath/addcurve%28to,control1,control2,transform%29.md)
  Adds a cubic Bézier curve to the path, with the specified end point and control points.
- [func addQuadCurve(to: CGPoint, control: CGPoint, transform: CGAffineTransform)](./cgmutablepath/addquadcurve%28to,control,transform%29.md)
  Adds a quadratic Bézier curve to the path, with the specified end point and control point.
- [func addPath(CGPath, transform: CGAffineTransform)](./cgmutablepath/addpath%28_,transform%29.md)
  Appends another path object to the path.
- [func closeSubpath()](./cgmutablepath/closesubpath%28%29.md)
  Closes and completes a subpath in a mutable graphics path.
- [CGPathMoveToPoint](./cgpathmovetopoint.md)
  Starts a new subpath at a specified location in a mutable graphics path.
- [CGPathAddLineToPoint](./cgpathaddlinetopoint.md)
  Appends a line segment to a mutable graphics path.
- [CGPathAddLines](./cgpathaddlines.md)
  Appends an array of new line segments to a mutable graphics path.
- [CGPathAddRect](./cgpathaddrect.md)
  Appends a rectangle to a mutable graphics path.
- [CGPathAddRects](./cgpathaddrects.md)
  Appends an array of rectangles to a mutable graphics path.
- [CGPathAddEllipseInRect](./cgpathaddellipseinrect.md)
  Adds to a path an ellipse that fits inside a rectangle.
- [CGPathAddRoundedRect](./cgpathaddroundedrect.md)
  Appends a rounded rectangle to a mutable graphics path.
- [CGPathAddArc](./cgpathaddarc.md)
  Appends an arc to a mutable graphics path, possibly preceded by a straight line segment.
- [CGPathAddArcToPoint](./cgpathaddarctopoint.md)
  Appends an arc to a mutable graphics path, possibly preceded by a straight line segment.
- [CGPathAddRelativeArc](./cgpathaddrelativearc.md)
  Appends an arc to a mutable graphics path, possibly preceded by a straight line segment.
- [CGPathAddCurveToPoint](./cgpathaddcurvetopoint.md)
  Appends a cubic Bézier curve to a mutable graphics path.
- [CGPathAddQuadCurveToPoint](./cgpathaddquadcurvetopoint.md)
  Appends a quadratic Bézier curve to a mutable graphics path.
- [CGPathAddPath](./cgpathaddpath.md)
  Appends a path to onto a mutable graphics path.
### Retaining and Releasing a Path
- [CGPathRelease](./cgpathrelease.md)
  Decrements the retain count of a graphics path.
- [CGPathRetain](./cgpathretain.md)
  Increments the retain count of a graphics path.

## Relationships

### Inherits From
- [CGPath](./cgpath.md)
### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Related Documentation
- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
### 2D Drawing
- [class CGContext](./cgcontext.md)
  A Quartz 2D drawing environment.
- [class CGImage](./cgimage.md)
  A bitmap image or image mask.
- [class CGPath](./cgpath.md)
  An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [class CGLayer](./cglayer.md)
  An offscreen context for reusing content drawn with Core Graphics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgmutablepath)*