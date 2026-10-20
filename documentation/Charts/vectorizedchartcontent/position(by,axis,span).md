# position(by:axis:span:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Instance Method

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
func position(by value: PlottableProjection<Self.DataElement, some Plottable>, axis: Axis? = nil, span: MarkDimension = .automatic) -> some VectorizedChartContent<Self.DataElement>
```

## See Also

### Styling marks
- [func foregroundStyle(KeyPath<Self.DataElement, some ShapeStyle>) -> some VectorizedChartContent<Self.DataElement>
](./foregroundstyle%28_%29.md)
  Represents data using a foreground style.
- [func opacity(KeyPath<Self.DataElement, CGFloat>) -> some VectorizedChartContent<Self.DataElement>
](./opacity%28_%29.md)
- [func lineStyle(KeyPath<Self.DataElement, StrokeStyle>) -> some VectorizedChartContent<Self.DataElement>
](./linestyle%28_%29.md)
  Represents data using line styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/vectorizedchartcontent/position(by:axis:span:))*