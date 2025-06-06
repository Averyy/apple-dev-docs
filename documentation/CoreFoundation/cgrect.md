# CGRect

**Framework**: Core Foundation  
**Kind**: struct

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
struct CGRect
```

## Topics

### Initializers
- [init()](cgrect/init.md)
- [init?(dictionaryRepresentation: CFDictionary)](cgrect/init(dictionaryrepresentation:).md)
- [init(origin: CGPoint, size: CGSize)](cgrect/init(origin:size:).md)
- [init(x: Double, y: Double, width: Double, height: Double)](cgrect/init(x:y:width:height:)-27bxn.md)
- [init(x: Int, y: Int, width: Int, height: Int)](cgrect/init(x:y:width:height:)-3kjh6.md)
- [init(x: CGFloat, y: CGFloat, width: CGFloat, height: CGFloat)](cgrect/init(x:y:width:height:)-3xq19.md)
### Instance Properties
- [var customPlaygroundQuickLook: PlaygroundQuickLook](cgrect/customplaygroundquicklook.md)
  A custom playground Quick Look for this instance.
- [var dictionaryRepresentation: CFDictionary](cgrect/dictionaryrepresentation.md)
- [var height: CGFloat](cgrect/height.md)
- [var integral: CGRect](cgrect/integral.md)
- [var isEmpty: Bool](cgrect/isempty.md)
- [var isInfinite: Bool](cgrect/isinfinite.md)
- [var isNull: Bool](cgrect/isnull.md)
- [var maxX: CGFloat](cgrect/maxx.md)
- [var maxY: CGFloat](cgrect/maxy.md)
- [var midX: CGFloat](cgrect/midx.md)
- [var midY: CGFloat](cgrect/midy.md)
- [var minX: CGFloat](cgrect/minx.md)
- [var minY: CGFloat](cgrect/miny.md)
- [var origin: CGPoint](cgrect/origin.md)
- [var size: CGSize](cgrect/size.md)
- [var standardized: CGRect](cgrect/standardized.md)
- [var width: CGFloat](cgrect/width.md)
### Instance Methods
- [func applying(CGAffineTransform) -> CGRect](cgrect/applying(_:).md)
- [func clip()](cgrect/clip.md)
  Modifies the current graphics context clipping path by intersecting it with this rect. This permanently modifies the graphics state, so the current state should be saved beforehand and restored afterwards.
- [func contains(CGPoint) -> Bool](cgrect/contains(_:)-6n2uh.md)
- [func contains(CGRect) -> Bool](cgrect/contains(_:)-8fdse.md)
- [func divided(atDistance: CGFloat, from: CGRectEdge) -> (slice: CGRect, remainder: CGRect)](cgrect/divided(atdistance:from:).md)
- [func equalTo(CGRect) -> Bool](cgrect/equalto(_:).md)
- [func fill(using: NSCompositingOperation)](cgrect/fill(using:).md)
  Fills this rect in the current NSGraphicsContext in the context’s fill color. The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSRectFill()`.
- [func frame(withWidth: CGFloat, using: NSCompositingOperation)](cgrect/frame(withwidth:using:).md)
  Draws a frame around the inside of this rect in the current NSGraphicsContext in the context’s fill color The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSFrameRect()`.
- [func inset(by: UIEdgeInsets) -> CGRect](cgrect/inset(by:).md)
- [func insetBy(dx: CGFloat, dy: CGFloat) -> CGRect](cgrect/insetby(dx:dy:).md)
- [func intersection(CGRect) -> CGRect](cgrect/intersection(_:).md)
- [func intersects(CGRect) -> Bool](cgrect/intersects(_:).md)
- [func offsetBy(dx: CGFloat, dy: CGFloat) -> CGRect](cgrect/offsetby(dx:dy:).md)
- [func union(CGRect) -> CGRect](cgrect/union(_:).md)
### Type Properties
- [static var infinite: CGRect](cgrect/infinite.md)
- [static var null: CGRect](cgrect/null.md)
- [static var zero: CGRect](cgrect/zero.md)

## Relationships

### Conforms To
- [Animatable](../SwiftUI/Animatable.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct CGAffineTransform](cgaffinetransform.md)
- [struct CGAffineTransformComponents](cgaffinetransformcomponents.md)
- [struct CGFloat](cgfloat-swift.struct.md)
  The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [struct CGPoint](cgpoint.md)
- [struct CGSize](cgsize.md)
  A structure that contains width and height values.
- [struct CGVector](cgvector.md)
  A structure that contains a two-dimensional vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cgrect)*