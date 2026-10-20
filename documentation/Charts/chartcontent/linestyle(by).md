# lineStyle(by:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Instance Method

Represents data using line styles.

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
func lineStyle<D>(by value: PlottableValue<D>) -> some ChartContent where D : Plottable
```

## Parameters

- `value`: The data value.

## See Also

### Encoding data into mark characteristics
- [func foregroundStyle<D>(by: PlottableValue<D>) -> some ChartContent](./foregroundstyle%28by%29.md)
  Represents data using a foreground style.
- [func position<P>(by: PlottableValue<P>, axis: Axis?, span: MarkDimension) -> some ChartContent](./position%28by,axis,span%29.md)
  Represents data using position.
- [func symbol<D>(by: PlottableValue<D>) -> some ChartContent](./symbol%28by%29.md)
  Represents data using different kinds of symbols.
- [func symbolSize<D>(by: PlottableValue<D>) -> some ChartContent](./symbolsize%28by%29.md)
  Represents data using symbol sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/linestyle(by:))*