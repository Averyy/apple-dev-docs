# Graphics and rendering modifiers

**Framework**: SwiftUI

Affect the way the system draws a view, for example by scaling or masking a view, or by applying graphical effects.

#### Overview

Use these view modifiers to apply many of the rendering effects typically associated with a graphics context, like adding masks and creating composites. You can apply these effects to graphical views, like [`Shapes`](shapes.md), as well as any other SwiftUI view.

When you do need the flexibility of immediate mode drawing in a graphics context, use a [`Canvas`](canvas.md) view instead. This can be particularly helpful when you want to draw an extremely large number of dynamic shapes — for example, to create particle effects.

For more information about using these effects in your app, see [`Drawing and graphics`](drawing-and-graphics.md).

## Topics

### Masks and clipping
- [func mask<Mask>(alignment: Alignment, () -> Mask) -> some View](view/mask(alignment:_:).md)
  Masks this view using the alpha channel of the given view.
- [func clipped(antialiased: Bool) -> some View](view/clipped(antialiased:).md)
  Clips this view to its bounding rectangular frame.
- [func clipShape<S>(S, style: FillStyle) -> some View](view/clipshape(_:style:).md)
  Sets a clipping shape for this view.
- [func containerShape<T>(T) -> some View](view/containershape(_:).md)
  Sets the container shape to use for any container relative shape within this view.
### Scale
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
- [func imageScale(Image.Scale) -> some View](view/imagescale(_:).md)
  Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [func aspectRatio(_:contentMode:)](view/aspectratio(_:contentmode:).md)
  Constrains this view’s dimensions to the specified aspect ratio.
### Rotation and transformation
- [func rotationEffect(Angle, anchor: UnitPoint) -> some View](view/rotationeffect(_:anchor:).md)
  Rotates a view’s rendered output in two dimensions around the specified point.
- [func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View](view/rotation3deffect(_:anchor:).md)
  Rotates the view’s content by the specified 3D rotation value.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](view/rotation3deffect(_:axis:anchor:anchorz:perspective:).md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func rotation3DEffect(_:axis:anchor:)](view/rotation3deffect(_:axis:anchor:).md)
  Rotates the view’s content by an angle about an axis that you specify as a tuple of elements.
- [func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](view/perspectiverotationeffect(_:axis:anchor:anchorz:perspective:).md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func projectionEffect(ProjectionTransform) -> some View](view/projectioneffect(_:).md)
  Applies a projection transformation to this view’s rendered output.
- [func transformEffect(CGAffineTransform) -> some View](view/transformeffect(_:).md)
  Applies an affine transformation to this view’s rendered output.
- [func transform3DEffect(AffineTransform3D) -> some View](view/transform3deffect(_:).md)
  Applies a 3D transformation to this view’s rendered output.
### Graphical effects
- [func blur(radius: CGFloat, opaque: Bool) -> some View](view/blur(radius:opaque:).md)
  Applies a Gaussian blur to this view.
- [func opacity(Double) -> some View](view/opacity(_:).md)
  Sets the transparency of this view.
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
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some View](view/shadow(color:radius:x:y:).md)
  Adds a shadow to this view.
- [func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) -> some View](view/visualeffect(_:).md)
  Applies effects to this view, while providing access to layout information through a geometry proxy.
- [func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some VisualEffect) -> some View](view/visualeffect3d(_:).md)
  Applies effects to this view, while providing access to layout information through a 3D geometry proxy.
### Shaders
- [func colorEffect(Shader, isEnabled: Bool) -> some View](view/coloreffect(_:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a filter effect on the color of each pixel.
- [func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](view/distortioneffect(_:maxsampleoffset:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](view/layereffect(_:maxsampleoffset:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.
### Composites
- [func blendMode(BlendMode) -> some View](view/blendmode(_:).md)
  Sets the blend mode for compositing this view with overlapping views.
- [func compositingGroup() -> some View](view/compositinggroup.md)
  Wraps this view in a compositing group.
- [func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View](view/drawinggroup(opaque:colormode:).md)
  Composites this view’s contents into an offscreen image before final display.
### Animations
- [func animation(_:)](view/animation(_:).md)
  Applies the given animation to this view when this view changes.
- [func animation<V>(Animation?, value: V) -> some View](view/animation(_:value:).md)
  Applies the given animation to this view when the specified value changes.
- [func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) -> some View](view/animation(_:body:).md)
  Applies the given animation to all animatable values within the `body` closure.
- [func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](view/keyframeanimator(initialvalue:repeating:content:keyframes:).md)
  Loops the given keyframes continuously, updating the view using the modifiers you apply in `body`.
- [func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](view/keyframeanimator(initialvalue:trigger:content:keyframes:).md)
  Plays the given keyframes when the given trigger value changes, updating the view using the modifiers you apply in `body`.
- [func phaseAnimator<Phase>(some Sequence, content: (PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) -> Animation?) -> some View](view/phaseanimator(_:content:animation:).md)
  Animates effects that you apply to a view over a sequence of phases that change continuously.
- [func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content: (PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) -> Animation?) -> some View](view/phaseanimator(_:trigger:content:animation:).md)
  Animates effects that you apply to a view over a sequence of phases that change based on a trigger.
- [func contentTransition(ContentTransition) -> some View](view/contenttransition(_:).md)
  Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [func transition(_:)](view/transition(_:).md)
  Associates a transition with the view.
- [func transaction((inout Transaction) -> Void) -> some View](view/transaction(_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transaction(value: some Equatable, (inout Transaction) -> Void) -> some View](view/transaction(value:_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transaction<V>((inout Transaction) -> Void, body: (PlaceholderContentView<Self>) -> V) -> some View](view/transaction(_:body:).md)
  Applies the given transaction mutation function to all animations used within the `body` closure.
- [func contentTransition(ContentTransition) -> some View](view/contenttransition(_:).md)
  Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties: MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View](view/matchedgeometryeffect(id:in:properties:anchor:issource:).md)
  Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [func geometryGroup() -> some View](view/geometrygroup.md)
  Isolates the geometry (e.g. position and size) of the view from its parent view.

## See Also

- [Style modifiers](view-style-modifiers.md)
  Apply built-in styles to different types of views.
- [Layout modifiers](view-layout.md)
  Tell a view how to arrange itself within a view hierarchy by adjusting its size, position, alignment, padding, and so on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-graphics-and-rendering)*