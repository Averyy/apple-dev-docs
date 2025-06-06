# init(_:xStart:xEnd:y:)

**Framework**: Swift Charts  
**Kind**: init

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
init<Data, X>(_ data: Data, xStart: PlottableProjection<AreaPlot<Content>.DataElement, X>, xEnd: PlottableProjection<AreaPlot<Content>.DataElement, X>, y: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>) where Content == VectorizedAreaPlotContent<Data>, Data : RandomAccessCollection, X : Plottable
```

## See Also

- [init<Data>(Data, x: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, y: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, stacking: MarkStackingMethod)](areaplot/init(_:x:y:stacking:).md)
- [init<Data>(Data, x: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, y: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, series: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, stacking: MarkStackingMethod)](areaplot/init(_:x:y:series:stacking:).md)
- [init<Data, X>(Data, xStart: PlottableProjection<AreaPlot<Content>.DataElement, X>, xEnd: PlottableProjection<AreaPlot<Content>.DataElement, X>, y: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, series: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>)](areaplot/init(_:xstart:xend:y:series:).md)
- [init<Data, Y>(Data, x: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, yStart: PlottableProjection<AreaPlot<Content>.DataElement, Y>, yEnd: PlottableProjection<AreaPlot<Content>.DataElement, Y>)](areaplot/init(_:x:ystart:yend:).md)
- [init<Data, Y>(Data, x: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, yStart: PlottableProjection<AreaPlot<Content>.DataElement, Y>, yEnd: PlottableProjection<AreaPlot<Content>.DataElement, Y>, series: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>)](areaplot/init(_:x:ystart:yend:series:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/areaplot/init(_:xstart:xend:y:))*