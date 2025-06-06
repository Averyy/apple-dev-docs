# position(by:axis:span:)

**Framework**: Swift Charts  
**Kind**: method

Represents data using position.

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
func position<P>(by value: PlottableValue<P>, axis: Axis? = nil, span: MarkDimension = .automatic) -> some ChartContent where P : Plottable
```

#### Discussion

The code below creates a grouped bar chart that positions marks with the same “product” along the horizontal axis by their “type”.

```swift
Chart(cars) {
    BarMark(
        x: .value("product", $0.product),
        y: .value("price", $0.price)
    )
    .position(by: .value("type", $0.type), axis: .horizontal)
}
```

## Parameters

- `value`: The data used for positioning marks.
- `axis`: The axis to position marks along. Set this to    to use a default configuration.
- `span`: The span of the positioned marks. Use this to control   the total amount space available to the marks.

## See Also

- [func foregroundStyle<D>(by: PlottableValue<D>) -> some ChartContent](chartcontent/foregroundstyle(by:).md)
  Represents data using a foreground style.
- [func lineStyle<D>(by: PlottableValue<D>) -> some ChartContent](chartcontent/linestyle(by:).md)
  Represents data using line styles.
- [func symbol<D>(by: PlottableValue<D>) -> some ChartContent](chartcontent/symbol(by:).md)
  Represents data using different kinds of symbols.
- [func symbolSize<D>(by: PlottableValue<D>) -> some ChartContent](chartcontent/symbolsize(by:).md)
  Represents data using symbol sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/position(by:axis:span:))*