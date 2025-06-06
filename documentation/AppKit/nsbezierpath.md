# NSBezierPath

**Framework**: AppKit  
**Kind**: class

An object that can create paths using PostScript-style commands.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSBezierPath
```

#### Overview

Paths consist of straight and curved line segments joined together. Paths can form recognizable shapes such as rectangles, ovals, arcs, and glyphs; they can also form complex polygons using either straight or curved line segments. A single path can be closed by connecting its two endpoints, or it can be left open.

An [`NSBezierPath`](nsbezierpath.md) object can contain multiple disconnected paths, whether they are closed or open. Each of these paths is referred to as a subpath. The subpaths of a Bézier path object must be manipulated as a group. The only way to manipulate subpaths individually is to create separate [`NSBezierPath`](nsbezierpath.md) objects for each.

For a given [`NSBezierPath`](nsbezierpath.md) object, you can stroke the path’s outline or fill the region occupied by the path. You can also use the path as a clipping region for views or other regions. Using methods of [`NSBezierPath`](nsbezierpath.md), you can also perform hit detection on the filled or stroked path. Hit detection is needed to implement interactive graphics, as in rubber banding and dragging operations.

The current graphics context is automatically saved and restored for all drawing operations involving Bézier path objects, so your application does not need to worry about the graphics settings changing across invocations.

## Topics

### Creating a Bézier Path
- [init(ovalIn: NSRect)](nsbezierpath/init(ovalin:).md)
  Creates and returns a new Bézier path object initialized with an oval path inscribed in the specified rectangle.
- [init(rect: NSRect)](nsbezierpath/init(rect:).md)
  Creates and returns a new Bézier path object initialized with a rectangular path.
- [init(roundedRect: NSRect, xRadius: CGFloat, yRadius: CGFloat)](nsbezierpath/init(roundedrect:xradius:yradius:).md)
  Creates and returns a new Bézier path object initialized with a rounded rectangular path.
- [init(cgPath: CGPath)](nsbezierpath/init(cgpath:).md)
- [var flattened: NSBezierPath](nsbezierpath/flattened.md)
  A flattened version of the path object.
- [var reversed: NSBezierPath](nsbezierpath/reversed.md)
  A path containing the reversed contents of the current path object.
### Constructing a Path
- [func move(to: NSPoint)](nsbezierpath/move(to:).md)
  Moves the path’s current point to the specified location.
- [func line(to: NSPoint)](nsbezierpath/line(to:).md)
  Appends a straight line to the path.
- [func curve(to: NSPoint, controlPoint1: NSPoint, controlPoint2: NSPoint)](nsbezierpath/curve(to:controlpoint1:controlpoint2:).md)
  Adds a Bezier cubic curve to the path.
- [func curve(to: NSPoint, controlPoint: NSPoint)](nsbezierpath/curve(to:controlpoint:).md)
- [func close()](nsbezierpath/close.md)
  Closes the most recently added subpath.
- [func relativeMove(to: NSPoint)](nsbezierpath/relativemove(to:).md)
  Moves the path’s current point to a new point whose location is the specified distance from the current point.
- [func relativeLine(to: NSPoint)](nsbezierpath/relativeline(to:).md)
  Appends a straight line segment to the path starting at the current point and moving towards the specified point, relative to the current location.
- [func relativeCurve(to: NSPoint, controlPoint1: NSPoint, controlPoint2: NSPoint)](nsbezierpath/relativecurve(to:controlpoint1:controlpoint2:).md)
  Adds a Bezier cubic curve to the path from the current point to a new location, which is specified as a relative distance from the current point.
- [func relativeCurve(to: NSPoint, controlPoint: NSPoint)](nsbezierpath/relativecurve(to:controlpoint:).md)
### Appending Common Shapes to a Path
- [func append(NSBezierPath)](nsbezierpath/append(_:).md)
  Appends the contents of the specified path object to the path.
- [func appendPoints(NSPointArray, count: Int)](nsbezierpath/appendpoints(_:count:).md)
  Appends a series of line segments to the path.
- [func appendOval(in: NSRect)](nsbezierpath/appendoval(in:).md)
  Appends an oval path to the path, inscribing the oval in the specified rectangle.
- [func appendArc(from: NSPoint, to: NSPoint, radius: CGFloat)](nsbezierpath/appendarc(from:to:radius:).md)
  Appends an arc to the path.
- [func appendArc(withCenter: NSPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat)](nsbezierpath/appendarc(withcenter:radius:startangle:endangle:).md)
  Appends an arc of a circle to the path.
- [func appendArc(withCenter: NSPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](nsbezierpath/appendarc(withcenter:radius:startangle:endangle:clockwise:).md)
  Appends an arc of a circle to the path.
- [func appendRect(NSRect)](nsbezierpath/appendrect(_:).md)
  Appends a rectangular path to the path.
- [func appendRoundedRect(NSRect, xRadius: CGFloat, yRadius: CGFloat)](nsbezierpath/appendroundedrect(_:xradius:yradius:).md)
  Appends a rounded rectangular path to the path.
- [func append(withCGGlyph: CGGlyph, in: NSFont)](nsbezierpath/append(withcgglyph:in:).md)
  Appends an outline of the specified glyph to the path.
- [func append(withCGGlyphs: UnsafePointer<CGGlyph>, count: Int, in: NSFont)](nsbezierpath/append(withcgglyphs:count:in:).md)
  Appends the outlines of the specified glyphs to the path.
- [func appendGlyph(NSGlyph, in: NSFont)](nsbezierpath/appendglyph(_:in:).md)
  Appends an outline of the specified glyph to the path.
- [func appendGlyphs(UnsafeMutablePointer<NSGlyph>, count: Int, in: NSFont)](nsbezierpath/appendglyphs(_:count:in:).md)
  Appends the outlines of the specified glyphs to the path.
- [func appendPackedGlyphs(UnsafePointer<CChar>)](nsbezierpath/appendpackedglyphs(_:).md)
  Appends an array of packed glyphs to the path.
### Accessing a Path’s Attributes
- [var windingRule: NSBezierPath.WindingRule](nsbezierpath/windingrule-swift.property.md)
  The winding rule used to fill the path.
- [var lineCapStyle: NSBezierPath.LineCapStyle](nsbezierpath/linecapstyle-swift.property.md)
  The line cap style for the path.
- [var lineJoinStyle: NSBezierPath.LineJoinStyle](nsbezierpath/linejoinstyle-swift.property.md)
  The line join style for the path.
- [var lineWidth: CGFloat](nsbezierpath/linewidth.md)
  The width of stroked path lines.
- [var miterLimit: CGFloat](nsbezierpath/miterlimit.md)
  The limit at which miter joins are converted to bevel joins.
- [var flatness: CGFloat](nsbezierpath/flatness.md)
  The accuracy with which curves are rendered.
- [func getLineDash(UnsafeMutablePointer<CGFloat>?, count: UnsafeMutablePointer<Int>?, phase: UnsafeMutablePointer<CGFloat>?)](nsbezierpath/getlinedash(_:count:phase:).md)
  Returns the line-stroking pattern for the receiver.
- [func setLineDash(UnsafePointer<CGFloat>?, count: Int, phase: CGFloat)](nsbezierpath/setlinedash(_:count:phase:).md)
  Sets the line-stroking pattern for the path.
### Configuring Default Path Attributes
- [class var defaultWindingRule: NSBezierPath.WindingRule](nsbezierpath/defaultwindingrule.md)
  Returns the default winding rule used to fill all paths.
- [class var defaultLineCapStyle: NSBezierPath.LineCapStyle](nsbezierpath/defaultlinecapstyle.md)
  Returns the default line cap style for all paths.
- [class var defaultLineJoinStyle: NSBezierPath.LineJoinStyle](nsbezierpath/defaultlinejoinstyle.md)
  Returns the default line join style for all paths.
- [class var defaultLineWidth: CGFloat](nsbezierpath/defaultlinewidth.md)
  Returns the default line width for the all paths.
- [class var defaultMiterLimit: CGFloat](nsbezierpath/defaultmiterlimit.md)
  Returns the default miter limit for all paths.
- [class var defaultFlatness: CGFloat](nsbezierpath/defaultflatness.md)
  The default flatness value for all paths.
### Drawing a Path
- [func stroke()](nsbezierpath/stroke.md)
  Draws a line along the path using the current stroke color and drawing attributes.
- [func fill()](nsbezierpath/fill.md)
  Paints the region enclosed by the path.
- [class func fill(NSRect)](nsbezierpath/fill(_:).md)
  Fills the specified rectangular path with the current fill color.
- [class func stroke(NSRect)](nsbezierpath/stroke(_:).md)
  Strokes the path of the specified rectangle using the current stroke color and the default drawing attributes.
- [class func strokeLine(from: NSPoint, to: NSPoint)](nsbezierpath/strokeline(from:to:).md)
  Strokes a line between two points using the current stroke color and the default drawing attributes.
- [class func drawPackedGlyphs(UnsafePointer<CChar>, at: NSPoint)](nsbezierpath/drawpackedglyphs(_:at:).md)
  Draws a set of packed glyphs at the specified point in the current coordinate system.
### Specifying a Clipping Path
- [func addClip()](nsbezierpath/addclip.md)
  Intersects the area enclosed by the path with the clipping path of the current graphics context and makes the resulting shape the current clipping path.
- [func setClip()](nsbezierpath/setclip.md)
  Replaces the clipping path of the current graphics context with the area inside the path.
- [class func clip(NSRect)](nsbezierpath/clip(_:).md)
  Intersects the specified rectangle with the clipping path of the current graphics context and makes the resulting shape the current clipping path.
### Performing Hit-Testing
- [func contains(NSPoint) -> Bool](nsbezierpath/contains(_:).md)
  Returns a Boolean value that indicates whether the path contains the specified point.
### Querying a Path
- [var bounds: NSRect](nsbezierpath/bounds.md)
  The bounding box of the path.
- [var controlPointBounds: NSRect](nsbezierpath/controlpointbounds.md)
  The bounding box of the path, including any control points.
- [var currentPoint: NSPoint](nsbezierpath/currentpoint.md)
  The current point (the trailing point or ending point in the most recently added segment).
- [var isEmpty: Bool](nsbezierpath/isempty.md)
  A Boolean value that indicates whether the path is empty.
### Applying Transformations
- [func transform(using: AffineTransform)](nsbezierpath/transform(using:).md)
  Transforms all points in the path using the specified transform.
### Accessing Elements of a Path
- [var cgPath: CGPath](nsbezierpath/cgpath.md)
- [var elementCount: Int](nsbezierpath/elementcount.md)
  The total number of path elements in the path.
- [func element(at: Int) -> NSBezierPath.ElementType](nsbezierpath/element(at:).md)
  Returns the type of path element at the specified index.
- [func element(at: Int, associatedPoints: NSPointArray?) -> NSBezierPath.ElementType](nsbezierpath/element(at:associatedpoints:).md)
  Gets the element type and (and optionally) the associated points for the path element at the specified index.
- [func removeAllPoints()](nsbezierpath/removeallpoints.md)
  Removes all path elements from the path, effectively clearing the path.
- [func setAssociatedPoints(NSPointArray?, at: Int)](nsbezierpath/setassociatedpoints(_:at:).md)
  Changes the points associated with the specified path element.
### Constants
- [NSBezierPath.ElementType](nsbezierpath/elementtype.md)
  Constants that specify basic path element commands.
- [NSBezierPath.LineJoinStyle](nsbezierpath/linejoinstyle-swift.enum.md)
  Constants that specify the shape of the joins between connected segments of a stroked path.
- [NSBezierPath.LineCapStyle](nsbezierpath/linecapstyle-swift.enum.md)
  Constants that specify the shape of endpoints for an open path when it is stroked.
- [NSBezierPath.WindingRule](nsbezierpath/windingrule-swift.enum.md)
  Constants that specify the winding rule a Bézier path uses.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Convenience Functions](convenience-functions.md)
  Draw rectangles and other primitive shapes using these convenience functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath)*