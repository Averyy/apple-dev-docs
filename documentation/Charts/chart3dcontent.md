# Chart3DContent

**Framework**: Swift Charts  
**Kind**: protocol

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency protocol Chart3DContent
```

## Topics

### Associated Types
- [associatedtype Body : Chart3DContent](chart3dcontent/body-swift.associatedtype.md)
### Instance Properties
- [var body: Self.Body](chart3dcontent/body-swift.property.md)
### Instance Methods
- [func foregroundStyle(some Chart3DSurfaceStyle) -> some Chart3DContent](chart3dcontent/foregroundstyle(_:)-1pjaq.md)
- [func foregroundStyle(some ShapeStyle) -> some Chart3DContent](chart3dcontent/foregroundstyle(_:)-7skde.md)
- [func foregroundStyle<D>(by: PlottableValue<D>) -> some Chart3DContent](chart3dcontent/foregroundstyle(by:).md)
- [func metalness(Double) -> some Chart3DContent](chart3dcontent/metalness(_:).md)
  A value that controls whether the surface has a metallic look.
- [func roughness(Double) -> some Chart3DContent](chart3dcontent/roughness(_:).md)
  A value that controls the degree of surface roughness.
- [func symbol<S>(S) -> some Chart3DContent](chart3dcontent/symbol(_:).md)
- [func symbolRotation(Rotation3D) -> some Chart3DContent](chart3dcontent/symbolrotation(_:).md)
- [func symbolSize(CGFloat) -> some Chart3DContent](chart3dcontent/symbolsize(_:).md)

## Relationships

### Conforming Types
- [BuilderConditional](builderconditional.md)
- [PointMark](pointmark.md)
- [RectangleMark](rectanglemark.md)
- [RuleMark](rulemark.md)
- [SurfacePlot](surfaceplot.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chart3dcontent)*