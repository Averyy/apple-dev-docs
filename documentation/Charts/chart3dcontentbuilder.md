# Chart3DContentBuilder

**Framework**: Swift Charts  
**Kind**: struct

A result builder that you use to compose the three-dimensional contents of a chart.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@resultBuilder
struct Chart3DContentBuilder
```

## Topics

### Type Methods
- [static func buildBlock() -> some Chart3DContent](chart3dcontentbuilder/buildblock.md)
- [static func buildBlock<Content>(Content) -> Content](chart3dcontentbuilder/buildblock(_:)-7r61g.md)
- [static func buildBlock<each Content>(repeat each Content) -> some Chart3DContent](chart3dcontentbuilder/buildblock(_:)-ny3i.md)
- [static func buildEither<C1, C2>(first: C1) -> BuilderConditional<C1, C2>](chart3dcontentbuilder/buildeither(first:).md)
- [static func buildEither<C1, C2>(second: C2) -> BuilderConditional<C1, C2>](chart3dcontentbuilder/buildeither(second:).md)
- [static func buildExpression<Content>(Content) -> Content](chart3dcontentbuilder/buildexpression(_:).md)
- [static func buildLimitedAvailability<Content>(Content) -> some Chart3DContent](chart3dcontentbuilder/buildlimitedavailability(_:).md)
- [static func buildOptional<Content>(Content) -> Content](chart3dcontentbuilder/buildoptional(_:).md)

## See Also

- [struct Chart3D](chart3d.md)
  A SwiftUI view that displays interactive 3D charts and visualizations.
- [protocol Chart3DContent](chart3dcontent.md)
  A type that represents the three-dimensional content that you draw on a chart.
- [struct SurfacePlot](surfaceplot.md)
  Chart content that represents a mathematical function of two variables using a 3D surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chart3dcontentbuilder)*