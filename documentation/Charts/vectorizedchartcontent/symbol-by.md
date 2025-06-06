# symbol(by:)

**Framework**: Swift Charts  
**Kind**: method

Represents data using different kinds of symbols.

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
func symbol(by value: PlottableProjection<Self.DataElement, some Plottable>) -> some VectorizedChartContent<Self.DataElement>
```

## Parameters

- `value`: The data value.   must be categorial, such as  .

## See Also

- [func symbolSize(KeyPath<Self.DataElement, CGSize>) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/symbolsize(_:)-12tl1.md)
  Sets the plotting symbol size for the chart content.
- [func symbolSize(KeyPath<Self.DataElement, CGFloat>) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/symbolsize(_:)-3nwop.md)
  Sets the plotting symbol size for the chart content according to a perceived area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/vectorizedchartcontent/symbol(by:))*