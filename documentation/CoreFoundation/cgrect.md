# CGRect

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

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
struct CGRect
```

```c
struct CGRect;
```

## Topics

### Initializers
- [init()](./cgrect/init%28%29.md)
- [init?(dictionaryRepresentation: CFDictionary)](./cgrect/init%28dictionaryrepresentation%29.md)
- [init(origin: CGPoint, size: CGSize)](./cgrect/init%28origin,size%29.md)
- [init(x: Double, y: Double, width: Double, height: Double)](./cgrect/init%28x,y,width,height%29-27bxn.md)
- [init(x: Int, y: Int, width: Int, height: Int)](./cgrect/init%28x,y,width,height%29-3kjh6.md)
- [init(x: CGFloat, y: CGFloat, width: CGFloat, height: CGFloat)](./cgrect/init%28x,y,width,height%29-3xq19.md)
### Instance Properties
- [var customPlaygroundQuickLook: PlaygroundQuickLook](./cgrect/customplaygroundquicklook.md)
  A custom playground Quick Look for this instance.
- [var dictionaryRepresentation: CFDictionary](./cgrect/dictionaryrepresentation.md)
- [var formattedDescription: String](./cgrect/formatteddescription.md)
- [var height: CGFloat](./cgrect/height.md)
- [var integral: CGRect](./cgrect/integral.md)
- [var isEmpty: Bool](./cgrect/isempty.md)
- [var isInfinite: Bool](./cgrect/isinfinite.md)
- [var isNull: Bool](./cgrect/isnull.md)
- [var maxX: CGFloat](./cgrect/maxx.md)
- [var maxY: CGFloat](./cgrect/maxy.md)
- [var midX: CGFloat](./cgrect/midx.md)
- [var midY: CGFloat](./cgrect/midy.md)
- [var minX: CGFloat](./cgrect/minx.md)
- [var minY: CGFloat](./cgrect/miny.md)
- [var origin: CGPoint](./cgrect/origin.md)
- [var size: CGSize](./cgrect/size.md)
- [var standardized: CGRect](./cgrect/standardized.md)
- [var width: CGFloat](./cgrect/width.md)
### Instance Methods
- [func applying(CGAffineTransform) -> CGRect](./cgrect/applying%28_%29.md)
- [func clip()](./cgrect/clip%28%29.md)
  Modifies the current graphics context clipping path by intersecting it with this rect. This permanently modifies the graphics state, so the current state should be saved beforehand and restored afterwards.
- [func contains(CGPoint) -> Bool](./cgrect/contains%28_%29-6n2uh.md)
- [func contains(CGRect) -> Bool](./cgrect/contains%28_%29-8fdse.md)
- [func divided(atDistance: CGFloat, from: CGRectEdge) -> (slice: CGRect, remainder: CGRect)](./cgrect/divided%28atdistance,from%29.md)
- [func equalTo(CGRect) -> Bool](./cgrect/equalto%28_%29.md)
- [func fill(using: NSCompositingOperation)](./cgrect/fill%28using%29.md)
  Fills this rect in the current NSGraphicsContext in the context’s fill color. The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSRectFill()`.
- [func frame(withWidth: CGFloat, using: NSCompositingOperation)](./cgrect/frame%28withwidth,using%29.md)
  Draws a frame around the inside of this rect in the current NSGraphicsContext in the context’s fill color The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSFrameRect()`.
- [func inset(by: UIEdgeInsets) -> CGRect](./cgrect/inset%28by%29.md)
- [func insetBy(dx: CGFloat, dy: CGFloat) -> CGRect](./cgrect/insetby%28dx,dy%29.md)
- [func intersection(CGRect) -> CGRect](./cgrect/intersection%28_%29.md)
- [func intersects(CGRect) -> Bool](./cgrect/intersects%28_%29.md)
- [func offsetBy(dx: CGFloat, dy: CGFloat) -> CGRect](./cgrect/offsetby%28dx,dy%29.md)
- [func union(CGRect) -> CGRect](./cgrect/union%28_%29.md)
### Type Properties
- [static var infinite: CGRect](./cgrect/infinite.md)
- [static var null: CGRect](./cgrect/null.md)
- [static var zero: CGRect](./cgrect/zero.md)

## Relationships

### Conforms To
- [Animatable](../SwiftUI/animatable.md)
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [CVAttachmentValueRepresentable](../CoreVideo/cvattachmentvaluerepresentable.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Structures
- [struct CGAffineTransform](./cgaffinetransform.md)
- [struct CGAffineTransformComponents](./cgaffinetransformcomponents.md)
- [struct CGFloat](./cgfloat-swift.struct.md)
  The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [struct CGPoint](./cgpoint.md)
- [struct CGSize](./cgsize.md)
  A structure that contains width and height values.
- [struct CGVector](./cgvector.md)
  A structure that contains a two-dimensional vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cgrect)*