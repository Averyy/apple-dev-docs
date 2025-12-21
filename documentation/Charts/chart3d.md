# Chart3D

**Framework**: Swift Charts  
**Kind**: struct

A SwiftUI view that displays interactive 3D charts and visualizations.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency struct Chart3D<Content> where Content : Chart3DContent
```

#### Overview

Use `Chart3D` to create three-dimensional data visualizations with compatible mark types. To add content to your chart, use the 3D-only [`SurfacePlot`](surfaceplot.md) or the 3D initializers of [`PointMark`](pointmark.md), [`RuleMark`](rulemark.md), and [`RectangleMark`](rectanglemark.md).

For example, you can use a [`SurfacePlot`](surfaceplot.md) to visualize a 3D surface for the function `y = cos(2 * x) * sin(2 * x)`:

```swift
Chart3D {
    SurfacePlot(x: "x", y: "y", z: "z") { x, z in
        sin(2 * x) * cos(2 * z)
    }
}
```

You can also use the 3D initializers for `PointMark` [`init(x:y:z:)`](pointmark/init(x:y:z:).md), `RuleMark` [`init(x:y:z:)`](rulemark/init(x:y:z:).md), `RectangleMark` [`init(x:y:z:)`](rectanglemark/init(x:y:z:).md) to plot 3D visualizations of your data.

For example, suppose you have an array of `Penguin` structures that define datapoints composed of `beakLength`, `weight` `flipperLength`:

```swift
struct Penguin: Identifiable {
    let id: Int
    let flipperLength: Double
    let weight: Double
    let beakLength: Double
}

let penguins: [Penguin] = [
    Penguin(id: 0, flipperLength: 197, weight: 4.2, beakLength: 59),
    Penguin(id: 1, flipperLength: 220, weight: 4.7, beakLength: 48),
    Penguin(id: 2, flipperLength: 235, weight: 5.8, beakLength: 42),
    ...
]
```

You can also use the 3D initializer of`PointMark` [`init(x:y:z:)`](pointmark/init(x:y:z:).md) to represent the `flipperLength` property as the x value, the `weight` property as the y value, and the `beakLength` property as the z value:

```swift
Chart3D(penguins) {
    PointMark(
        x: .value("Flipper Length (mm)", $0.flipperLength),
        y: .value("Weight (kg)", $0.weight),
        z: .value("Beak Length (mm)", $0.beakLength)
    )
}
```

##### Customizing Interactivity

To make your 3D Chart interactive, declare a `@State` property of type  [`Chart3DPose`](chart3dpose.md) and pass it as a binding to the `chart3DPose(_:)-(Binding<Chart3DPose>)` view modifier:

```swift
@State private var pose: Chart3DPose = .default
var body: some View {
    Chart3D(penguins) {
        PointMark(
            x: .value("Flipper Length (mm)", $0.flipperLength),
            y: .value("Weight (kg)", $0.weight),
            z: .value("Beak Length (mm)", $0.beakLength)
        )
    }
    .chart3DPose($pose)
}
```

On available platforms, you can use the `chart3DCameraProjection(_:)` modifier to switch from orthographic to perspective projection.

```swift
Chart3D(penguins) {
    ...
}
.chart3DCameraProjection(.perspective)
```

A SwiftUI view that displays a three-dimensional chart.

## Topics

### Creating 3D charts
- [init<Data, C>(Data, content: (Data.Element) -> C)](chart3d/init(_:content:).md)
  Creates a 3D chart composed of a series of identifiable marks.
- [init<Data, ID, C>(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) -> C)](chart3d/init(_:id:content:).md)
  Creates a 3D chart composed of a series of marks.
- [init(content: () -> Content)](chart3d/init(content:).md)
### Configuring chart shapes
- [protocol Chart3DSymbolShape](chart3dsymbolshape.md)
  A type that can act as a shape for the marks that you add to a chart.
- [struct BasicChart3DSymbolShape](basicchart3dsymbolshape.md)
  A basic chart symbol shape.
### Configuring surfaces
- [protocol Chart3DSurfaceStyle](chart3dsurfacestyle.md)
- [struct BasicChart3DSurfaceStyle](basicchart3dsurfacestyle.md)
### Customizing chart presentation
- [struct Chart3DCameraProjection](chart3dcameraprojection.md)
- [struct Chart3DPose](chart3dpose.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [protocol Chart3DContent](chart3dcontent.md)
  A type that represents the three-dimensional content that you draw on a chart.
- [struct Chart3DContentBuilder](chart3dcontentbuilder.md)
  A result builder that you use to compose the three-dimensional contents of a chart.
- [struct SurfacePlot](surfaceplot.md)
  Chart content that represents a mathematical function of two variables using a 3D surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chart3d)*