# Chart3DContent

**Framework**: Swift Charts  
**Kind**: protocol  
**Role**: Protocol

A type that represents the three-dimensional content that you draw on a chart.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol Chart3DContent
```

## Topics

### Associated Types
- [associatedtype Body : Chart3DContent](./chart3dcontent/body-swift.associatedtype.md)
### Instance Properties
- [var body: Self.Body](./chart3dcontent/body-swift.property.md)
### Instance Methods
- [func foregroundStyle(some Chart3DSurfaceStyle) -> some Chart3DContent](./chart3dcontent/foregroundstyle%28_%29-1pjaq.md)
- [func foregroundStyle(some ShapeStyle) -> some Chart3DContent](./chart3dcontent/foregroundstyle%28_%29-7skde.md)
- [func foregroundStyle<D>(by: PlottableValue<D>) -> some Chart3DContent](./chart3dcontent/foregroundstyle%28by%29.md)
- [func metalness(Double) -> some Chart3DContent](./chart3dcontent/metalness%28_%29.md)
  A value that controls whether the surface has a metallic look.
- [func roughness(Double) -> some Chart3DContent](./chart3dcontent/roughness%28_%29.md)
  A value that controls the degree of surface roughness.
- [func symbol<S>(S) -> some Chart3DContent](./chart3dcontent/symbol%28_%29.md)
- [func symbolRotation(Rotation3D) -> some Chart3DContent](./chart3dcontent/symbolrotation%28_%29.md)
  Set the rotation of a 3D symbol.
- [func symbolSize(CGFloat) -> some Chart3DContent](./chart3dcontent/symbolsize%28_%29.md)

## Relationships

### Conforming Types
- [BuilderConditional](./builderconditional.md)
- [PointMark](./pointmark.md)
- [RectangleMark](./rectanglemark.md)
- [RuleMark](./rulemark.md)
- [SurfacePlot](./surfaceplot.md)

## See Also

### 3D charts
- [struct Chart3D](./chart3d.md)
  A SwiftUI view that displays interactive 3D charts and visualizations.
- [struct Chart3DContentBuilder](./chart3dcontentbuilder.md)
  A result builder that you use to compose the three-dimensional contents of a chart.
- [struct SurfacePlot](./surfaceplot.md)
  Chart content that represents a mathematical function of two variables using a 3D surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chart3dcontent)*