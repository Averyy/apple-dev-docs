# init(_:xStart:xEnd:y:)

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
init<Data>(_ data: Data, xStart: KeyPath<RulePlot<Content>.DataElement, CGFloat>, xEnd: KeyPath<RulePlot<Content>.DataElement, CGFloat>, y: PlottableProjection<RulePlot<Content>.DataElement, some Plottable>) where Content == VectorizedRulePlotContent<Data>, Data : RandomAccessCollection
```

## See Also

### Plotting rules from a collection
- [init<Data>(Data, x: PlottableProjection<RulePlot<Content>.DataElement, some Plottable>, yStart: CGFloat?, yEnd: CGFloat?)](./init%28_,x,ystart,yend%29-13wts.md)
- [init<Data, Y>(Data, x: KeyPath<RulePlot<Content>.DataElement, CGFloat>, yStart: PlottableProjection<RulePlot<Content>.DataElement, Y>, yEnd: PlottableProjection<RulePlot<Content>.DataElement, Y>)](./init%28_,x,ystart,yend%29-3fig9.md)
- [init<Data>(Data, x: PlottableProjection<RulePlot<Content>.DataElement, some Plottable>, yStart: KeyPath<RulePlot<Content>.DataElement, CGFloat>, yEnd: KeyPath<RulePlot<Content>.DataElement, CGFloat>)](./init%28_,x,ystart,yend%29-6ts7e.md)
- [init<Data, Y>(Data, x: CGFloat?, yStart: PlottableProjection<RulePlot<Content>.DataElement, Y>, yEnd: PlottableProjection<RulePlot<Content>.DataElement, Y>)](./init%28_,x,ystart,yend%29-8b2lx.md)
- [init<Data, Y>(Data, x: PlottableProjection<RulePlot<Content>.DataElement, some Plottable>, yStart: PlottableProjection<RulePlot<Content>.DataElement, Y>, yEnd: PlottableProjection<RulePlot<Content>.DataElement, Y>)](./init%28_,x,ystart,yend%29-zxo0.md)
- [init<Data>(Data, xStart: CGFloat?, xEnd: CGFloat?, y: PlottableProjection<RulePlot<Content>.DataElement, some Plottable>)](./init%28_,xstart,xend,y%29-4yxo8.md)
- [init<Data, X>(Data, xStart: PlottableProjection<RulePlot<Content>.DataElement, X>, xEnd: PlottableProjection<RulePlot<Content>.DataElement, X>, y: KeyPath<RulePlot<Content>.DataElement, CGFloat>)](./init%28_,xstart,xend,y%29-54gxx.md)
- [init<Data, X>(Data, xStart: PlottableProjection<RulePlot<Content>.DataElement, X>, xEnd: PlottableProjection<RulePlot<Content>.DataElement, X>, y: PlottableProjection<RulePlot<Content>.DataElement, some Plottable>)](./init%28_,xstart,xend,y%29-8ehr7.md)
- [init<Data, X>(Data, xStart: PlottableProjection<RulePlot<Content>.DataElement, X>, xEnd: PlottableProjection<RulePlot<Content>.DataElement, X>, y: CGFloat?)](./init%28_,xstart,xend,y%29-hx5a.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/ruleplot/init(_:xstart:xend:y:)-3dsvn)*