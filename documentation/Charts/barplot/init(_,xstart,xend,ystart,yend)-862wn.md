# init(_:xStart:xEnd:yStart:yEnd:)

**Framework**: Swift Charts  
**Kind**: init  
**Role**: Initializer

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
init<Data, Y>(_ data: Data, xStart: KeyPath<BarPlot<Content>.DataElement, CGFloat>, xEnd: KeyPath<BarPlot<Content>.DataElement, CGFloat>, yStart: PlottableProjection<BarPlot<Content>.DataElement, Y>, yEnd: PlottableProjection<BarPlot<Content>.DataElement, Y>) where Content == VectorizedBarPlotContent<Data>, Data : RandomAccessCollection, Y : Plottable
```

## See Also

### Plotting bars from a collection
- [init<Data>(Data, x: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, y: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, width: MarkDimensions<BarPlot<Content>.DataElement>, height: MarkDimensions<BarPlot<Content>.DataElement>, stacking: MarkStackingMethod)](./init%28_,x,y,width,height,stacking%29.md)
- [init<Data, Y>(Data, x: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, yStart: PlottableProjection<BarPlot<Content>.DataElement, Y>, yEnd: PlottableProjection<BarPlot<Content>.DataElement, Y>, width: MarkDimensions<BarPlot<Content>.DataElement>)](./init%28_,x,ystart,yend,width%29.md)
- [init<Data>(Data, x: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, yStart: CGFloat?, yEnd: CGFloat?, width: MarkDimensions<BarPlot<Content>.DataElement>, stacking: MarkStackingMethod)](./init%28_,x,ystart,yend,width,stacking%29-2mtih.md)
- [init<Data>(Data, x: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, yStart: KeyPath<BarPlot<Content>.DataElement, CGFloat>, yEnd: KeyPath<BarPlot<Content>.DataElement, CGFloat>, width: MarkDimensions<BarPlot<Content>.DataElement>, stacking: MarkStackingMethod)](./init%28_,x,ystart,yend,width,stacking%29-680hw.md)
- [init<Data>(Data, xStart: KeyPath<BarPlot<Content>.DataElement, CGFloat>, xEnd: KeyPath<BarPlot<Content>.DataElement, CGFloat>, y: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, height: MarkDimensions<BarPlot<Content>.DataElement>, stacking: MarkStackingMethod)](./init%28_,xstart,xend,y,height,stacking%29-16tou.md)
- [init<Data>(Data, xStart: CGFloat?, xEnd: CGFloat?, y: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, height: MarkDimensions<BarPlot<Content>.DataElement>, stacking: MarkStackingMethod)](./init%28_,xstart,xend,y,height,stacking%29-2x0yx.md)
- [init<Data, X>(Data, xStart: PlottableProjection<BarPlot<Content>.DataElement, X>, xEnd: PlottableProjection<BarPlot<Content>.DataElement, X>, y: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, height: MarkDimensions<BarPlot<Content>.DataElement>)](./init%28_,xstart,xend,y,height%29.md)
- [init<Data, X>(Data, xStart: PlottableProjection<BarPlot<Content>.DataElement, X>, xEnd: PlottableProjection<BarPlot<Content>.DataElement, X>, yStart: CGFloat?, yEnd: CGFloat?)](./init%28_,xstart,xend,ystart,yend%29-48su5.md)
- [init<Data, X>(Data, xStart: PlottableProjection<BarPlot<Content>.DataElement, X>, xEnd: PlottableProjection<BarPlot<Content>.DataElement, X>, yStart: KeyPath<BarPlot<Content>.DataElement, CGFloat>, yEnd: KeyPath<BarPlot<Content>.DataElement, CGFloat>)](./init%28_,xstart,xend,ystart,yend%29-mtdv.md)
- [init<Data, Y>(Data, xStart: CGFloat?, xEnd: CGFloat?, yStart: PlottableProjection<BarPlot<Content>.DataElement, Y>, yEnd: PlottableProjection<BarPlot<Content>.DataElement, Y>)](./init%28_,xstart,xend,ystart,yend%29-raqh.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/barplot/init(_:xstart:xend:ystart:yend:)-862wn)*