# init(x:yStart:yEnd:)

**Framework**: Swift Charts  
**Kind**: init

Creates an area mark that plots values with a vertical interval.

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
init<X, Y>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>) where X : Plottable, Y : Plottable
```

#### Discussion

Use this initializer to create a range area chart with vertical intervals. For example you can create a region that encompasses all the temperatures over the course of a day, across a number of days:

```swift
Chart(data) { day in
    AreaMark(
        x: .value("Date", day.date),
        yStart: .value("Minimum Temperature", minimumTemperature),
        yEnd: .value("Maximum Temperature", day.maximumTemperature)
    )
}
```

![A chart that shows month names on the x-axis, ranging from January to October, and a number in the range 0 to 80 on the y-axis. A solid blue region spans the chart from left to right. The region is close to the middle of the y-axis on either end, and closer to the top of the chart in the middle. The region is thinner at the ends and thicker in the middle.](https://docs-assets.developer.apple.com/published/312b9822d288c8f1e400decc5e04ad9e/AreaMark-5-macOS%402x.png)

If you want to plot values that have a horiztonal interval, use [`init(xStart:xEnd:y:)`](areamark/init(xstart:xend:y:).md) instead.

## Parameters

- `x`: The horizontal position for the mark.
- `yStart`: The starting vertical position for the mark.
- `yEnd`: The ending vertical position for the mark.

## See Also

- [init<X, Y, S>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>, series: PlottableValue<S>)](areamark/init(x:ystart:yend:series:).md)
  Creates an area mark that plots values with a vertical interval and associates it with the specified series.
- [init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>)](areamark/init(xstart:xend:y:).md)
  Creates an area mark that plots values with a horizontal interval.
- [init<X, Y, S>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>, series: PlottableValue<S>)](areamark/init(xstart:xend:y:series:).md)
  Creates an area mark that plots values with a horizontal interval and associates it with the specified series.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/areamark/init(x:ystart:yend:))*