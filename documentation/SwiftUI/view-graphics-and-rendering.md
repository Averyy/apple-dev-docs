# Graphics and rendering modifiers

**Framework**: SwiftUI  
**Role**: API Collection

Affect the way the system draws a view, for example by scaling or masking a view, or by applying graphical effects.

## Overview

Use these view modifiers to apply many of the rendering effects typically associated with a graphics context, like adding masks and creating composites. You can apply these effects to graphical views, like [Shapes](./shapes.md), as well as any other SwiftUI view.

When you do need the flexibility of immediate mode drawing in a graphics context, use a [`Canvas`](./canvas.md) view instead. This can be particularly helpful when you want to draw an extremely large number of dynamic shapes — for example, to create particle effects.

For more information about using these effects in your app, see [Drawing and graphics](./drawing-and-graphics.md).

## Topics

### Masks and clipping
- [func mask<Mask>(alignment: Alignment, () -> Mask) -> some View](./view/mask%28alignment,_%29.md)
  Masks this view using the alpha channel of the given view.
- [func clipped(antialiased: Bool) -> some View](./view/clipped%28antialiased%29.md)
  Clips this view to its bounding rectangular frame.
- [func clipShape<S>(S, style: FillStyle) -> some View](./view/clipshape%28_,style%29.md)
  Sets a clipping shape for this view.
- [func containerShape(_:)](./view/containershape%28_%29.md)
  Sets the container shape to use for any container relative shape or concentric rectangle within this view.
### Scale
- [func scaledToFill() -> some View](./view/scaledtofill%28%29.md)
  Scales this view to fill its parent.
- [func scaledToFill3D() -> some View](./view/scaledtofill3d%28%29.md)
  Scales this view to fill its parent.
- [func scaledToFit() -> some View](./view/scaledtofit%28%29.md)
  Scales this view to fit its parent.
- [func scaledToFit3D() -> some View](./view/scaledtofit3d%28%29.md)
  Scales this view to fit its parent.
- [func scaleEffect(_:anchor:)](./view/scaleeffect%28_,anchor%29.md)
  Scales this view uniformly by the specified factor, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View](./view/scaleeffect%28x,y,anchor%29.md)
  Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) -> some View](./view/scaleeffect%28x,y,z,anchor%29.md)
  Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
- [func imageScale(Image.Scale) -> some View](./view/imagescale%28_%29.md)
  Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [func aspectRatio(_:contentMode:)](./view/aspectratio%28_,contentmode%29.md)
  Constrains this view’s dimensions to the specified aspect ratio.
- [func aspectRatio3D(Size3D?, contentMode: ContentMode) -> some View](./view/aspectratio3d%28_,contentmode%29.md)
  Constrains this view’s dimensions to the specified 3D aspect ratio.
### Rotation and transformation
- [func rotationEffect(Angle, anchor: UnitPoint) -> some View](./view/rotationeffect%28_,anchor%29.md)
  Rotates a view’s rendered output in two dimensions around the specified point.
- [func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View](./view/rotation3deffect%28_,anchor%29.md)
  Rotates the view’s content by the specified 3D rotation value.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](./view/rotation3deffect%28_,axis,anchor,anchorz,perspective%29.md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func rotation3DEffect(_:axis:anchor:)](./view/rotation3deffect%28_,axis,anchor%29.md)
  Rotates the view’s content by an angle about an axis that you specify as a tuple of elements.
- [func rotation3DLayout(Rotation3D) -> some View](./view/rotation3dlayout%28_%29.md)
  Rotates a view with impacts to its frame in a containing layout
- [func rotation3DLayout(_:axis:)](./view/rotation3dlayout%28_,axis%29.md)
  Rotates a view with impacts to its frame in a containing layout
- [func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](./view/perspectiverotationeffect%28_,axis,anchor,anchorz,perspective%29.md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func projectionEffect(ProjectionTransform) -> some View](./view/projectioneffect%28_%29.md)
  Applies a projection transformation to this view’s rendered output.
- [func transformEffect(CGAffineTransform) -> some View](./view/transformeffect%28_%29.md)
  Applies an affine transformation to this view’s rendered output.
- [func transform3DEffect(AffineTransform3D) -> some View](./view/transform3deffect%28_%29.md)
  Applies a 3D transformation to this view’s rendered output.
### Graphical effects
- [func blur(radius: CGFloat, opaque: Bool) -> some View](./view/blur%28radius,opaque%29.md)
  Applies a Gaussian blur to this view.
- [func opacity(Double) -> some View](./view/opacity%28_%29.md)
  Sets the transparency of this view.
- [func brightness(Double) -> some View](./view/brightness%28_%29.md)
  Brightens this view by the specified amount.
- [func contrast(Double) -> some View](./view/contrast%28_%29.md)
  Sets the contrast and separation between similar colors in this view.
