# chartZAxis(content:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures the z-axis for 3D charts in the view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
func chartZAxis<Content>(@AxisContentBuilder content: () -> Content) -> some View where Content : AxisContent
```

#### Discussion

Use this modifier to customize the z-axis of a chart. Provide an `AxisMarks` builder that composes `AxisGridLine`, `AxisTick`, and `AxisValueLabel` structures to form the axis. Omit components from the builder to omit them from the resulting axis. For example, the following code adds grid lines to the z-axis:

```swift
.chartZAxis {
    AxisMarks {
        AxisGridLine()
    }
}
```

Use arguments such as `position:` or `values:` to control the placement of the axis values it displays.

> **Note**: To add an axis label, use one of the label modifiers, like https://developer.apple.com/documentation/SwiftUI/View/chartZAxisLabel(position:alignment:spacing:content:).

## Parameters

- `content`: The axis content.

## See Also

### Axes
- [func chartXAxis(Visibility) -> some View](./chartxaxis%28_%29.md)
  Sets the visibility of the x axis.
- [func chartXAxis<Content>(content: () -> Content) -> some View](./chartxaxis%28content%29.md)
  Configures the x-axis for charts in the view.
- [func chartXAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some View](./chartxaxisstyle%28content%29.md)
  Configures the x axis content of charts.
- [func chartYAxis(Visibility) -> some View](./chartyaxis%28_%29.md)
  Sets the visibility of the y axis.
- [func chartYAxis<Content>(content: () -> Content) -> some View](./chartyaxis%28content%29.md)
  Configures the y-axis for charts in the view.
- [func chartYAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some View](./chartyaxisstyle%28content%29.md)
  Configures the y axis content of charts.
- [func chartZAxis(Visibility) -> some View](./chartzaxis%28_%29.md)
  Sets the visibility of the z axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartzaxis(content:))*