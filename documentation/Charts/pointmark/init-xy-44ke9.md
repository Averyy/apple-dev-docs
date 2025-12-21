# init(x:y:)

**Framework**: Swift Charts  
**Kind**: init

Creates a point mark that plots values to x and y.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>) where X : Plottable, Y : Plottable
```

##### Discussion

Use this initializer to plot one property with x and another property with y:

```swift
Chart(data) {
    PointMark(
        x: .value("Wing Length", $0.wingLength),
        y: .value("Wing Length", $0.wingWidth)
    )
}
```

![A scatter plot with wing width plotted on the x-axis and wing height plotted on the y-axis. There are 12 points on the chart that demonstrate a roughly linear relationship between wing width and height.](https://docs-assets.developer.apple.com/published/fca032573a6787a1f164ba898618e71a/PointMarkSwift.PointMarkScatterChart%402x.png)

For more background, see the first example used in [`PointMark`](pointmark.md) which shows the structure that contains the `wingLength` and `wingHeight` properties.

## Parameters

- `x`: The value plotted with x.
- `y`: The value plotted with y.

## See Also

- [init<Y>(x: CGFloat?, y: PlottableValue<Y>)](pointmark/init(x:y:)-9dswq.md)
  Creates a point mark with fixed x position and plots values with y.
- [init<X>(x: PlottableValue<X>, y: CGFloat?)](pointmark/init(x:y:)-9hppd.md)
  Creates a point mark that plots a value on x with fixed y position.
- [init(x: PlottableValue<some Plottable>, y: PlottableValue<some Plottable>, z: PlottableValue<some Plottable>)](pointmark/init(x:y:z:).md)
  Creates a 3D point mark that plots values to x, y and z.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/pointmark/init(x:y:)-44ke9)*