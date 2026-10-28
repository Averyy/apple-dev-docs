# chartXAxisStyle(content:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures the x axis content of charts.

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
func chartXAxisStyle<Content>(@ViewBuilder content: @escaping (ChartAxisContent) -> Content) -> some View where Content : View
```

## Discussion

Use this modifier to configure the size or aspect ratio of the plot area of charts.

For example:

```swift
Chart(data: data) {
    BarMark(x: .value("Category", $0.category))
}
.chartXAxisStyle { axis in
    axis.opacity(0.5)
}
```

## Parameters

- `content`: A closure that returns the content of the axis.

## See Also

### Axes
- [func chartXAxis(Visibility) -> some View](./chartxaxis%28_%29.md)
  Sets the visibility of the x axis.
- [func chartXAxis<Content>(content: () -> Content) -> some View](./chartxaxis%28content%29.md)
  Configures the x-axis for charts in the view.
- [func chartYAxis(Visibility) -> some View](./chartyaxis%28_%29.md)
  Sets the visibility of the y axis.
- [func chartYAxis<Content>(content: () -> Content) -> some View](./chartyaxis%28content%29.md)
  Configures the y-axis for charts in the view.
- [func chartYAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some View](./chartyaxisstyle%28content%29.md)
  Configures the y axis content of charts.
- [func chartZAxis(Visibility) -> some View](./chartzaxis%28_%29.md)
  Sets the visibility of the z axis.
- [func chartZAxis<Content>(content: () -> Content) -> some View](./chartzaxis%28content%29.md)
  Configures the z-axis for 3D charts in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartxaxisstyle(content:))*