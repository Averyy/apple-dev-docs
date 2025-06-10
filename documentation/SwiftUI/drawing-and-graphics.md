# Drawing and graphics

**Framework**: SwiftUI

Enhance your views with graphical effects and customized drawings.

#### Overview

You create rich, dynamic user interfaces with the built-in views and [`Shapes`](shapes.md) that SwiftUI provides. To enhance any view, you can apply many of the graphical effects typically associated with a graphics context, like setting colors, adding masks, and creating composites.

![None](https://docs-assets.developer.apple.com/published/80221e0a7ef63e2fa17f92780533bf94/drawing-and-graphics-hero%402x.png)

When you need the flexibility of immediate mode drawing in a graphics context, use a [`Canvas`](canvas.md) view. This can be particularly helpful when you want to draw an extremely large number of dynamic shapes — for example, to create particle effects.

For design guidance, see [`Materials`](https://developer.apple.com/design/Human-Interface-Guidelines/materials) and [`Color`](https://developer.apple.com/design/Human-Interface-Guidelines/color) in the Human Interface Guidelines.

## Topics

### Immediate mode drawing
- [Add Rich Graphics to Your SwiftUI App](add_rich_graphics_to_your_swiftui_app.md)
  Make your apps stand out by adding background materials, vibrancy, custom graphics, and animations.
- [struct Canvas](canvas.md)
  A view type that supports immediate mode drawing.
- [struct GraphicsContext](graphicscontext.md)
  An immediate mode drawing destination, and its current state.
### Setting a color
- [func tint(_:)](view/tint(_:).md)
  Sets the tint color within this view.
- [struct Color](color.md)
  A representation of a color that adapts to a given context.
### Styling content
- [func border<S>(S, width: CGFloat) -> some View](view/border(_:width:).md)
  Adds a border to this view with the specified style and width.
- [func foregroundStyle<S>(S) -> some View](view/foregroundstyle(_:).md)
  Sets a view’s foreground elements to use a given style.
- [func foregroundStyle<S1, S2>(S1, S2) -> some View](view/foregroundstyle(_:_:).md)
  Sets the primary and secondary levels of the foreground style in the child view.
- [func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View](view/foregroundstyle(_:_:_:).md)
  Sets the primary, secondary, and tertiary levels of the foreground style.
- [func backgroundStyle<S>(S) -> some View](view/backgroundstyle(_:).md)
  Sets the specified style to render backgrounds within the view.
- [var backgroundStyle: AnyShapeStyle?](environmentvalues/backgroundstyle.md)
  An optional style that overrides the default system background style when set.
- [protocol ShapeStyle](shapestyle.md)
  A color or pattern to use when rendering a shape.
- [struct AnyShapeStyle](anyshapestyle.md)
  A type-erased ShapeStyle value.
- [struct Gradient](gradient.md)
  A color gradient represented as an array of color stops, each having a parametric location value.
- [struct MeshGradient](meshgradient.md)
  A two-dimensional gradient defined by a 2D grid of positioned colors.
- [struct AnyGradient](anygradient.md)
  A color gradient.
- [struct ShadowStyle](shadowstyle.md)
  A style to use when rendering shadows.
- [struct Glass](glass.md)
  A structure that defines the configuration of the Liquid Glass material.
### Transforming colors
- [func brightness(Double) -> some View](view/brightness(_:).md)
  Brightens this view by the specified amount.
- [func contrast(Double) -> some View](view/contrast(_:).md)
  Sets the contrast and separation between similar colors in this view.
- [func colorInvert() -> some View](view/colorinvert.md)
  Inverts the colors in this view.
- [func colorMultiply(Color) -> some View](view/colormultiply(_:).md)
  Adds a color multiplication effect to this view.
- [func saturation(Double) -> some View](view/saturation(_:).md)
  Adjusts the color saturation of this view.
- [func grayscale(Double) -> some View](view/grayscale(_:).md)
  Adds a grayscale effect to this view.
- [func hueRotation(Angle) -> some View](view/huerotation(_:).md)
  Applies a hue rotation effect to this view.
- [func luminanceToAlpha() -> some View](view/luminancetoalpha.md)
  Adds a luminance to alpha effect to this view.
- [func materialActiveAppearance(MaterialActiveAppearance) -> some View](view/materialactiveappearance(_:).md)
  Sets an explicit active appearance for materials in this view.
- [var materialActiveAppearance: MaterialActiveAppearance](environmentvalues/materialactiveappearance.md)
  The behavior materials should use for their active state, defaulting to `automatic`.
- [struct MaterialActiveAppearance](materialactiveappearance.md)
  The behavior for how materials appear active and inactive.
### Scaling, rotating, or transforming a view
- [func scaledToFill() -> some View](view/scaledtofill.md)
  Scales this view to fill its parent.
- [func scaledToFit() -> some View](view/scaledtofit.md)
  Scales this view to fit its parent.
- [func scaleEffect(_:anchor:)](view/scaleeffect(_:anchor:).md)
  Scales this view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View](view/scaleeffect(x:y:anchor:).md)
  Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) -> some View](view/scaleeffect(x:y:z:anchor:).md)
  Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
