# lineStyle(_:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Instance Method

Represents data using line styles.

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
func lineStyle(_ style: KeyPath<Self.DataElement, StrokeStyle>) -> some VectorizedChartContent<Self.DataElement>
```

## Parameters

- `style`: The keyPath accessor for shape style.

## See Also

### Styling marks
- [func foregroundStyle(KeyPath<Self.DataElement, some ShapeStyle>) -> some VectorizedChartContent<Self.DataElement>
](./foregroundstyle%28_%29.md)
  Represents data using a foreground style.
- [func opacity(KeyPath<Self.DataElement, CGFloat>) -> some VectorizedChartContent<Self.DataElement>
](./opacity%28_%29.md)
- [func position(by: PlottableProjection<Self.DataElement, some Plottable>, axis: Axis?, span: MarkDimension) -> some VectorizedChartContent<Self.DataElement>
](./position%28by,axis,span%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/vectorizedchartcontent/linestyle(_:))*