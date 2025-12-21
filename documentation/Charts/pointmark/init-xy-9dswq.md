# init(x:y:)

**Framework**: Swift Charts  
**Kind**: init

Creates a point mark with fixed x position and plots values with y.

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
init<Y>(x: CGFloat? = nil, y: PlottableValue<Y>) where Y : Plottable
```

##### Discussion

Use this initializer to plot a property to y:

```swift
Chart(data) {
    PointMark(
        y: .value("Weight", $0.weight)
    )
}
```

![Vertical point chart with weight plotted to the y-axis. There are 9 points at: 22, 24, 18, 22, 30, 27, 20, 14, 29.](https://docs-assets.developer.apple.com/published/50181f48d9c044281492be817a26addc/PointMarkSwift.PointMarkVerticalPointChart%402x.png)

For more background, see the first example used in [`PointMark`](pointmark.md) which shows the structure that contains the `weight` property.

## Parameters

- `x`: The x position.  If   is  , the bar will be centered horizontally by default.
- `y`: The value plotted with y.

## See Also

- [init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>)](pointmark/init(x:y:)-44ke9.md)
  Creates a point mark that plots values to x and y.
- [init<X>(x: PlottableValue<X>, y: CGFloat?)](pointmark/init(x:y:)-9hppd.md)
  Creates a point mark that plots a value on x with fixed y position.
- [init(x: PlottableValue<some Plottable>, y: PlottableValue<some Plottable>, z: PlottableValue<some Plottable>)](pointmark/init(x:y:z:).md)
  Creates a 3D point mark that plots values to x, y and z.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/pointmark/init(x:y:)-9dswq)*