- [func aspectRatio(_:contentMode:)](view/aspectratio(_:contentmode:).md)
  Constrains this view’s dimensions to the specified aspect ratio.
- [func rotationEffect(Angle, anchor: UnitPoint) -> some View](view/rotationeffect(_:anchor:).md)
  Rotates a view’s rendered output in two dimensions around the specified point.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](view/rotation3deffect(_:axis:anchor:anchorz:perspective:).md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](view/perspectiverotationeffect(_:axis:anchor:anchorz:perspective:).md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View](view/rotation3deffect(_:anchor:).md)
  Rotates the view’s content by the specified 3D rotation value.
- [func rotation3DEffect(_:axis:anchor:)](view/rotation3deffect(_:axis:anchor:).md)
  Rotates the view’s content by an angle about an axis that you specify as a tuple of elements.
- [func transformEffect(CGAffineTransform) -> some View](view/transformeffect(_:).md)
  Applies an affine transformation to this view’s rendered output.
- [func transform3DEffect(AffineTransform3D) -> some View](view/transform3deffect(_:).md)
  Applies a 3D transformation to this view’s rendered output.
- [func projectionEffect(ProjectionTransform) -> some View](view/projectioneffect(_:).md)
  Applies a projection transformation to this view’s rendered output.
- [struct ProjectionTransform](projectiontransform.md)
- [enum ContentMode](contentmode.md)
  Constants that define how a view’s content fills the available space.
### Masking and clipping
- [func mask<Mask>(alignment: Alignment, () -> Mask) -> some View](view/mask(alignment:_:).md)
  Masks this view using the alpha channel of the given view.
- [func clipped(antialiased: Bool) -> some View](view/clipped(antialiased:).md)
  Clips this view to its bounding rectangular frame.
- [func clipShape<S>(S, style: FillStyle) -> some View](view/clipshape(_:style:).md)
  Sets a clipping shape for this view.
### Applying blur and shadows
- [func blur(radius: CGFloat, opaque: Bool) -> some View](view/blur(radius:opaque:).md)
  Applies a Gaussian blur to this view.
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some View](view/shadow(color:radius:x:y:).md)
  Adds a shadow to this view.
- [struct ColorMatrix](colormatrix.md)
  A matrix to use in an RGBA color transformation.
### Applying effects based on geometry
- [func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) -> some View](view/visualeffect(_:).md)
  Applies effects to this view, while providing access to layout information through a geometry proxy.
- [func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some VisualEffect) -> some View](view/visualeffect3d(_:).md)
  Applies effects to this view, while providing access to layout information through a 3D geometry proxy.
- [protocol VisualEffect](visualeffect.md)
  Visual Effects change the visual appearance of a view without changing its ancestors or descendents.
