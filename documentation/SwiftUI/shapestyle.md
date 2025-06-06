# ShapeStyle

**Framework**: SwiftUI  
**Kind**: protocol

A color or pattern to use when rendering a shape.

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
protocol ShapeStyle : Sendable
```

#### Overview

You create custom shape styles by declaring a type that conforms to the `ShapeStyle` protocol and implementing the required `resolve` function to return a shape style that represents the desired appearance based on the current environment.

For example this shape style reads the current color scheme from the environment to choose the blend mode its color will be composited with:

```swift
struct MyShapeStyle: ShapeStyle {
    func resolve(in environment: EnvironmentValues) -> some ShapeStyle {
        if environment.colorScheme == .light {
            return Color.red.blendMode(.lighten)
        } else {
            return Color.red.blendMode(.darken)
        }
    }
}
```

In addition to creating a custom shape style, you can also use one of the concrete styles that SwiftUI defines. To indicate a specific color or pattern, you can use [`Color`](color.md) or the style returned by [`image(_:sourceRect:scale:)`](shapestyle/image(_:sourcerect:scale:).md), or one of the gradient types, like the one returned by [`radialGradient(_:center:startRadius:endRadius:)`](shapestyle/radialgradient(_:center:startradius:endradius:).md). To set a color that’s appropriate for a given context on a given platform, use one of the semantic styles, like [`background`](shapestyle/background.md) or [`primary`](shapestyle/primary.md).

You can use a shape style by:

- Filling a shape with a style with the [`fill(_:style:)`](shape/fill(_:style:).md) modifier: ```swift
Path { path in
    path.move(to: .zero)
    path.addLine(to: CGPoint(x: 50, y: 0))
    path.addArc(
        center: .zero,
        radius: 50,
        startAngle: .zero,
        endAngle: .degrees(90),
        clockwise: false)
}
.fill(.radialGradient(
    Gradient(colors: [.yellow, .red]),
    center: .topLeading,
    startRadius: 15,
    endRadius: 80))
``` ![A screenshot of a quarter of a circle filled with](https://docs-assets.developer.apple.com/published/3785a0af3ac638892cc24860786c4049/ShapeStyle-1%402x.png)
- Tracing the outline of a shape with a style with either the [`stroke(_:lineWidth:)`](shape/stroke(_:linewidth:).md) or the [`stroke(_:style:)`](shape/stroke(_:style:).md) modifier: ```swift
RoundedRectangle(cornerRadius: 10)
    .stroke(.mint, lineWidth: 10)
    .frame(width: 200, height: 50)
