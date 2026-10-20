# init(_:x:y:series:)

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
init<Data>(_ data: Data, x: PlottableProjection<LinePlot<Content>.DataElement, some Plottable>, y: PlottableProjection<LinePlot<Content>.DataElement, some Plottable>, series: PlottableProjection<LinePlot<Content>.DataElement, some Plottable>) where Content == VectorizedLinePlotContent<Data>, Data : RandomAccessCollection
```

## See Also

### Plotting lines from a collection
- [init<Data>(Data, x: PlottableProjection<LinePlot<Content>.DataElement, some Plottable>, y: PlottableProjection<LinePlot<Content>.DataElement, some Plottable>)](./init%28_,x,y%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/lineplot/init(_:x:y:series:))*