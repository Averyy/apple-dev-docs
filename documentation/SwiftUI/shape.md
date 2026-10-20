# Shape

**Framework**: SwiftUI  
**Kind**: protocol  
**Role**: Protocol

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
nonisolated
protocol Shape : Sendable, Animatable, View
```

#### Overview

Shapes without an explicit fill or stroke get a default fill based on the foreground color.

You can define shapes in relation to an implicit frame of reference, such as the natural size of the view that contains it. Alternatively, you can define shapes in terms of absolute coordinates.

## Topics

### Getting standard shapes
- [static var buttonBorder: ButtonBorderShape](./shape/buttonborder.md)
  A shape that defers to the environment to determine the resolved button border shape.
- [static var capsule: Capsule](./shape/capsule.md)
  A capsule shape aligned inside the frame of the view containing it.
- [static func capsule(style: RoundedCornerStyle) -> Self](./shape/capsule%28style%29.md)
  A capsule shape aligned inside the frame of the view containing it.
- [static var circle: Circle](./shape/circle.md)
  A circle centered on the frame of the view containing it.
- [static var containerRelative: ContainerRelativeShape](./shape/containerrelative.md)
  A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.
- [static var ellipse: Ellipse](./shape/ellipse.md)
  An ellipse aligned inside the frame of the view containing it.
- [static var textInputBorder: TextInputBorderShape](./shape/textinputborder.md)
  A shape that defers to the environment to determine the resolved text input border shape.
### Getting rectangles
- [static var rect: Rectangle](./shape/rect.md)
  A rectangular shape aligned inside the frame of the view containing it.
- [static func rect(cornerRadii: RectangleCornerRadii, style: RoundedCornerStyle) -> Self](./shape/rect%28cornerradii,style%29.md)
  A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [static func rect(cornerRadius: CGFloat, style: RoundedCornerStyle) -> Self](./shape/rect%28cornerradius,style%29.md)
  A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [static func rect(corners: Edge.Corner.Style, isUniform: Bool) -> Self](./shape/rect%28corners,isuniform%29.md)
  Creates a rectangle with the same corner style set on four corners.
- [static func rect(cornerSize: CGSize, style: RoundedCornerStyle) -> Self](./shape/rect%28cornersize,style%29.md)
  A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [static func rect(topLeadingCorner: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style, bottomLeadingCorner: Edge.Corner.Style, bottomTrailingCorner: Edge.Corner.Style) -> Self](./shape/rect%28topleadingcorner,toptrailingcorner,bottomleadingcorner,bottomtrailingcorner%29.md)
  Creates a rectangle with individual styles for each corner.
- [static func rect(topLeadingRadius: CGFloat, bottomLeadingRadius: CGFloat, bottomTrailingRadius: CGFloat, topTrailingRadius: CGFloat, style: RoundedCornerStyle) -> Self](./shape/rect%28topleadingradius,bottomleadingradius,bottomtrailingradius,toptrailingradius,style%29.md)
  A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [static func rect(uniformBottomCorners: Edge.Corner.Style, topLeadingCorner: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style) -> Self](./shape/rect%28uniformbottomcorners,topleadingcorner,toptrailingcorner%29.md)
  Creates a rectangle with a corner style set on the two bottom corners uniformly, and two other styles for the two top corners respectively.
- [static func rect(uniformLeadingCorners: Edge.Corner.Style, topTrailingCorner: Edge.Corner.Style, bottomTrailingCorner: Edge.Corner.Style) -> Self](./shape/rect%28uniformleadingcorners,toptrailingcorner,bottomtrailingcorner%29.md)
  Creates a rectangle with a corner style uniformly set on the two leading corners, and two other styles for the two trailing corners respectively.
- [static func rect(uniformLeadingCorners: Edge.Corner.Style, uniformTrailingCorners: Edge.Corner.Style) -> Self](./shape/rect%28uniformleadingcorners,uniformtrailingcorners%29.md)
  Creates a rectangle with a corner style uniformly set on the two leading corners, and another style uniformly set on the two trailing corners.
- [static func rect(uniformTopCorners: Edge.Corner.Style, bottomLeadingCorner: Edge.Corner.Style, bottomTrailingCorner: Edge.Corner.Style) -> Self](./shape/rect%28uniformtopcorners,bottomleadingcorner,bottomtrailingcorner%29.md)
  Creates a rectangle with a corner style uniformly set on the two top corners, and two other styles for the bottom two corners respectively.
- [static func rect(uniformTopCorners: Edge.Corner.Style, uniformBottomCorners: Edge.Corner.Style) -> Self](./shape/rect%28uniformtopcorners,uniformbottomcorners%29.md)
  Creates a rectangle with a corner style uniformly set on the two top corners, and another style uniformly set on the two bottom corners.
- [static func rect(uniformTrailingCorners: Edge.Corner.Style, topLeadingCorner: Edge.Corner.Style, bottomLeadingCorner: Edge.Corner.Style) -> Self](./shape/rect%28uniformtrailingcorners,topleadingcorner,bottomleadingcorner%29.md)
  Creates a rectangle with a corner style uniformly set on the two trailing corners, and two other styles for the two leading corners respectively.
### Defining a shape’s size and path
- [func sizeThatFits(ProposedViewSize) -> CGSize](./shape/sizethatfits%28_%29.md)
  Returns the size of the view that will render the shape, given a proposed size.
- [func path(in: CGRect) -> Path](./shape/path%28in%29.md)
  Describes this shape as a path within a rectangular frame of reference.
### Transforming a shape
- [func trim(from: CGFloat, to: CGFloat) -> some Shape](./shape/trim%28from,to%29.md)
  Trims this shape by a fractional amount based on its representation as a path.
- [func transform(CGAffineTransform) -> TransformedShape<Self>](./shape/transform%28_%29.md)
  Applies an affine transform to this shape.
- [func size(CGSize) -> some Shape](./shape/size%28_%29.md)
  Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of `size`. This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [func size(CGSize, anchor: UnitPoint) -> some Shape](./shape/size%28_,anchor%29.md)
  Returns a new version of self representing the same shape, but within a rect of `size` instead of the container size.
- [func size(width: CGFloat, height: CGFloat) -> some Shape](./shape/size%28width,height%29.md)
  Returns a new version of self representing the same shape, but that will ask it to create its path from a rect of size `(width, height)`. This does not affect the layout properties of any views created from the shape (e.g. by filling it).
- [func size(width: CGFloat, height: CGFloat, anchor: UnitPoint) -> some Shape](./shape/size%28width,height,anchor%29.md)
  Returns a new version of self representing the same shape, but within a rect of `(width, height)` instead of the container size.
- [func scale(CGFloat, anchor: UnitPoint) -> ScaledShape<Self>](./shape/scale%28_,anchor%29.md)
  Scales this shape without changing its bounding frame.
- [func scale(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> ScaledShape<Self>](./shape/scale%28x,y,anchor%29.md)
  Scales this shape without changing its bounding frame.
- [func rotation(Angle, anchor: UnitPoint) -> RotatedShape<Self>](./shape/rotation%28_,anchor%29.md)
  Rotates this shape around an anchor point at the angle you specify.
- [func offset(_:)](./shape/offset%28_%29.md)
  Changes the relative position of this shape using the specified point.
- [func offset(x: CGFloat, y: CGFloat) -> OffsetShape<Self>](./shape/offset%28x,y%29.md)
  Changes the relative position of this shape using the specified point.
### Setting the stroke characteristics
- [func stroke<S>(S, lineWidth: CGFloat) -> some View](./shape/stroke%28_,linewidth%29.md)
  Traces the outline of this shape with a color or gradient.
- [func stroke<S>(S, lineWidth: CGFloat, antialiased: Bool) -> StrokeShapeView<Self, S, EmptyView>](./shape/stroke%28_,linewidth,antialiased%29.md)
  Traces the outline of this shape with a color or gradient.
- [func stroke(lineWidth: CGFloat) -> some Shape](./shape/stroke%28linewidth%29.md)
  Returns a new shape that is a stroked copy of `self` with line-width defined by `lineWidth` and all other properties of `StrokeStyle` having their default values.
- [func stroke<S>(S, style: StrokeStyle) -> some View](./shape/stroke%28_,style%29.md)
  Traces the outline of this shape with a color or gradient.
- [func stroke<S>(S, style: StrokeStyle, antialiased: Bool) -> StrokeShapeView<Self, S, EmptyView>](./shape/stroke%28_,style,antialiased%29.md)
  Traces the outline of this shape with a color or gradient.
- [func stroke(style: StrokeStyle) -> some Shape](./shape/stroke%28style%29.md)
  Returns a new shape that is a stroked copy of `self`, using the contents of `style` to define the stroke characteristics.
### Filling a shape
- [func fill(_:style:)](./shape/fill%28_,style%29.md)
  Fills this shape with a color or gradient.
- [func fill(style: FillStyle) -> some View](./shape/fill%28style%29.md)
  Fills this shape with the foreground color.
### Setting the role
- [static var role: ShapeRole](./shape/role.md)
  An indication of how to style a shape.
### Indicating a layout direction
- [var layoutDirectionBehavior: LayoutDirectionBehavior](./shape/layoutdirectionbehavior.md)
  Returns the behavior this shape should use for different layout directions.
### Performing operations on a shape
- [func intersection<T>(T, eoFill: Bool) -> some Shape](./shape/intersection%28_,eofill%29.md)
  Returns a new shape with filled regions common to both shapes.
- [func lineIntersection<T>(T, eoFill: Bool) -> some Shape](./shape/lineintersection%28_,eofill%29.md)
  Returns a new shape with a line from this shape that overlaps the filled regions of the given shape.
- [func lineSubtraction<T>(T, eoFill: Bool) -> some Shape](./shape/linesubtraction%28_,eofill%29.md)
  Returns a new shape with a line from this shape that does not overlap the filled region of the given shape.
- [func subtracting<T>(T, eoFill: Bool) -> some Shape](./shape/subtracting%28_,eofill%29.md)
  Returns a new shape with filled regions from this shape that are not in the given shape.
- [func symmetricDifference<T>(T, eoFill: Bool) -> some Shape](./shape/symmetricdifference%28_,eofill%29.md)
  Returns a new shape with filled regions either from this shape or the given shape, but not in both.
- [func union<T>(T, eoFill: Bool) -> some Shape](./shape/union%28_,eofill%29.md)
  Returns a new shape with filled regions in either this shape or the given shape.

## Relationships

### Inherits From
- [Animatable](./animatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](./view.md)
### Inherited By
- [InsettableShape](./insettableshape.md)
- [RoundedRectangularShape](./roundedrectangularshape.md)
### Conforming Types
- [AnyShape](./anyshape.md)
- [ButtonBorderShape](./buttonbordershape.md)
- [Capsule](./capsule.md)
- [Circle](./circle.md)
- [ConcentricRectangle](./concentricrectangle.md)
- [ContainerRelativeShape](./containerrelativeshape.md)
- [DefaultGlassEffectShape](./defaultglasseffectshape.md)
- [Ellipse](./ellipse.md)
- [OffsetShape](./offsetshape.md)
- [Path](./path.md)
- [Rectangle](./rectangle.md)
- [RotatedShape](./rotatedshape.md)
- [RoundedRectangle](./roundedrectangle.md)
- [ScaledShape](./scaledshape.md)
- [TextInputBorderShape](./textinputbordershape.md)
- [TransformedShape](./transformedshape.md)
- [UnevenRoundedRectangle](./unevenroundedrectangle.md)

## See Also

### Defining shape behavior
- [protocol ShapeView](./shapeview.md)
  A view that provides a shape that you can use for drawing operations.
- [struct AnyShape](./anyshape.md)
  A type-erased shape value.
- [enum ShapeRole](./shaperole.md)
  Ways of styling a shape.
- [struct StrokeStyle](./strokestyle.md)
  The characteristics of a stroke that traces a path.
- [struct StrokeShapeView](./strokeshapeview.md)
  A shape provider that strokes its shape.
- [struct StrokeBorderShapeView](./strokebordershapeview.md)
  A shape provider that strokes the border of its shape.
- [struct FillStyle](./fillstyle.md)
  A style for rasterizing vector shapes.
- [struct FillShapeView](./fillshapeview.md)
  A shape provider that fills its shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape)*