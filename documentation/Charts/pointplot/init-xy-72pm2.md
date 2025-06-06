# init(_:x:y:)

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
init<Data>(_ data: Data, x: PlottableProjection<PointPlot<Content>.DataElement, some Plottable>, y: CGFloat? = nil) where Content == VectorizedPointPlotContent<Data>, Data : RandomAccessCollection
```

## See Also

- [init<Data>(Data, x: KeyPath<Data.Element, CGFloat>, y: PlottableProjection<PointPlot<Content>.DataElement, some Plottable>)](pointplot/init(_:x:y:)-1a9af.md)
- [init<Data>(Data, x: CGFloat?, y: PlottableProjection<PointPlot<Content>.DataElement, some Plottable>)](pointplot/init(_:x:y:)-1p6px.md)
- [init<Data>(Data, x: PlottableProjection<PointPlot<Content>.DataElement, some Plottable>, y: PlottableProjection<PointPlot<Content>.DataElement, some Plottable>)](pointplot/init(_:x:y:)-7frpp.md)
- [init<Data>(Data, x: PlottableProjection<PointPlot<Content>.DataElement, some Plottable>, y: KeyPath<PointPlot<Content>.DataElement, CGFloat>)](pointplot/init(_:x:y:)-9p3yg.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/pointplot/init(_:x:y:)-72pm2)*