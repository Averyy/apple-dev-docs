# init(_:x:y:series:)

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
init<Data>(_ data: Data, x: PlottableProjection<LinePlot<Content>.DataElement, some Plottable>, y: PlottableProjection<LinePlot<Content>.DataElement, some Plottable>, series: PlottableProjection<LinePlot<Content>.DataElement, some Plottable>) where Content == VectorizedLinePlotContent<Data>, Data : RandomAccessCollection
```

## See Also

- [init<Data>(Data, x: PlottableProjection<LinePlot<Content>.DataElement, some Plottable>, y: PlottableProjection<LinePlot<Content>.DataElement, some Plottable>)](lineplot/init(_:x:y:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/lineplot/init(_:x:y:series:))*