# chartZAxis(content:)

**Framework**: SwiftUI  
**Kind**: method

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

> **Note**: To add an axis label, use one of the label modifiers, like doc://com.apple.documentation/documentation/SwiftUI/View/chartZAxisLabel(position:alignment:spacing:content:).

## Parameters

- `content`: The axis content.

## See Also

- [func chartXAxis(Visibility) -> some View](view/chartxaxis(_:).md)
  Sets the visibility of the x axis.
- [func chartXAxis<Content>(content: () -> Content) -> some View](view/chartxaxis(content:).md)
  Configures the x-axis for charts in the view.
- [func chartXAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some View](view/chartxaxisstyle(content:).md)
  Configures the x axis content of charts.
- [func chartYAxis(Visibility) -> some View](view/chartyaxis(_:).md)
  Sets the visibility of the y axis.
- [func chartYAxis<Content>(content: () -> Content) -> some View](view/chartyaxis(content:).md)
  Configures the y-axis for charts in the view.
- [func chartYAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some View](view/chartyaxisstyle(content:).md)
  Configures the y axis content of charts.
- [func chartZAxis(Visibility) -> some View](view/chartzaxis(_:).md)
  Sets the visibility of the z axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartzaxis(content:))*