# Shapes

**Framework**: SwiftUI

Trace and fill built-in and custom shapes with a color, gradient, or other pattern.

#### Overview

Draw shapes like circles and rectangles, as well as custom paths that define shapes of your own design. Apply styles that include environment-aware colors, rich gradients, and material effects to the foreground, background, and outline of your shapes.

![None](https://docs-assets.developer.apple.com/published/b96b0c072d71e44a18d813a1b180ba9b/shapes-hero%402x.png)

If you need the efficiency or flexibility of immediate mode drawing — for example, to create particle effects — use a [`Canvas`](canvas.md) view instead.

## Topics

### Creating rectangular shapes
- [struct Rectangle](rectangle.md)
  A rectangular shape aligned inside the frame of the view containing it.
- [struct RoundedRectangle](roundedrectangle.md)
  A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [enum RoundedCornerStyle](roundedcornerstyle.md)
  Defines the shape of a rounded rectangle’s corners.
- [protocol RoundedRectangularShape](roundedrectangularshape.md)
  A protocol of [`InsettableShape`](insettableshape.md) that describes a rounded rectangular shape.
- [struct RoundedRectangularShapeCorners](roundedrectangularshapecorners.md)
  A type describing the corner styles of a [`RoundedRectangularShape`](roundedrectangularshape.md).
- [struct UnevenRoundedRectangle](unevenroundedrectangle.md)
  A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [struct RectangleCornerRadii](rectanglecornerradii.md)
  Describes the corner radius values of a rounded rectangle with uneven corners.
- [struct RectangleCornerInsets](rectanglecornerinsets.md)
  The inset sizes for the corners of a rectangle.
- [struct ConcentricRectangle](concentricrectangle.md)
  A shape that is replaced by a concentric version of the current container shape. If the container shape is a rectangle derived shape with four corners, this shape could choose to respect corners individually.
### Creating circular shapes
- [struct Circle](circle.md)
  A circle centered on the frame of the view containing it.
- [struct Ellipse](ellipse.md)
  An ellipse aligned inside the frame of the view containing it.
- [struct Capsule](capsule.md)
  A capsule shape aligned inside the frame of the view containing it.
### Drawing custom shapes
- [struct Path](path.md)
  The outline of a 2D shape.
### Defining shape behavior
- [protocol ShapeView](shapeview.md)
  A view that provides a shape that you can use for drawing operations.
- [protocol Shape](shape.md)
  A 2D shape that you can use when drawing a view.
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
### Transforming a shape
- [struct ScaledShape](scaledshape.md)
  A shape with a scale transform applied to it.
- [struct RotatedShape](rotatedshape.md)
  A shape with a rotation transform applied to it.
- [struct OffsetShape](offsetshape.md)
  A shape with a translation offset transform applied to it.
- [struct TransformedShape](transformedshape.md)
  A shape with an affine transform applied to it.
### Setting a container shape
- [func containerShape(_:)](view/containershape(_:).md)
  Sets the container shape to use for any container relative shape or concentric rectangle within this view.
- [protocol InsettableShape](insettableshape.md)
  A shape type that is able to inset itself to produce another shape.
- [struct ContainerRelativeShape](containerrelativeshape.md)
  A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.

## See Also

- [View fundamentals](view-fundamentals.md)
  Define the visual elements of your app using a hierarchy of views.
- [View configuration](view-configuration.md)
  Adjust the characteristics of views in a hierarchy.
- [View styles](view-styles.md)
  Apply built-in and custom appearances and behaviors to different types of views.
- [Animations](animations.md)
  Create smooth visual updates in response to state changes.
- [Text input and output](text-input-and-output.md)
  Display formatted text and get text input from the user.
- [Images](images.md)
  Add images and symbols to your app’s user interface.
- [Controls and indicators](controls-and-indicators.md)
  Display values and get user selections.
- [Menus and commands](menus-and-commands.md)
  Provide space-efficient, context-dependent access to commands and controls.
- [Drawing and graphics](drawing-and-graphics.md)
  Enhance your views with graphical effects and customized drawings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapes)*