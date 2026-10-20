# symbolSize(_:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Instance Method

Sets the plotting symbol size for the chart content according to a perceived area.

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
func symbolSize(_ area: KeyPath<Self.DataElement, CGFloat>) -> some VectorizedChartContent<Self.DataElement>
```

## Parameters

- `area`: The perceived area in square points. For example, a square with 10 points on each side has an area of 100 square points.

## See Also

### Setting symbol appearance
- [func symbol(by: PlottableProjection<Self.DataElement, some Plottable>) -> some VectorizedChartContent<Self.DataElement>
](./symbol%28by%29.md)
  Represents data using different kinds of symbols.
- [func symbolSize(KeyPath<Self.DataElement, CGSize>) -> some VectorizedChartContent<Self.DataElement>
](./symbolsize%28_%29-12tl1.md)
  Sets the plotting symbol size for the chart content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/vectorizedchartcontent/symbolsize(_:)-3nwop)*