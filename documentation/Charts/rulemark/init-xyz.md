# init(x:y:z:)

**Framework**: Swift Charts  
**Kind**: init

Creates a horizontal or vertical rule mark for a  3D chart.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
init(x: PlottableValue<some Plottable>, y: PlottableValue<some Plottable>, z: PlottableValue<some Plottable>)
```

#### Discussion

> ❗ **Important**: A 3D RuleMark requires exactly two numeric points and one numeric range.

Use this initializer to create rules at positions along two axes, and a range along a third axis:

```swift
Chart3D {
    // A red rule from from -0.5 to 0.5 on the x-axis, positioned at y = 0, z = 0
    RuleMark(
        x: .value("x", -0.5..<0.5),
        y: .value("y", 0),
        z: .value("z", 0)
    )
    .foregroundStyle(.red)

    // A green rule from -0.5 to 0.5 on the y-axis, positioned at x = 0, z = 0
    RuleMark(
        x: .value("x", 0),
        y: .value("y", -0.5..<0.5),
        z: .value("z", 0)
    )
    .foregroundStyle(.green)

    // A blue rule from from -0.5 to 0.5 on the z-axis, positioned at x = 0, y = 0
    RuleMark(
        x: .value("x", 0),
        y: .value("y", 0),
        z: .value("z", -0.5..<0.5)
    )
    .foregroundStyle(.blue)
}
```

## Parameters

- `x`: The x value.
- `y`: The y value.
- `z`: The z value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/rulemark/init(x:y:z:))*