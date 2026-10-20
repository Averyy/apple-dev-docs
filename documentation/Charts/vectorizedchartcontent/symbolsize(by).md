# symbolSize(by:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Instance Method

Represents data using symbol sizes.

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
func symbolSize(by value: PlottableProjection<Self.DataElement, some Plottable>) -> some VectorizedChartContent<Self.DataElement>
```

## Parameters

- `value`: The data value to encode by size.

## See Also

### Encoding data into mark characteristics
- [func foregroundStyle(by: PlottableProjection<Self.DataElement, some Plottable>) -> some VectorizedChartContent<Self.DataElement>
](./foregroundstyle%28by%29.md)
  Represents data using a foreground style.
- [func lineStyle(by: PlottableProjection<Self.DataElement, some Plottable>) -> some VectorizedChartContent<Self.DataElement>
](./linestyle%28by%29.md)
  Represents data using line styles.
- [func symbol(by: PlottableProjection<Self.DataElement, some Plottable>) -> some VectorizedChartContent<Self.DataElement>
](./symbol%28by%29.md)
  Represents data using different kinds of symbols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/vectorizedchartcontent/symbolsize(by:))*