- [struct EmptyVisualEffect](emptyvisualeffect.md)
  The base visual effect that you apply additional effect to.
### Compositing views
- [func blendMode(BlendMode) -> some View](view/blendmode(_:).md)
  Sets the blend mode for compositing this view with overlapping views.
- [func compositingGroup() -> some View](view/compositinggroup.md)
  Wraps this view in a compositing group.
- [func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View](view/drawinggroup(opaque:colormode:).md)
  Composites this view’s contents into an offscreen image before final display.
- [enum BlendMode](blendmode.md)
  Modes for compositing a view with overlapping content.
- [enum ColorRenderingMode](colorrenderingmode.md)
  The set of possible working color spaces for color-compositing operations.
- [protocol CompositorContent](compositorcontent.md)
- [struct CompositorContentBuilder](compositorcontentbuilder.md)
  A result builder for composing a collection of [`CompositorContent`](compositorcontent.md) elements.
### Measuring a view
- [struct GeometryReader](geometryreader.md)
  A container view that defines its content as a function of its own size and coordinate space.
- [struct GeometryReader3D](geometryreader3d.md)
  A container view that defines its content as a function of its own size and coordinate space.
- [struct GeometryProxy](geometryproxy.md)
  A proxy for access to the size and coordinate space (for anchor resolution) of the container view.
- [struct GeometryProxy3D](geometryproxy3d.md)
  A proxy for access to the size and coordinate space of the container view.
- [func coordinateSpace(NamedCoordinateSpace) -> some View](view/coordinatespace(_:).md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [enum CoordinateSpace](coordinatespace.md)
  A resolved coordinate space created by the coordinate space protocol.
- [protocol CoordinateSpaceProtocol](coordinatespaceprotocol.md)
  A frame of reference within the layout system.
- [struct PhysicalMetric](physicalmetric.md)
  Provides access to a value in points that corresponds to the specified physical measurement.
- [struct PhysicalMetricsConverter](physicalmetricsconverter.md)
  A physical metrics converter provides conversion between point values and their extent in 3D space, in the form of physical length measurements.
### Responding to a geometry change
- [func onGeometryChange(for:of:action:)](view/ongeometrychange(for:of:action:).md)
  Adds an action to be performed when a value, created from a geometry proxy, changes.
### Accessing Metal shaders
- [func colorEffect(Shader, isEnabled: Bool) -> some View](view/coloreffect(_:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a filter effect on the color of each pixel.
- [func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](view/distortioneffect(_:maxsampleoffset:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](view/layereffect(_:maxsampleoffset:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.
- [struct Shader](shader.md)
  A reference to a function in a Metal shader library, along with its bound uniform argument values.
- [struct ShaderFunction](shaderfunction.md)
  A reference to a function in a Metal shader library.
- [struct ShaderLibrary](shaderlibrary.md)
  A Metal shader library.
### Accessing geometric constructs
- [enum Axis](axis.md)
  The horizontal or vertical dimension in a 2D coordinate system.
- [struct Angle](angle.md)
  A geometric angle whose value you access in either radians or degrees.
- [struct UnitPoint](unitpoint.md)
  A normalized 2D point in a view’s coordinate space.
- [struct UnitPoint3D](unitpoint3d.md)
  A normalized 3D point in a view’s coordinate space.
- [struct Anchor](anchor.md)
  An opaque value derived from an anchor source and a particular view.
- [protocol DepthAlignmentID](depthalignmentid.md)
- [struct Alignment3D](alignment3d.md)
  An alignment in all three axes.
- [struct GeometryProxyCoordinateSpace3D](geometryproxycoordinatespace3d.md)
  A representation of a `GeometryProxy3D` which can be used for `CoordinateSpace3D` based conversions.

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
- [Shapes](shapes.md)
  Trace and fill built-in and custom shapes with a color, gradient, or other pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/drawing-and-graphics)*