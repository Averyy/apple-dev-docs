# init(_:x:yStart:yEnd:width:)

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
init<Data>(_ data: Data, x: PlottableProjection<RectanglePlot<Content>.DataElement, some Plottable>, yStart: CGFloat? = nil, yEnd: CGFloat? = nil, width: MarkDimensions<RectanglePlot<Content>.DataElement> = .automatic) where Content == VectorizedRectanglePlotContent<Data>, Data : RandomAccessCollection
```

## See Also

- [init<Data>(Data, x: PlottableProjection<RectanglePlot<Content>.DataElement, some Plottable>, y: PlottableProjection<RectanglePlot<Content>.DataElement, some Plottable>, width: MarkDimensions<RectanglePlot<Content>.DataElement>, height: MarkDimensions<RectanglePlot<Content>.DataElement>)](rectangleplot/init(_:x:y:width:height:).md)
- [init<Data, Y>(Data, x: PlottableProjection<RectanglePlot<Content>.DataElement, some Plottable>, yStart: PlottableProjection<RectanglePlot<Content>.DataElement, Y>, yEnd: PlottableProjection<RectanglePlot<Content>.DataElement, Y>, width: MarkDimensions<RectanglePlot<Content>.DataElement>)](rectangleplot/init(_:x:ystart:yend:width:)-93op1.md)
- [init<Data>(Data, x: PlottableProjection<RectanglePlot<Content>.DataElement, some Plottable>, yStart: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, yEnd: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, width: MarkDimensions<RectanglePlot<Content>.DataElement>)](rectangleplot/init(_:x:ystart:yend:width:)-nnvk.md)
- [init<Data>(Data, xStart: CGFloat?, xEnd: CGFloat?, y: PlottableProjection<RectanglePlot<Content>.DataElement, some Plottable>, height: MarkDimensions<RectanglePlot<Content>.DataElement>)](rectangleplot/init(_:xstart:xend:y:height:)-51nra.md)
- [init<Data>(Data, xStart: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, xEnd: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, y: PlottableProjection<RectanglePlot<Content>.DataElement, some Plottable>, height: MarkDimensions<RectanglePlot<Content>.DataElement>)](rectangleplot/init(_:xstart:xend:y:height:)-8s17v.md)
- [init<Data, X>(Data, xStart: PlottableProjection<RectanglePlot<Content>.DataElement, X>, xEnd: PlottableProjection<RectanglePlot<Content>.DataElement, X>, y: PlottableProjection<RectanglePlot<Content>.DataElement, some Plottable>, height: MarkDimensions<RectanglePlot<Content>.DataElement>)](rectangleplot/init(_:xstart:xend:y:height:)-15ish.md)
- [init<Data, X>(Data, xStart: PlottableProjection<RectanglePlot<Content>.DataElement, X>, xEnd: PlottableProjection<RectanglePlot<Content>.DataElement, X>, yStart: CGFloat?, yEnd: CGFloat?)](rectangleplot/init(_:xstart:xend:ystart:yend:)-46wi0.md)
- [init<Data, X, Y>(Data, xStart: PlottableProjection<RectanglePlot<Content>.DataElement, X>, xEnd: PlottableProjection<RectanglePlot<Content>.DataElement, X>, yStart: PlottableProjection<RectanglePlot<Content>.DataElement, Y>, yEnd: PlottableProjection<RectanglePlot<Content>.DataElement, Y>)](rectangleplot/init(_:xstart:xend:ystart:yend:)-4g377.md)
- [init<Data, Y>(Data, xStart: CGFloat?, xEnd: CGFloat?, yStart: PlottableProjection<RectanglePlot<Content>.DataElement, Y>, yEnd: PlottableProjection<RectanglePlot<Content>.DataElement, Y>)](rectangleplot/init(_:xstart:xend:ystart:yend:)-6d8yb.md)
- [init<Data, X>(Data, xStart: PlottableProjection<RectanglePlot<Content>.DataElement, X>, xEnd: PlottableProjection<RectanglePlot<Content>.DataElement, X>, yStart: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, yEnd: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>)](rectangleplot/init(_:xstart:xend:ystart:yend:)-6uuk4.md)
- [init<Data, Y>(Data, xStart: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, xEnd: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, yStart: PlottableProjection<RectanglePlot<Content>.DataElement, Y>, yEnd: PlottableProjection<RectanglePlot<Content>.DataElement, Y>)](rectangleplot/init(_:xstart:xend:ystart:yend:)-741lz.md)
- [init<Data>(Data, xStart: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, xEnd: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, yStart: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, yEnd: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>)](rectangleplot/init(_:xstart:xend:ystart:yend:)-ir9o.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/rectangleplot/init(_:x:ystart:yend:width:)-12u1b)*