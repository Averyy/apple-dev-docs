# foregroundStyle(_:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Instance Method

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
func foregroundStyle(_ keyPath: KeyPath<Self.DataElement, some ShapeStyle>) -> some VectorizedChartContent<Self.DataElement>
```

## Parameters

- `keyPath`: The accessor for shape style.

## See Also

### Styling marks
- [func opacity(KeyPath<Self.DataElement, CGFloat>) -> some VectorizedChartContent<Self.DataElement>
](./opacity%28_%29.md)
- [func lineStyle(KeyPath<Self.DataElement, StrokeStyle>) -> some VectorizedChartContent<Self.DataElement>
](./linestyle%28_%29.md)
  Represents data using line styles.
- [func position(by: PlottableProjection<Self.DataElement, some Plottable>, axis: Axis?, span: MarkDimension) -> some VectorizedChartContent<Self.DataElement>
](./position%28by,axis,span%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/vectorizedchartcontent/foregroundstyle(_:))*