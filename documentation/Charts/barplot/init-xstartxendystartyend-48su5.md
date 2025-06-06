# init(_:xStart:xEnd:yStart:yEnd:)

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
init<Data, X>(_ data: Data, xStart: PlottableProjection<BarPlot<Content>.DataElement, X>, xEnd: PlottableProjection<BarPlot<Content>.DataElement, X>, yStart: CGFloat? = nil, yEnd: CGFloat? = nil) where Content == VectorizedBarPlotContent<Data>, Data : RandomAccessCollection, X : Plottable
```

## See Also

- [init<Data>(Data, x: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, y: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, width: MarkDimensions<BarPlot<Content>.DataElement>, height: MarkDimensions<BarPlot<Content>.DataElement>, stacking: MarkStackingMethod)](barplot/init(_:x:y:width:height:stacking:).md)
- [init<Data, Y>(Data, x: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, yStart: PlottableProjection<BarPlot<Content>.DataElement, Y>, yEnd: PlottableProjection<BarPlot<Content>.DataElement, Y>, width: MarkDimensions<BarPlot<Content>.DataElement>)](barplot/init(_:x:ystart:yend:width:).md)
- [init<Data>(Data, x: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, yStart: CGFloat?, yEnd: CGFloat?, width: MarkDimensions<BarPlot<Content>.DataElement>, stacking: MarkStackingMethod)](barplot/init(_:x:ystart:yend:width:stacking:)-2mtih.md)
- [init<Data>(Data, x: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, yStart: KeyPath<BarPlot<Content>.DataElement, CGFloat>, yEnd: KeyPath<BarPlot<Content>.DataElement, CGFloat>, width: MarkDimensions<BarPlot<Content>.DataElement>, stacking: MarkStackingMethod)](barplot/init(_:x:ystart:yend:width:stacking:)-680hw.md)
- [init<Data>(Data, xStart: KeyPath<BarPlot<Content>.DataElement, CGFloat>, xEnd: KeyPath<BarPlot<Content>.DataElement, CGFloat>, y: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, height: MarkDimensions<BarPlot<Content>.DataElement>, stacking: MarkStackingMethod)](barplot/init(_:xstart:xend:y:height:stacking:)-16tou.md)
- [init<Data>(Data, xStart: CGFloat?, xEnd: CGFloat?, y: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, height: MarkDimensions<BarPlot<Content>.DataElement>, stacking: MarkStackingMethod)](barplot/init(_:xstart:xend:y:height:stacking:)-2x0yx.md)
- [init<Data, X>(Data, xStart: PlottableProjection<BarPlot<Content>.DataElement, X>, xEnd: PlottableProjection<BarPlot<Content>.DataElement, X>, y: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, height: MarkDimensions<BarPlot<Content>.DataElement>)](barplot/init(_:xstart:xend:y:height:).md)
- [init<Data, Y>(Data, xStart: KeyPath<BarPlot<Content>.DataElement, CGFloat>, xEnd: KeyPath<BarPlot<Content>.DataElement, CGFloat>, yStart: PlottableProjection<BarPlot<Content>.DataElement, Y>, yEnd: PlottableProjection<BarPlot<Content>.DataElement, Y>)](barplot/init(_:xstart:xend:ystart:yend:)-862wn.md)
- [init<Data, X>(Data, xStart: PlottableProjection<BarPlot<Content>.DataElement, X>, xEnd: PlottableProjection<BarPlot<Content>.DataElement, X>, yStart: KeyPath<BarPlot<Content>.DataElement, CGFloat>, yEnd: KeyPath<BarPlot<Content>.DataElement, CGFloat>)](barplot/init(_:xstart:xend:ystart:yend:)-mtdv.md)
- [init<Data, Y>(Data, xStart: CGFloat?, xEnd: CGFloat?, yStart: PlottableProjection<BarPlot<Content>.DataElement, Y>, yEnd: PlottableProjection<BarPlot<Content>.DataElement, Y>)](barplot/init(_:xstart:xend:ystart:yend:)-raqh.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/barplot/init(_:xstart:xend:ystart:yend:)-48su5)*