``` ![A screenshot of a rounded rectangle, outlined in mint.](https://docs-assets.developer.apple.com/published/71f178536aa4724205ac12cbb26a0d81/ShapeStyle-2%402x.png)
- Styling the foreground elements in a view with the [`foregroundStyle(_:)`](view/foregroundstyle(_:).md) modifier: ```swift
VStack(alignment: .leading) {
    Text("Primary")
        .font(.title)
    Text("Secondary")
        .font(.caption)
        .foregroundStyle(.secondary)
}
``` ![A screenshot of a title in the primary content color above a](https://docs-assets.developer.apple.com/published/25e5e8427d277b3dcfcc1150ea5bc0d1/ShapeStyle-3%402x.png)

## Topics

### System colors
- [static var black: Color](shapestyle/black.md)
  A black color suitable for use in UI elements.
- [static var blue: Color](shapestyle/blue.md)
  A context-dependent blue color suitable for use in UI elements.
- [static var brown: Color](shapestyle/brown.md)
  A context-dependent brown color suitable for use in UI elements.
- [static var clear: Color](shapestyle/clear.md)
  A clear color suitable for use in UI elements.
- [static var cyan: Color](shapestyle/cyan.md)
  A context-dependent cyan color suitable for use in UI elements.
- [static var gray: Color](shapestyle/gray.md)
  A context-dependent gray color suitable for use in UI elements.
- [static var green: Color](shapestyle/green.md)
  A context-dependent green color suitable for use in UI elements.
- [static var indigo: Color](shapestyle/indigo.md)
  A context-dependent indigo color suitable for use in UI elements.
- [static var mint: Color](shapestyle/mint.md)
  A context-dependent mint color suitable for use in UI elements.
- [static var orange: Color](shapestyle/orange.md)
  A context-dependent orange color suitable for use in UI elements.
- [static var pink: Color](shapestyle/pink.md)
  A context-dependent pink color suitable for use in UI elements.
- [static var purple: Color](shapestyle/purple.md)
  A context-dependent purple color suitable for use in UI elements.
- [static var red: Color](shapestyle/red.md)
  A context-dependent red color suitable for use in UI elements.
- [static var teal: Color](shapestyle/teal.md)
  A context-dependent teal color suitable for use in UI elements.
- [static var white: Color](shapestyle/white.md)
  A white color suitable for use in UI elements.
- [static var yellow: Color](shapestyle/yellow.md)
  A context-dependent yellow color suitable for use in UI elements.
### Angular gradients
- [static angularGradient(_:center:startAngle:endAngle:)](shapestyle/angulargradient(_:center:startangle:endangle:).md)
  An angular gradient, which applies the color function as the angle changes between the start and end angles, and anchored to a relative center point within the filled shape.
- [static func angularGradient(colors: [Color], center: UnitPoint, startAngle: Angle, endAngle: Angle) -> AngularGradient](shapestyle/angulargradient(colors:center:startangle:endangle:).md)
  An angular gradient defined by a collection of colors.
- [static func angularGradient(stops: [Gradient.Stop], center: UnitPoint, startAngle: Angle, endAngle: Angle) -> AngularGradient](shapestyle/angulargradient(stops:center:startangle:endangle:).md)
  An angular gradient defined by a collection of color stops.
### Conic gradients
- [static conicGradient(_:center:angle:)](shapestyle/conicgradient(_:center:angle:).md)
  A conic gradient that completes a full turn, optionally starting from a given angle and anchored to a relative center point within the filled shape.
- [static func conicGradient(colors: [Color], center: UnitPoint, angle: Angle) -> AngularGradient](shapestyle/conicgradient(colors:center:angle:).md)
  A conic gradient defined by a collection of colors that completes a full turn.
- [static func conicGradient(stops: [Gradient.Stop], center: UnitPoint, angle: Angle) -> AngularGradient](shapestyle/conicgradient(stops:center:angle:).md)
  A conic gradient defined by a collection of color stops that completes a full turn.
### Elliptical gradients
- [static ellipticalGradient(_:center:startRadiusFraction:endRadiusFraction:)](shapestyle/ellipticalgradient(_:center:startradiusfraction:endradiusfraction:).md)
  A radial gradient that draws an ellipse.
- [static func ellipticalGradient(colors: [Color], center: UnitPoint, startRadiusFraction: CGFloat, endRadiusFraction: CGFloat) -> EllipticalGradient](shapestyle/ellipticalgradient(colors:center:startradiusfraction:endradiusfraction:).md)
  A radial gradient that draws an ellipse defined by a collection of colors.
- [static func ellipticalGradient(stops: [Gradient.Stop], center: UnitPoint, startRadiusFraction: CGFloat, endRadiusFraction: CGFloat) -> EllipticalGradient](shapestyle/ellipticalgradient(stops:center:startradiusfraction:endradiusfraction:).md)
  A radial gradient that draws an ellipse defined by a collection of color stops.
### Linear gradients
- [static linearGradient(_:startPoint:endPoint:)](shapestyle/lineargradient(_:startpoint:endpoint:).md)
  A linear gradient.
- [static func linearGradient(colors: [Color], startPoint: UnitPoint, endPoint: UnitPoint) -> LinearGradient](shapestyle/lineargradient(colors:startpoint:endpoint:).md)
  A linear gradient defined by a collection of colors.
- [static func linearGradient(stops: [Gradient.Stop], startPoint: UnitPoint, endPoint: UnitPoint) -> LinearGradient](shapestyle/lineargradient(stops:startpoint:endpoint:).md)
  A linear gradient defined by a collection of color stops.
### Radial gradients
- [static radialGradient(_:center:startRadius:endRadius:)](shapestyle/radialgradient(_:center:startradius:endradius:).md)
  A radial gradient.
- [static func radialGradient(colors: [Color], center: UnitPoint, startRadius: CGFloat, endRadius: CGFloat) -> RadialGradient](shapestyle/radialgradient(colors:center:startradius:endradius:).md)
  A radial gradient defined by a collection of colors.
- [static func radialGradient(stops: [Gradient.Stop], center: UnitPoint, startRadius: CGFloat, endRadius: CGFloat) -> RadialGradient](shapestyle/radialgradient(stops:center:startradius:endradius:).md)
  A radial gradient defined by a collection of color stops.
### Materials
- [static var ultraThinMaterial: Material](shapestyle/ultrathinmaterial.md)
  A mostly translucent material.
- [static var thinMaterial: Material](shapestyle/thinmaterial.md)
  A material that’s more translucent than opaque.
- [static var regularMaterial: Material](shapestyle/regularmaterial.md)
  A material that’s somewhat translucent.
- [static var thickMaterial: Material](shapestyle/thickmaterial.md)
  A material that’s more opaque than translucent.
- [static var ultraThickMaterial: Material](shapestyle/ultrathickmaterial.md)
  A mostly opaque material.
- [static var bar: Material](shapestyle/bar.md)
  A material matching the style of system toolbars.
### Image paint styles
- [static func image(Image, sourceRect: CGRect, scale: CGFloat) -> ImagePaint](shapestyle/image(_:sourcerect:scale:).md)
  A shape style that fills a shape by repeating a region of an image.
### Hierarchical styles
- [var secondary: some ShapeStyle](shapestyle/secondary-swift.property.md)
  Returns the second level of this shape style.
- [var tertiary: some ShapeStyle](shapestyle/tertiary-swift.property.md)
  Returns the third level of this shape style.
- [var quaternary: some ShapeStyle](shapestyle/quaternary-swift.property.md)
  Returns the fourth level of this shape style.
- [var quinary: some ShapeStyle](shapestyle/quinary-swift.property.md)
  Returns the fifth level of this shape style.
- [static var primary: HierarchicalShapeStyle](shapestyle/primary.md)
  A shape style that maps to the first level of the current content style.
- [static var secondary: HierarchicalShapeStyle](shapestyle/secondary-swift.type.property.md)
  A shape style that maps to the second level of the current content style.
- [static var tertiary: HierarchicalShapeStyle](shapestyle/tertiary-swift.type.property.md)
  A shape style that maps to the third level of the current content style.
- [static var quaternary: HierarchicalShapeStyle](shapestyle/quaternary-swift.type.property.md)
  A shape style that maps to the fourth level of the current content style.
- [static var quinary: HierarchicalShapeStyle](shapestyle/quinary-swift.type.property.md)
  A shape style that maps to the fifth level of the current content style.
### Semantic styles
- [static var foreground: ForegroundStyle](shapestyle/foreground.md)
  The foreground style in the current context.
- [static var background: BackgroundStyle](shapestyle/background.md)
  The background style in the current context.
- [static var selection: SelectionShapeStyle](shapestyle/selection.md)
  A style used to visually indicate selection following platform conventional colors and behaviors.
- [static var separator: SeparatorShapeStyle](shapestyle/separator.md)
  A style appropriate for foreground separator or border lines.
- [static var tint: TintShapeStyle](shapestyle/tint.md)
  A style that reflects the current tint color.
- [static var placeholder: PlaceholderTextShapeStyle](shapestyle/placeholder.md)
  A style appropriate for placeholder text.
- [static var link: LinkShapeStyle](shapestyle/link.md)
  A style appropriate for links.
- [static var fill: FillShapeStyle](shapestyle/fill.md)
  An overlay fill style for filling shapes.
- [static var windowBackground: WindowBackgroundShapeStyle](shapestyle/windowbackground.md)
  A style appropriate for elements that should match the background of their containing window.
### Modifying a shape style
- [func blendMode(BlendMode) -> some ShapeStyle](shapestyle/blendmode(_:)-swift.method.md)
  Returns a new style based on `self` that applies the specified blend mode when drawing.
- [func opacity(Double) -> some ShapeStyle](shapestyle/opacity(_:)-swift.method.md)
  Returns a new style based on `self` that multiplies by the specified opacity when drawing.
- [func shadow(ShadowStyle) -> some ShapeStyle](shapestyle/shadow(_:)-swift.method.md)
  Applies the specified shadow effect to the shape style.
### Configuring the default shape style
- [static func blendMode(BlendMode) -> some ShapeStyle](shapestyle/blendmode(_:)-swift.type.method.md)
  Returns a new style based on the current style that uses `mode` as its blend mode when drawing.
- [static func opacity(Double) -> some ShapeStyle](shapestyle/opacity(_:)-swift.type.method.md)
  Returns a new style based on the current style that multiplies by `opacity` when drawing.
- [static func shadow(ShadowStyle) -> some ShapeStyle](shapestyle/shadow(_:)-swift.type.method.md)
  Returns a shape style that applies the specified shadow style to the current style.
### Mapping to absolute coordinates
- [func `in`(CGRect) -> some ShapeStyle](shapestyle/in(_:).md)
  Maps a shape style’s unit-space coordinates to the absolute coordinates of a given rectangle.
### Resolving a shape style in an environment
- [func resolve(in: EnvironmentValues) -> Self.Resolved](shapestyle/resolve(in:).md)
  Evaluate to a resolved shape style given the current `environment`.
- [associatedtype Resolved : ShapeStyle = Never](shapestyle/resolved.md)
  The type of shape style this will resolve to.
### Using a shape style as a view
- [var body: _ShapeView<Rectangle, Self>](shapestyle/body.md)
  A rectangular view that’s filled with the shape style.
### Supporting types
- [struct AngularGradient](angulargradient.md)
  An angular gradient.
- [struct EllipticalGradient](ellipticalgradient.md)
  A radial gradient that draws an ellipse.
- [struct LinearGradient](lineargradient.md)
  A linear gradient.
- [struct RadialGradient](radialgradient.md)
  A radial gradient.
- [struct Material](material.md)
  A background material type.
- [struct ImagePaint](imagepaint.md)
  A shape style that fills a shape by repeating a region of an image.
- [struct HierarchicalShapeStyle](hierarchicalshapestyle.md)
  A shape style that maps to one of the numbered content styles.
- [struct HierarchicalShapeStyleModifier](hierarchicalshapestylemodifier.md)
  Styles that you can apply to hierarchical shapes.
- [struct ForegroundStyle](foregroundstyle.md)
  The foreground style in the current context.
- [struct BackgroundStyle](backgroundstyle.md)
  The background style in the current context.
- [struct SelectionShapeStyle](selectionshapestyle.md)
  A style used to visually indicate selection following platform conventional colors and behaviors.
- [struct SeparatorShapeStyle](separatorshapestyle.md)
  A style appropriate for foreground separator or border lines.
- [struct TintShapeStyle](tintshapestyle.md)
  A style that reflects the current tint color.
- [struct FillShapeStyle](fillshapestyle.md)
  A shape style that displays one of the overlay fills.
- [struct LinkShapeStyle](linkshapestyle.md)
  A style appropriate for links.
- [struct PlaceholderTextShapeStyle](placeholdertextshapestyle.md)
  A style appropriate for placeholder text.
- [struct WindowBackgroundShapeStyle](windowbackgroundshapestyle.md)
  A style appropriate for elements that should match the background of their containing window.
### Instance Methods
- [func materialActiveAppearance(MaterialActiveAppearance) -> some ShapeStyle](shapestyle/materialactiveappearance(_:).md)
  Sets an explicit active appearance for materials created by this style.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [AngularGradient](angulargradient.md)
- [AnyGradient](anygradient.md)
- [AnyShapeStyle](anyshapestyle.md)
- [BackgroundStyle](backgroundstyle.md)
- [Color](color.md)
- [Color.Resolved](color/resolved.md)
- [EllipticalGradient](ellipticalgradient.md)
- [FillShapeStyle](fillshapestyle.md)
- [ForegroundStyle](foregroundstyle.md)
- [Gradient](gradient.md)
- [HierarchicalShapeStyle](hierarchicalshapestyle.md)
- [HierarchicalShapeStyleModifier](hierarchicalshapestylemodifier.md)
- [ImagePaint](imagepaint.md)
- [LinearGradient](lineargradient.md)
- [LinkShapeStyle](linkshapestyle.md)
- [Material](material.md)
- [MeshGradient](meshgradient.md)
- [PlaceholderTextShapeStyle](placeholdertextshapestyle.md)
- [RadialGradient](radialgradient.md)
- [SelectionShapeStyle](selectionshapestyle.md)
- [SeparatorShapeStyle](separatorshapestyle.md)
- [Shader](shader.md)
- [TintShapeStyle](tintshapestyle.md)
- [WindowBackgroundShapeStyle](windowbackgroundshapestyle.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle)*