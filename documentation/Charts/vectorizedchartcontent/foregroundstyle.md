# foregroundStyle(_:)

**Framework**: Swift Charts  
**Kind**: method

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

- [func opacity(KeyPath<Self.DataElement, CGFloat>) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/opacity(_:).md)
- [func lineStyle(KeyPath<Self.DataElement, StrokeStyle>) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/linestyle(_:).md)
  Represents data using line styles.
- [func position(by: PlottableProjection<Self.DataElement, some Plottable>, axis: Axis?, span: MarkDimension) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/position(by:axis:span:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/vectorizedchartcontent/foregroundstyle(_:))*