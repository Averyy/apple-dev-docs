# init(x:y:series:stacking:)

**Framework**: Swift Charts  
**Kind**: init

Creates an area mark and associates it with the specified series.

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
init<X, Y, S>(x: PlottableValue<X>, y: PlottableValue<Y>, series: PlottableValue<S>, stacking: MarkStackingMethod = .standard) where X : Plottable, Y : Plottable, S : Plottable
```

#### Discussion

The initializer behaves like [`init(x:y:stacking:)`](areamark/init(x:y:stacking:).md), except that you can indicate which region each data point belongs to by providing a value for the `series` input. This enables you to plot more than one region on a single chart.

## Parameters

- `x`: The horizontal position for the mark.
- `y`: The vertical position for the mark.
- `series`: A series to associate the mark with.
- `stacking`: The way in which the chart stacks area regions. The   default is  .

## See Also

- [init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, stacking: MarkStackingMethod)](areamark/init(x:y:stacking:).md)
  Creates an area mark using the specified horizontal and vertical positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/areamark/init(x:y:series:stacking:))*