- [func colorInvert() -> some View](./view/colorinvert%28%29.md)
  Inverts the colors in this view.
- [func colorMultiply(Color) -> some View](./view/colormultiply%28_%29.md)
  Adds a color multiplication effect to this view.
- [func saturation(Double) -> some View](./view/saturation%28_%29.md)
  Adjusts the color saturation of this view.
- [func grayscale(Double) -> some View](./view/grayscale%28_%29.md)
  Adds a grayscale effect to this view.
- [func hueRotation(Angle) -> some View](./view/huerotation%28_%29.md)
  Applies a hue rotation effect to this view.
- [func luminanceToAlpha() -> some View](./view/luminancetoalpha%28%29.md)
  Adds a luminance to alpha effect to this view.
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some View](./view/shadow%28color,radius,x,y%29.md)
  Adds a shadow to this view.
- [func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) -> some View](./view/visualeffect%28_%29.md)
  Applies effects to this view, while providing access to layout information through a geometry proxy.
- [func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some VisualEffect) -> some View](./view/visualeffect3d%28_%29.md)
  Applies effects to this view, while providing access to layout information through a 3D geometry proxy.
- [func materialActiveAppearance(MaterialActiveAppearance) -> some View](./view/materialactiveappearance%28_%29.md)
  Sets an explicit active appearance for materials in this view.
### Shaders
- [func colorEffect(Shader, isEnabled: Bool) -> some View](./view/coloreffect%28_,isenabled%29.md)
  Returns a new view that applies `shader` to `self` as a filter effect on the color of each pixel.
- [func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](./view/distortioneffect%28_,maxsampleoffset,isenabled%29.md)
  Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](./view/layereffect%28_,maxsampleoffset,isenabled%29.md)
  Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.
### Composites
- [func blendMode(BlendMode) -> some View](./view/blendmode%28_%29.md)
  Sets the blend mode for compositing this view with overlapping views.
- [func compositingGroup() -> some View](./view/compositinggroup%28%29.md)
  Wraps this view in a compositing group.
- [func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View](./view/drawinggroup%28opaque,colormode%29.md)
  Composites this view’s contents into an offscreen image before final display.
### Animations
- [func animation<V>(Animation?, value: V) -> some View](./view/animation%28_,value%29.md)
  Applies the given animation to this view when the specified value changes.
- [func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) -> some View](./view/animation%28_,body%29.md)
  Applies the given animation to all animatable values within the `body` closure.
- [func contentTransition(ContentTransition) -> some View](./view/contenttransition%28_%29.md)
  Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [func geometryGroup() -> some View](./view/geometrygroup%28%29.md)
  Isolates the geometry (e.g. position and size) of the view from its parent view.
- [func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](./view/keyframeanimator%28initialvalue,repeating,content,keyframes%29.md)
  Loops the given keyframes continuously, updating the view using the modifiers you apply in `body`.
- [func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](./view/keyframeanimator%28initialvalue,trigger,content,keyframes%29.md)
  Plays the given keyframes when the given trigger value changes, updating the view using the modifiers you apply in `body`.
- [func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties: MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View](./view/matchedgeometryeffect%28id,in,properties,anchor,issource%29.md)
  Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID) -> some View](./view/matchedtransitionsource%28id,in%29.md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID, configuration: (EmptyMatchedTransitionSourceConfiguration) -> some MatchedTransitionSourceConfiguration) -> some View](./view/matchedtransitionsource%28id,in,configuration%29.md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func phaseAnimator<Phase>(some Sequence, content: (PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) -> Animation?) -> some View](./view/phaseanimator%28_,content,animation%29.md)
  Animates effects that you apply to a view over a sequence of phases that change continuously.
- [func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content: (PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) -> Animation?) -> some View](./view/phaseanimator%28_,trigger,content,animation%29.md)
  Animates effects that you apply to a view over a sequence of phases that change based on a trigger.
- [func transition(_:)](./view/transition%28_%29.md)
  Associates a transition with the view.
- [func transaction((inout Transaction) -> Void) -> some View](./view/transaction%28_%29.md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transaction(value: some Equatable, (inout Transaction) -> Void) -> some View](./view/transaction%28value,_%29.md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transaction<V>((inout Transaction) -> Void, body: (PlaceholderContentView<Self>) -> V) -> some View](./view/transaction%28_,body%29.md)
  Applies the given transaction mutation function to all animations used within the `body` closure.
- [func animation(_:)](./view/animation%28_%29.md)
  Applies the given animation to this view when this view changes.

## See Also

### Drawing views
- [Style modifiers](./view-style-modifiers.md)
  Apply built-in styles to different types of views.
- [Layout modifiers](./view-layout.md)
  Tell a view how to arrange itself within a view hierarchy by adjusting its size, position, alignment, padding, and so on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-graphics-and-rendering)*