# MeshGradient

**Framework**: SwiftUI  
**Kind**: struct

A two-dimensional gradient defined by a 2D grid of positioned colors.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct MeshGradient
```

#### Overview

Each vertex has a position, a color and four surrounding Bezier control points (leading, top, trailing, bottom) that define the tangents connecting the vertex with its four neighboring vertices. (Vertices on the corners or edges of the mesh have less than four neighbors, they ignore their extra control points.) Control points may either be specified explicitly or implicitly.

When rendering, a tessellated sequence of Bezier patches are created, and vertex colors are interpolated across each patch, either linearly, or via another set of cubic curves derived from how the colors change between neighbors – the latter typically gives smoother color transitions.

```swift
MeshGradient(width: 3, height: 3, points: [
    .init(0, 0), .init(0.5, 0), .init(1, 0),
    .init(0, 0.5), .init(0.5, 0.5), .init(1, 0.5),
    .init(0, 1), .init(0.5, 1), .init(1, 1)
], colors: [
    .red, .purple, .indigo,
    .orange, .white, .blue,
    .yellow, .green, .mint
])
```

## Topics

### Structures
- [MeshGradient.BezierPoint](meshgradient/bezierpoint.md)
  One location in a gradient mesh, along with the four Bezier control points surrounding it.
### Initializers
- [init(width: Int, height: Int, bezierPoints: [MeshGradient.BezierPoint], colors: [Color], background: Color, smoothsColors: Bool, colorSpace: Gradient.ColorSpace)](meshgradient/init(width:height:bezierpoints:colors:background:smoothscolors:colorspace:).md)
  Creates a new gradient mesh specified as a 2D grid of colored points, specifying the Bezier control points explicitly.
- [init(width: Int, height: Int, bezierPoints: [MeshGradient.BezierPoint], resolvedColors: [Color.Resolved], background: Color, smoothsColors: Bool, colorSpace: Gradient.ColorSpace)](meshgradient/init(width:height:bezierpoints:resolvedcolors:background:smoothscolors:colorspace:).md)
  Creates a new gradient mesh specified as a 2D grid of colored points, specifying the Bezier control points explicitly, with already-resolved sRGB colors.
- [init(width: Int, height: Int, locations: MeshGradient.Locations, colors: MeshGradient.Colors, background: Color, smoothsColors: Bool, colorSpace: Gradient.ColorSpace)](meshgradient/init(width:height:locations:colors:background:smoothscolors:colorspace:).md)
  Creates a new gradient mesh specified as a 2D grid of colored vertices.
- [init(width: Int, height: Int, points: [SIMD2<Float>], colors: [Color], background: Color, smoothsColors: Bool, colorSpace: Gradient.ColorSpace)](meshgradient/init(width:height:points:colors:background:smoothscolors:colorspace:).md)
  Creates a new gradient mesh specified as a 2D grid of colored points.
- [init(width: Int, height: Int, points: [SIMD2<Float>], resolvedColors: [Color.Resolved], background: Color, smoothsColors: Bool, colorSpace: Gradient.ColorSpace)](meshgradient/init(width:height:points:resolvedcolors:background:smoothscolors:colorspace:).md)
  Creates a new gradient mesh specified as a 2D grid of colored points, with already-resolved sRGB colors.
### Instance Properties
- [var background: Color](meshgradient/background.md)
  The background color, this fills any points outside the defined vertex mesh.
- [var colorSpace: Gradient.ColorSpace](meshgradient/colorspace.md)
  The color space in which to interpolate vertex colors.
- [var colors: MeshGradient.Colors](meshgradient/colors-swift.property.md)
  The array of colors. Must contain `width x height` elements.
- [var height: Int](meshgradient/height.md)
  The height of the mesh, i.e. the number of vertices per column.
- [var locations: MeshGradient.Locations](meshgradient/locations-swift.property.md)
  The array of locations. Must contain `width x height` elements.
- [var smoothsColors: Bool](meshgradient/smoothscolors.md)
  Whether cubic (smooth) interpolation should be used for the colors in the mesh (rather than only for the shape of the mesh).
- [var width: Int](meshgradient/width.md)
  The width of the mesh, i.e. the number of vertices per row.
### Enumerations
- [MeshGradient.Colors](meshgradient/colors-swift.enum.md)
  An array of colors.
- [MeshGradient.Locations](meshgradient/locations-swift.enum.md)
  An array of 2D locations and their control points.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [ShapeStyle](shapestyle.md)
- [View](view.md)

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
- [protocol ShapeStyle](shapestyle.md)
  A color or pattern to use when rendering a shape.
- [struct AnyShapeStyle](anyshapestyle.md)
  A type-erased ShapeStyle value.
- [struct Gradient](gradient.md)
  A color gradient represented as an array of color stops, each having a parametric location value.
- [struct AnyGradient](anygradient.md)
  A color gradient.
- [struct ShadowStyle](shadowstyle.md)
  A style to use when rendering shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/meshgradient)*