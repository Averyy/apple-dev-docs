# opacity(_:)

**Framework**: Swift Charts  
**Kind**: method

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
func opacity(_ keyPath: KeyPath<Self.DataElement, CGFloat>) -> some VectorizedChartContent<Self.DataElement>
```

## Parameters

- `keyPath`: Points to a value between 0 (fully transparent) and 1 (fully opaque).

## See Also

- [func foregroundStyle(KeyPath<Self.DataElement, some ShapeStyle>) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/foregroundstyle(_:).md)
  Represents data using a foreground style.
- [func lineStyle(KeyPath<Self.DataElement, StrokeStyle>) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/linestyle(_:).md)
  Represents data using line styles.
- [func position(by: PlottableProjection<Self.DataElement, some Plottable>, axis: Axis?, span: MarkDimension) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/position(by:axis:span:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/vectorizedchartcontent/opacity(_:))*