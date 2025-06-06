# symbolSize(by:)

**Framework**: Swift Charts  
**Kind**: method

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

- [func foregroundStyle<D>(by: PlottableValue<D>) -> some ChartContent](chartcontent/foregroundstyle(by:).md)
  Represents data using a foreground style.
- [func lineStyle<D>(by: PlottableValue<D>) -> some ChartContent](chartcontent/linestyle(by:).md)
  Represents data using line styles.
- [func position<P>(by: PlottableValue<P>, axis: Axis?, span: MarkDimension) -> some ChartContent](chartcontent/position(by:axis:span:).md)
  Represents data using position.
- [func symbol<D>(by: PlottableValue<D>) -> some ChartContent](chartcontent/symbol(by:).md)
  Represents data using different kinds of symbols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/symbolsize(by:))*