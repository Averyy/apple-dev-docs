# foregroundStyle(by:)

**Framework**: Swift Charts  
**Kind**: method

Represents data using a foreground style.

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
func foregroundStyle(by value: PlottableProjection<Self.DataElement, some Plottable>) -> some VectorizedChartContent<Self.DataElement>
```

## Parameters

- `value`: The data value to encode using foreground style.

## See Also

- [func lineStyle(by: PlottableProjection<Self.DataElement, some Plottable>) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/linestyle(by:).md)
  Represents data using line styles.
- [func symbol(by: PlottableProjection<Self.DataElement, some Plottable>) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/symbol(by:).md)
  Represents data using different kinds of symbols.
- [func symbolSize(by: PlottableProjection<Self.DataElement, some Plottable>) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/symbolsize(by:).md)
  Represents data using symbol sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/vectorizedchartcontent/foregroundstyle(by:))*