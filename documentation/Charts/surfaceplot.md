# SurfacePlot

**Framework**: Swift Charts  
**Kind**: struct

Chart content that represents a mathematical function of two variables using a 3D surface.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency struct SurfacePlot
```

#### Overview

Use `SurfacePlot` to visualize a 3D surface for functions of the form `y = f(x, z)`

#### Overview

To create a `SurfacePlot`, provide a closure that takes `x` and `z` values as input and returns a `y` value. For example, to draw the function `y = sin(2 * x) * cos(2 * z)`, you write:

```swift
Chart3D {
    SurfacePlot(x: "x", y: "y", z: "z") { x, z in
        sin(2 * x) * cos(2 * z)
    }
    .foregroundStyle(.heightBased)
}
.chartXScale(domain: -2...2)
.chartYScale(domain: -1...1)
.chartZScale(domain: -2...2)
```

You can also explicitly define the plotting space of your `Chart3D` using the `Chart/chartXScale(domain:range:type:)->View`, `Chart/chartYScale(domain:range:type:)->View`, and `Chart/chartYScale(domain:range:type:)->View` modifiers.

#### Styling the Surface

You can style the surface using standard Swift Charts modifiers like `foregroundStyle(_:)-(Chart3DSurfaceStyle)->Chart3DContent`. You may find this useful for Charts that contain more than one `SurfacePlot`. A common and effective style for surfaces is [`heightBased`](chart3dsurfacestyle/heightbased.md), which creates a gradient using colors based on the y-value of your surface, making it easier to perceive its shape. You can also use [`normalBased`](chart3dsurfacestyle/normalbased.md) to color points on the `SurfacePlot` based on the direction that it is facing.

```swift
Chart3D {
    SurfacePlot(x: "x", y: "y", z: "z") { x, z in
        sin(2 * x) * cos(2 * z) * 0.5
    }
    .foregroundStyle(.heightBased)

    SurfacePlot(x: "x", y: "y", z: "z") { x, z in
        sin(4 * x) * cos(4 * z) * 0.2 - 1
    }
    .foregroundStyle(.normalBased)
}
.chartXScale(domain: -2...2)
.chartYScale(domain: -1.5...1)
.chartZScale(domain: -2...2)
```

Chart content that represents a collection of data using three-dimensional data.

## Topics

### Initializers
- [init(x: Text, y: Text, z: Text, function: (Double, Double) -> Double)](surfaceplot/init(x:y:z:function:)-2dqgp.md)
  Creates a SurfacePlot that represents a function y = f(x, z).
- [init(x: LocalizedStringKey, y: LocalizedStringKey, z: LocalizedStringKey, function: (Double, Double) -> Double)](surfaceplot/init(x:y:z:function:)-6c5e6.md)
  Creates a SurfacePlot that represents a function y = f(x, z).
- [init(x: LocalizedStringResource, y: LocalizedStringResource, z: LocalizedStringResource, function: (Double, Double) -> Double)](surfaceplot/init(x:y:z:function:)-8mf5t.md)
  Creates a SurfacePlot that represents a function y = f(x, z).
- [init(x: some StringProtocol, y: some StringProtocol, z: some StringProtocol, function: (Double, Double) -> Double)](surfaceplot/init(x:y:z:function:)-9xdw2.md)
  Creates a SurfacePlot that represents a function y = f(x, z).

## Relationships

### Conforms To
- [Chart3DContent](chart3dcontent.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Chart3D](chart3d.md)
  A SwiftUI view that displays interactive 3D charts and visualizations.
- [protocol Chart3DContent](chart3dcontent.md)
  A type that represents the three-dimensional content that you draw on a chart.
- [struct Chart3DContentBuilder](chart3dcontentbuilder.md)
  A result builder that you use to compose the three-dimensional contents of a chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/surfaceplot)*