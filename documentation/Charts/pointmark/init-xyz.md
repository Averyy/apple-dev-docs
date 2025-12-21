# init(x:y:z:)

**Framework**: Swift Charts  
**Kind**: init

Creates a 3D point mark that plots values to x, y and z.

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

> ❗ **Important**: A 3D PointMark requires exactly three numeric points.

Use this initializer to plot one property with each of the x, y and z axes:

```swift
Chart3D(data) {
    PointMark(
        x: .value("Wing Length", $0.wingLength),
        y: .value("Wing Width", $0.wingWidth),
        z: .value("Weight", $0.weight)
    )
}
```

## Parameters

- `x`: The x position.
- `y`: The y position.
- `z`: The z position.

## See Also

- [init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>)](pointmark/init(x:y:)-44ke9.md)
  Creates a point mark that plots values to x and y.
- [init<Y>(x: CGFloat?, y: PlottableValue<Y>)](pointmark/init(x:y:)-9dswq.md)
  Creates a point mark with fixed x position and plots values with y.
- [init<X>(x: PlottableValue<X>, y: CGFloat?)](pointmark/init(x:y:)-9hppd.md)
  Creates a point mark that plots a value on x with fixed y position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/pointmark/init(x:y:z:))*