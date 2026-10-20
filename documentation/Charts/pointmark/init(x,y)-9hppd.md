# init(x:y:)

**Framework**: Swift Charts  
**Kind**: init  
**Role**: Initializer

Creates a point mark that plots a value on x with fixed y position.

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
init<X>(x: PlottableValue<X>, y: CGFloat? = nil) where X : Plottable
```

##### Discussion

Use this initializer to plot a property with x:

```swift
Chart(data) {
    PointMark(
        x: .value("Weight", $0.weight)
    )
}
```

![Horizontal point chart with weight plotted to the x-axis. There are 9 points at: 22, 24, 18, 22, 30, 27, 20, 14, 29.](https://developer.apple.com/tutorials/images/com.apple.Charts/PointMarkSwift.PointMarkHorizontalPointChart@2x.png)

For more background, see the first example used in [`PointMark`](../pointmark.md) which shows the structure that contains the `weight` property.

## Parameters

- `x`: The value plotted with x.
- `y`: The y position.  If `y` is `nil`, the bar will be centered vertically by default.

## See Also

### Creating a point mark
- [init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>)](./init%28x,y%29-44ke9.md)
  Creates a point mark that plots values to x and y.
- [init<Y>(x: CGFloat?, y: PlottableValue<Y>)](./init%28x,y%29-9dswq.md)
  Creates a point mark with fixed x position and plots values with y.
- [init(x: PlottableValue<some Plottable>, y: PlottableValue<some Plottable>, z: PlottableValue<some Plottable>)](./init%28x,y,z%29.md)
  Creates a 3D point mark that plots values to x, y and z.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/pointmark/init(x:y:)-9hppd)*