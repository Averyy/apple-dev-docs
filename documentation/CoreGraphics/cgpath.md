# CGPath

**Framework**: Core Graphics  
**Kind**: class  
**Role**: Class

An immutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.

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
class CGPath
```

```c
typedef const struct CGPath * CGPathRef;
```

#### Overview

Neither `CGPath` nor [`CGMutablePath`](./cgmutablepath.md) define functions to draw a path. To draw a Core Graphics path to a graphics context, you add the path to the graphics context by calling [`addPath(_:)`](./cgcontext/addpath%28_%29.md) and then call one of the context’s drawing functions—see [`CGContext`](./cgcontext.md).

Each figure in the graphics path is constructed with a connected set of lines and Bézier curves, called a *subpath*. A subpath has an ordered set of *path elements* that represent single steps in the construction of the subpath. (For example, a line segment from one corner of a rectangle to another corner is a path element. Every subpath includes a *starting point*, which is the first point in the subpath. The path also maintains a *current point*, which is the last point in the last subpath.

## Topics

### Creating Graphics Paths
- [init(rect: CGRect, transform: UnsafePointer<CGAffineTransform>?)](./cgpath/init%28rect,transform%29.md)
  Create an immutable path of a rectangle.
- [init(ellipseIn: CGRect, transform: UnsafePointer<CGAffineTransform>?)](./cgpath/init%28ellipsein,transform%29.md)
  Create an immutable path of an ellipse.
- [init(roundedRect: CGRect, cornerWidth: CGFloat, cornerHeight: CGFloat, transform: UnsafePointer<CGAffineTransform>?)](./cgpath/init%28roundedrect,cornerwidth,cornerheight,transform%29.md)
  Create an immutable path of a rounded rectangle.
### Copying a Graphics Path
- [func copy() -> CGPath?](./cgpath/copy%28%29.md)
  Creates an immutable copy of a graphics path.
- [func copy(using: UnsafePointer<CGAffineTransform>?) -> CGPath?](./cgpath/copy%28using%29.md)
  Creates an immutable copy of a graphics path transformed by a transformation matrix.
- [func copy(dashingWithPhase: CGFloat, lengths: [CGFloat], transform: CGAffineTransform) -> CGPath](./cgpath/copy%28dashingwithphase,lengths,transform%29.md)
  Returns a new path equivalent to the results of drawing the path with a dashed stroke.
- [func copy(strokingWithWidth: CGFloat, lineCap: CGLineCap, lineJoin: CGLineJoin, miterLimit: CGFloat, transform: CGAffineTransform) -> CGPath](./cgpath/copy%28strokingwithwidth,linecap,linejoin,miterlimit,transform%29.md)
  Returns a new path equivalent to the results of drawing the path with a solid stroke.
- [func mutableCopy() -> CGMutablePath?](./cgpath/mutablecopy%28%29.md)
  Creates a mutable copy of an existing graphics path.
- [func mutableCopy(using: UnsafePointer<CGAffineTransform>?) -> CGMutablePath?](./cgpath/mutablecopy%28using%29.md)
  Creates a mutable copy of a graphics path transformed by a transformation matrix.
- [CGPathCreateCopyByDashingPath](./cgpathcreatecopybydashingpath.md)
  Creates a dashed copy of another path.
- [CGPathCreateCopyByStrokingPath](./cgpathcreatecopybystrokingpath.md)
  Creates a stroked copy of another path.
### Examining a Graphics Path
- [var boundingBox: CGRect](./cgpath/boundingbox.md)
  Returns the bounding box containing all points in a graphics path.
- [var boundingBoxOfPath: CGRect](./cgpath/boundingboxofpath.md)
  Returns the bounding box of a graphics path.
- [var currentPoint: CGPoint](./cgpath/currentpoint.md)
  Returns the current point in a graphics path.
- [func contains(CGPoint, using: CGPathFillRule, transform: CGAffineTransform) -> Bool](./cgpath/contains%28_,using,transform%29.md)
  Returns whether the specified point is interior to the path.
- [var isEmpty: Bool](./cgpath/isempty.md)
  Indicates whether or not a graphics path is empty.
- [func isRect(UnsafeMutablePointer<CGRect>?) -> Bool](./cgpath/isrect%28_%29.md)
  Indicates whether or not a graphics path represents a rectangle.
- [CGPathEqualToPath](./cgpathequaltopath.md)
  Indicates whether two graphics paths are equivalent.
- [CGPathContainsPoint](./cgpathcontainspoint.md)
  Checks whether a point is contained in a graphics path.
### Applying a Function to the Elements of a Path
- [func apply(info: UnsafeMutableRawPointer?, function: CGPathApplierFunction)](./cgpath/apply%28info,function%29.md)
  For each element in a graphics path, calls a custom applier function.
- [typealias CGPathApplierFunction](./cgpathapplierfunction.md)
  Defines a callback function that can view an element in a graphics path.
- [struct CGPathElement](./cgpathelement.md)
  A data structure that provides information about a path element.
- [enum CGPathElementType](./cgpathelementtype.md)
  The type of element found in a path.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](./cgpath/typeid.md)
  Returns the Core Foundation type identifier for Core Graphics paths.
### Instance Methods
- [func applyWithBlock((UnsafePointer<CGPathElement>) -> Void)](./cgpath/applywithblock%28_%29.md)
- [func componentsSeparated(using: CGPathFillRule) -> [CGPath]](./cgpath/componentsseparated%28using%29.md)
- [func flattened(threshold: CGFloat) -> CGPath](./cgpath/flattened%28threshold%29.md)
- [func intersection(CGPath, using: CGPathFillRule) -> CGPath](./cgpath/intersection%28_,using%29.md)
- [func intersects(CGPath, using: CGPathFillRule) -> Bool](./cgpath/intersects%28_,using%29.md)
- [func lineIntersection(CGPath, using: CGPathFillRule) -> CGPath](./cgpath/lineintersection%28_,using%29.md)
- [func lineSubtracting(CGPath, using: CGPathFillRule) -> CGPath](./cgpath/linesubtracting%28_,using%29.md)
- [func normalized(using: CGPathFillRule) -> CGPath](./cgpath/normalized%28using%29.md)
- [func subtracting(CGPath, using: CGPathFillRule) -> CGPath](./cgpath/subtracting%28_,using%29.md)
- [func symmetricDifference(CGPath, using: CGPathFillRule) -> CGPath](./cgpath/symmetricdifference%28_,using%29.md)
- [func union(CGPath, using: CGPathFillRule) -> CGPath](./cgpath/union%28_,using%29.md)
### Retaining and Releasing a Path
- [CGPathRelease](./cgpathrelease.md)
  Decrements the retain count of a graphics path.
- [CGPathRetain](./cgpathretain.md)
  Increments the retain count of a graphics path.
### Constants
- [CGPathDrawingMode](./cgpathdrawingmode.md)
  Options for rendering a path.
- [CGLineCap](./cglinecap.md)
  Styles for rendering the endpoint of a stroked line.
- [CGLineJoin](./cglinejoin.md)
  Junction types for stroked lines.

## Relationships

### Inherited By
- [CGMutablePath](./cgmutablepath.md)
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
- [class CGMutablePath](./cgmutablepath.md)
  A mutable graphics path: a mathematical description of shapes or lines to be drawn in a graphics context.
- [class CGLayer](./cglayer.md)
  An offscreen context for reusing content drawn with Core Graphics.
### Opaque Types
- [CGColorRef](./cgcolor.md)
  A set of components that define a color, with a color space specifying how to interpret them.
- [CGColorConversionInfoRef](./cgcolorconversioninfo.md)
  An object that describes how to convert between color spaces for use by other system services.
- [CGColorSpaceRef](./cgcolorspace.md)
  A profile that specifies how to interpret a color value for display.
- [CGDataConsumerRef](./cgdataconsumer.md)
  An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.
- [CGDataProviderRef](./cgdataprovider.md)
  An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.
- [CGFontRef](./cgfont.md)
  A set of character glyphs and layout information for drawing text.
- [CGFunctionRef](./cgfunction.md)
  A general facility for defining and using callback functions.
- [CGGradientRef](./cggradient.md)
  A definition for a smooth transition between colors for drawing radial and axial gradient fills.
- [CGPatternRef](./cgpattern.md)
  A 2D pattern to be used for drawing graphics paths.
- [CGPDFArray](./cgpdfarray.md)
  An array structure within a PDF document.
- [CGPDFContentStream](./cgpdfcontentstream.md)
  A representation of one or more content data streams in a PDF page.
- [CGPDFDictionary](./cgpdfdictionary.md)
  A dictionary structure within a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpath)*