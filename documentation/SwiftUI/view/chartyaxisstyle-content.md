# chartYAxisStyle(content:)

**Framework**: SwiftUI  
**Kind**: method

Configures the y axis content of charts.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func chartYAxisStyle<Content>(@ViewBuilder content: @escaping (ChartAxisContent) -> Content) -> some View where Content : View
```

#### Discussion

Use this modifier to configure the size or aspect ratio of the plot area of charts.

For example:

```swift
Chart(data: data) {
    BarMark(x: .value("Category", $0.category))
}
.chartYAxisStyle { axis in
    axis.opacity(0.5)
}
```

## Parameters

- `content`: A closure that returns the content of the axis.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartyaxisstyle(content:))*