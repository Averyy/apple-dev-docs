# Shape

**Framework**: SwiftUI  
**Kind**: protocol

A 2D shape that you can use when drawing a view.

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
protocol Shape : Sendable, Animatable, View, _RemoveGlobalActorIsolation
```

#### Overview

Shapes without an explicit fill or stroke get a default fill based on the foreground color.

You can define shapes in relation to an implicit frame of reference, such as the natural size of the view that contains it. Alternatively, you can define shapes in terms of absolute coordinates.

## Topics

### Getting standard shapes
- [static var buttonBorder: ButtonBorderShape](shape/buttonborder.md)
  A shape that defers to the environment to determine the resolved button border shape.
- [static var capsule: Capsule](shape/capsule.md)
  A capsule shape aligned inside the frame of the view containing it.
- [static func capsule(style: RoundedCornerStyle) -> Self](shape/capsule(style:).md)
  A capsule shape aligned inside the frame of the view containing it.
- [static var circle: Circle](shape/circle.md)
  A circle centered on the frame of the view containing it.
- [static var containerRelative: ContainerRelativeShape](shape/containerrelative.md)
  A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.
- [static var ellipse: Ellipse](shape/ellipse.md)
  An ellipse aligned inside the frame of the view containing it.
- [static var rect: Rectangle](shape/rect.md)
  A rectangular shape aligned inside the frame of the view containing it.
- [static func rect(cornerRadii: RectangleCornerRadii, style: RoundedCornerStyle) -> Self](shape/rect(cornerradii:style:).md)
  A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [static func rect(cornerRadius: CGFloat, style: RoundedCornerStyle) -> Self](shape/rect(cornerradius:style:).md)
  A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [static func rect(cornerSize: CGSize, style: RoundedCornerStyle) -> Self](shape/rect(cornersize:style:).md)
  A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [static func rect(topLeadingRadius: CGFloat, bottomLeadingRadius: CGFloat, bottomTrailingRadius: CGFloat, topTrailingRadius: CGFloat, style: RoundedCornerStyle) -> Self](shape/rect(topleadingradius:bottomleadingradius:bottomtrailingradius:toptrailingradius:style:).md)
  A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
### Defining a shape’s size and path
- [func sizeThatFits(ProposedViewSize) -> CGSize](shape/sizethatfits(_:).md)
  Returns the size of the view that will render the shape, given a proposed size.
- [func path(in: CGRect) -> Path](shape/path(in:).md)
  Describes this shape as a path within a rectangular frame of reference.
### Transforming a shape
- [func trim(from: CGFloat, to: CGFloat) -> some Shape](shape/trim(from:to:).md)
  Trims this shape by a fractional amount based on its representation as a path.
- [func transform(CGAffineTransform) -> TransformedShape<Self>](shape/transform(_:).md)
  Applies an affine transform to this shape.
- [func size(CGSize) -> some Shape](shape/size(_:).md)
  Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of `size`. This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [func size(width: CGFloat, height: CGFloat) -> some Shape](shape/size(width:height:).md)
  Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of size `(width, height)`. This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [func scale(CGFloat, anchor: UnitPoint) -> ScaledShape<Self>](shape/scale(_:anchor:).md)
  Scales this shape without changing its bounding frame.
- [func scale(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> ScaledShape<Self>](shape/scale(x:y:anchor:).md)
  Scales this shape without changing its bounding frame.
- [func rotation(Angle, anchor: UnitPoint) -> RotatedShape<Self>](shape/rotation(_:anchor:).md)
  Rotates this shape around an anchor point at the angle you specify.
- [func offset(_:)](shape/offset(_:).md)
  Changes the relative position of this shape using the specified point.
- [func offset(x: CGFloat, y: CGFloat) -> OffsetShape<Self>](shape/offset(x:y:).md)
  Changes the relative position of this shape using the specified point.
### Setting the stroke characteristics
- [func stroke<S>(S, lineWidth: CGFloat) -> some View](shape/stroke(_:linewidth:).md)
  Traces the outline of this shape with a color or gradient.
- [func stroke<S>(S, lineWidth: CGFloat, antialiased: Bool) -> StrokeShapeView<Self, S, EmptyView>](shape/stroke(_:linewidth:antialiased:).md)
  Traces the outline of this shape with a color or gradient.
- [func stroke(lineWidth: CGFloat) -> some Shape](shape/stroke(linewidth:).md)
  Returns a new shape that is a stroked copy of `self` with line-width defined by `lineWidth` and all other properties of `StrokeStyle` having their default values.
- [func stroke<S>(S, style: StrokeStyle) -> some View](shape/stroke(_:style:).md)
  Traces the outline of this shape with a color or gradient.
- [func stroke<S>(S, style: StrokeStyle, antialiased: Bool) -> StrokeShapeView<Self, S, EmptyView>](shape/stroke(_:style:antialiased:).md)
  Traces the outline of this shape with a color or gradient.
- [func stroke(style: StrokeStyle) -> some Shape](shape/stroke(style:).md)
  Returns a new shape that is a stroked copy of `self`, using the contents of `style` to define the stroke characteristics.
### Filling a shape
- [func fill(_:style:)](shape/fill(_:style:).md)
  Fills this shape with a color or gradient.
- [func fill(style: FillStyle) -> some View](shape/fill(style:).md)
  Fills this shape with the foreground color.
### Setting the role
- [static var role: ShapeRole](shape/role.md)
  An indication of how to style a shape.
### Indicating a layout direction
- [var layoutDirectionBehavior: LayoutDirectionBehavior](shape/layoutdirectionbehavior.md)
  Returns the behavior this shape should use for different layout directions.
### Performing operations on a shape
- [func intersection<T>(T, eoFill: Bool) -> some Shape](shape/intersection(_:eofill:).md)
  Returns a new shape with filled regions common to both shapes.
- [func lineIntersection<T>(T, eoFill: Bool) -> some Shape](shape/lineintersection(_:eofill:).md)
  Returns a new shape with a line from this shape that overlaps the filled regions of the given shape.
- [func lineSubtraction<T>(T, eoFill: Bool) -> some Shape](shape/linesubtraction(_:eofill:).md)
  Returns a new shape with a line from this shape that does not overlap the filled region of the given shape.
- [func subtracting<T>(T, eoFill: Bool) -> some Shape](shape/subtracting(_:eofill:).md)
  Returns a new shape with filled regions from this shape that are not in the given shape.
- [func symmetricDifference<T>(T, eoFill: Bool) -> some Shape](shape/symmetricdifference(_:eofill:).md)
  Returns a new shape with filled regions either from this shape or the given shape, but not in both.
- [func union<T>(T, eoFill: Bool) -> some Shape](shape/union(_:eofill:).md)
  Returns a new shape with filled regions in either this shape or the given shape.
### Instance Methods
- [func size(CGSize, anchor: UnitPoint) -> some Shape](shape/size(_:anchor:).md)
  Returns a new version of self representing the same shape, but within a rect of `size` instead of the container size.
- [func size(width: CGFloat, height: CGFloat, anchor: UnitPoint) -> some Shape](shape/size(width:height:anchor:).md)
  Returns a new version of self representing the same shape, but within a rect of `(width, height)` instead of the container size.

## Relationships

### Inherits From
- [Animatable](animatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](view.md)
### Inherited By
- [InsettableShape](insettableshape.md)
### Conforming Types
- [AnyShape](anyshape.md)
- [ButtonBorderShape](buttonbordershape.md)
- [Capsule](capsule.md)
- [Circle](circle.md)
- [ContainerRelativeShape](containerrelativeshape.md)
- [Ellipse](ellipse.md)
- [OffsetShape](offsetshape.md)
- [Path](path.md)
- [Rectangle](rectangle.md)
- [RotatedShape](rotatedshape.md)
- [RoundedRectangle](roundedrectangle.md)
- [ScaledShape](scaledshape.md)
- [TransformedShape](transformedshape.md)
- [UnevenRoundedRectangle](unevenroundedrectangle.md)

## See Also

- [protocol ShapeView](shapeview.md)
  A view that provides a shape that you can use for drawing operations.
- [struct AnyShape](anyshape.md)
  A type-erased shape value.
- [enum ShapeRole](shaperole.md)
  Ways of styling a shape.
- [struct StrokeStyle](strokestyle.md)
  The characteristics of a stroke that traces a path.
- [struct StrokeShapeView](strokeshapeview.md)
  A shape provider that strokes its shape.
- [struct StrokeBorderShapeView](strokebordershapeview.md)
  A shape provider that strokes the border of its shape.
- [struct FillStyle](fillstyle.md)
  A style for rasterizing vector shapes.
- [struct FillShapeView](fillshapeview.md)
  A shape provider that fills its shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape)*