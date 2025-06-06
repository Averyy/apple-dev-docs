# init(_:angle:innerRadius:outerRadius:angularInset:)

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
init<Data>(_ data: Data, angle: PlottableProjection<SectorPlot<Content>.DataElement, some Plottable>, innerRadius: MarkDimensions<SectorPlot<Content>.DataElement> = .automatic, outerRadius: MarkDimensions<SectorPlot<Content>.DataElement> = .automatic, angularInset: KeyPath<SectorPlot<Content>.DataElement, CGFloat>) where Content == VectorizedSectorPlotContent<Data>, Data : RandomAccessCollection
```

## See Also

- [init<Data>(Data, angle: PlottableProjection<SectorPlot<Content>.DataElement, some Plottable>, innerRadius: MarkDimensions<SectorPlot<Content>.DataElement>, outerRadius: MarkDimensions<SectorPlot<Content>.DataElement>, angularInset: CGFloat?)](sectorplot/init(_:angle:innerradius:outerradius:angularinset:)-1ed01.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/sectorplot/init(_:angle:innerradius:outerradius:angularinset:)-9pmo7)*