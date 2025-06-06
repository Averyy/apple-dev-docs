# CGPath

**Framework**: Core Graphics  
**Kind**: class

An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.

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
class CGPath
```

#### Overview

Neither `CGPath` nor [`CGMutablePath`](cgmutablepath.md) define functions to draw a path. To draw a Core Graphics path to a graphics context, you add the path to the graphics context by calling [`addPath(_:)`](cgcontext/addpath(_:).md) and then call one of the context’s drawing functions—see [`CGContext`](cgcontext.md).

Each figure in the graphics path is constructed with a connected set of lines and Bézier curves, called a . A subpath has an ordered set of  that represent single steps in the construction of the subpath. (For example, a line segment from one corner of a rectangle to another corner is a path element. Every subpath includes a , which is the first point in the subpath. The path also maintains a , which is the last point in the last subpath.

## Topics

### Creating Graphics Paths
- [init(rect: CGRect, transform: UnsafePointer<CGAffineTransform>?)](cgpath/init(rect:transform:).md)
  Create an immutable path of a rectangle.
- [init(ellipseIn: CGRect, transform: UnsafePointer<CGAffineTransform>?)](cgpath/init(ellipsein:transform:).md)
  Create an immutable path of an ellipse.
- [init(roundedRect: CGRect, cornerWidth: CGFloat, cornerHeight: CGFloat, transform: UnsafePointer<CGAffineTransform>?)](cgpath/init(roundedrect:cornerwidth:cornerheight:transform:).md)
  Create an immutable path of a rounded rectangle.
### Copying a Graphics Path
- [func copy() -> CGPath?](cgpath/copy.md)
  Creates an immutable copy of a graphics path.
- [func copy(using: UnsafePointer<CGAffineTransform>?) -> CGPath?](cgpath/copy(using:).md)
  Creates an immutable copy of a graphics path transformed by a transformation matrix.
- [func copy(dashingWithPhase: CGFloat, lengths: [CGFloat], transform: CGAffineTransform) -> CGPath](cgpath/copy(dashingwithphase:lengths:transform:).md)
  Returns a new path equivalent to the results of drawing the path with a dashed stroke.
- [func copy(strokingWithWidth: CGFloat, lineCap: CGLineCap, lineJoin: CGLineJoin, miterLimit: CGFloat, transform: CGAffineTransform) -> CGPath](cgpath/copy(strokingwithwidth:linecap:linejoin:miterlimit:transform:).md)
  Returns a new path equivalent to the results of drawing the path with a solid stroke.
- [func mutableCopy() -> CGMutablePath?](cgpath/mutablecopy.md)
  Creates a mutable copy of an existing graphics path.
- [func mutableCopy(using: UnsafePointer<CGAffineTransform>?) -> CGMutablePath?](cgpath/mutablecopy(using:).md)
  Creates a mutable copy of a graphics path transformed by a transformation matrix.
### Examining a Graphics Path
- [var boundingBox: CGRect](cgpath/boundingbox.md)
  Returns the bounding box containing all points in a graphics path.
- [var boundingBoxOfPath: CGRect](cgpath/boundingboxofpath.md)
  Returns the bounding box of a graphics path.
- [var currentPoint: CGPoint](cgpath/currentpoint.md)
  Returns the current point in a graphics path.
- [func contains(CGPoint, using: CGPathFillRule, transform: CGAffineTransform) -> Bool](cgpath/contains(_:using:transform:).md)
  Returns whether the specified point is interior to the path.
- [var isEmpty: Bool](cgpath/isempty.md)
  Indicates whether or not a graphics path is empty.
- [func isRect(UnsafeMutablePointer<CGRect>?) -> Bool](cgpath/isrect(_:).md)
  Indicates whether or not a graphics path represents a rectangle.
### Applying a Function to the Elements of a Path
- [func apply(info: UnsafeMutableRawPointer?, function: CGPathApplierFunction)](cgpath/apply(info:function:).md)
  For each element in a graphics path, calls a custom applier function.
- [typealias CGPathApplierFunction](cgpathapplierfunction.md)
  Defines a callback function that can view an element in a graphics path.
- [struct CGPathElement](cgpathelement.md)
  A data structure that provides information about a path element.
- [enum CGPathElementType](cgpathelementtype.md)
  The type of element found in a path.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](cgpath/typeid.md)
  Returns the Core Foundation type identifier for Core Graphics paths.
### Instance Methods
- [func applyWithBlock((UnsafePointer<CGPathElement>) -> Void)](cgpath/applywithblock(_:).md)
- [func componentsSeparated(using: CGPathFillRule) -> [CGPath]](cgpath/componentsseparated(using:).md)
- [func flattened(threshold: CGFloat) -> CGPath](cgpath/flattened(threshold:).md)
- [func intersection(CGPath, using: CGPathFillRule) -> CGPath](cgpath/intersection(_:using:).md)
- [func intersects(CGPath, using: CGPathFillRule) -> Bool](cgpath/intersects(_:using:).md)
- [func lineIntersection(CGPath, using: CGPathFillRule) -> CGPath](cgpath/lineintersection(_:using:).md)
- [func lineSubtracting(CGPath, using: CGPathFillRule) -> CGPath](cgpath/linesubtracting(_:using:).md)
- [func normalized(using: CGPathFillRule) -> CGPath](cgpath/normalized(using:).md)
- [func subtracting(CGPath, using: CGPathFillRule) -> CGPath](cgpath/subtracting(_:using:).md)
- [func symmetricDifference(CGPath, using: CGPathFillRule) -> CGPath](cgpath/symmetricdifference(_:using:).md)
- [func union(CGPath, using: CGPathFillRule) -> CGPath](cgpath/union(_:using:).md)

## Relationships

### Inherited By
- [CGMutablePath](cgmutablepath.md)
### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
- [class CGContext](cgcontext.md)
  A Quartz 2D drawing environment.
- [class CGImage](cgimage.md)
  A bitmap image or image mask.
- [class CGMutablePath](cgmutablepath.md)
  A mutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [class CGLayer](cglayer.md)
  An offscreen context for reusing content drawn with Core Graphics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpath)*