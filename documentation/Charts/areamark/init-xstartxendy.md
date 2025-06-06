# init(xStart:xEnd:y:)

**Framework**: Swift Charts  
**Kind**: init

Creates an area mark that plots values with a horizontal interval.

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
init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>) where X : Plottable, Y : Plottable
```

#### Discussion

Use this initializer to create a range area chart with horizontal intervals. For example you can create a region that encompasses all the temperatures over the course of a day, across a number of days:

```swift
Chart(data) { day in
    AreaMark(
        xStart: .value("Minimum Temperature", minimumTemperature),
        xEnd: .value("Maximum Temperature", day.maximumTemperature),
        y: .value("Date", day.date)
    )
}
```

![A chart that shows month names on the y-axis, ranging from January to October, and a number in the range 0 to 80 on the x-axis. A solid blue region spans the chart from top to bottom. The region is close to the middle of the x-axis on either end, and closer to the right of the chart in the middle. The region is thinner at the ends and thicker in the middle.](https://docs-assets.developer.apple.com/published/f553595c5ccf7707839392624453410e/AreaMark-6-macOS%402x.png)

If you want to plot values that have a vertical interval, use [`init(x:yStart:yEnd:)`](areamark/init(x:ystart:yend:).md) instead.

## Parameters

- `xStart`: The starting horizontal position for the mark.
- `xEnd`: The ending horizontal position for the mark.
- `y`: The vertical position for the mark.

## See Also

- [init<X, Y>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>)](areamark/init(x:ystart:yend:).md)
  Creates an area mark that plots values with a vertical interval.
- [init<X, Y, S>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>, series: PlottableValue<S>)](areamark/init(x:ystart:yend:series:).md)
  Creates an area mark that plots values with a vertical interval and associates it with the specified series.
- [init<X, Y, S>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>, series: PlottableValue<S>)](areamark/init(xstart:xend:y:series:).md)
  Creates an area mark that plots values with a horizontal interval and associates it with the specified series.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/areamark/init(xstart:xend:y:))*