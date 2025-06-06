# init(xStart:xEnd:y:series:)

**Framework**: Swift Charts  
**Kind**: init

Creates an area mark that plots values with a horizontal interval and associates it with the specified series.

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
init<X, Y, S>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>, series: PlottableValue<S>) where X : Plottable, Y : Plottable, S : Plottable
```

#### Discussion

The initializer behaves like [`init(xStart:xEnd:y:)`](areamark/init(xstart:xend:y:).md), except that you can indicate which region each interval belongs to by providing a value for the `series` input. This enables you to plot more than one region on a single chart.

To plot a series of values that have a vertical interval, use [`init(x:yStart:yEnd:series:)`](areamark/init(x:ystart:yend:series:).md) instead.

## Parameters

- `xStart`: The starting horizontal position for the mark.
- `xEnd`: The ending horizontal position for the mark.
- `y`: The vertical position for the mark.
- `series`: A series to associate the mark with.

## See Also

- [init<X, Y>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>)](areamark/init(x:ystart:yend:).md)
  Creates an area mark that plots values with a vertical interval.
- [init<X, Y, S>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>, series: PlottableValue<S>)](areamark/init(x:ystart:yend:series:).md)
  Creates an area mark that plots values with a vertical interval and associates it with the specified series.
- [init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>)](areamark/init(xstart:xend:y:).md)
  Creates an area mark that plots values with a horizontal interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/areamark/init(xstart:xend:y:series:))*