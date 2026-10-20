# symbolSize(by:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Instance Method

Represents data using symbol sizes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func symbolSize<D>(by value: PlottableValue<D>) -> some ChartContent where D : Plottable
```

## Parameters

- `value`: The data value to encode by size.

## See Also

### Encoding data into mark characteristics
- [func foregroundStyle<D>(by: PlottableValue<D>) -> some ChartContent](./foregroundstyle%28by%29.md)
  Represents data using a foreground style.
- [func lineStyle<D>(by: PlottableValue<D>) -> some ChartContent](./linestyle%28by%29.md)
  Represents data using line styles.
- [func position<P>(by: PlottableValue<P>, axis: Axis?, span: MarkDimension) -> some ChartContent](./position%28by,axis,span%29.md)
  Represents data using position.
- [func symbol<D>(by: PlottableValue<D>) -> some ChartContent](./symbol%28by%29.md)
  Represents data using different kinds of symbols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/symbolsize(by:))*