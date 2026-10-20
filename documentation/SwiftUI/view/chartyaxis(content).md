# chartYAxis(content:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures the y-axis for charts in the view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func chartYAxis<Content>(@AxisContentBuilder content: () -> Content) -> some View where Content : AxisContent
```

#### Discussion

Use this modifier to customize the y-axis of a chart. Provide an `AxisMarks` builder that composes `AxisGridLine`, `AxisTick`, and `AxisValueLabel` structures to form the axis. Omit components from the builder to omit them from the resulting axis. For example, the following code adds grid lines to the y-axis:

```swift
.chartYAxis {
    AxisMarks {
        AxisGridLine()
    }
}
```

Use arguments such as `position:` or `values:` to control the placement of the axis values it displays.

```swift
Chart(BatteryData.data, id: \.date) {
     BarMark(
         x: .value("Time", $0.date ..< $0.date.advanced(by: 1800)),
         y: .value("Battery Level", $0.level)
     )
     .foregroundStyle(.green)
 }
 .chartYAxis {
     AxisMarks(values: [0, 25, 50, 75, 100]) {
         AxisGridLine()
     }

     AxisMarks(values: [0, 50, 100]) {
         AxisValueLabel(format: Decimal.FormatStyle.Percent.percent.scale(1))
     }
 }
 .chartXAxis {
     AxisMarks(values: .stride(by: .hour, count: 3)) { value in
         if let date = value.as(Date.self) {
             let hour = Calendar.current.component(.hour, from: date)
             switch hour {
             case 0, 12:
                 AxisValueLabel {
                     VStack {
                         Text(date, format: .dateTime.hour())
                         if value.index == 0 {
                             Text(date, format: .dateTime.month().day())
                         }
                     }
                 }
             default:
                 AxisValueLabel(format: .dateTime.hour(.defaultDigits(amPM: .omitted)))
             }

             if hour == 0 {
                 AxisGridLine(stroke: StrokeStyle(lineWidth: 0.5))
                 AxisTick(stroke: StrokeStyle(lineWidth: 0.5))
             } else {
                 AxisGridLine()
                 AxisTick()
             }
         }
     }
 }
```

The above code customizes the y-axis to appear on the leading edge of the chart, with a solid grid line at the 0% and 100% marks.

> **Note**: To add an axis label, use one of the label modifiers, like [`chartYAxisLabel(position:alignment:spacing:content:)`](./chartyaxislabel%28position,alignment,spacing,content%29.md).

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
- [func chartYAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some View](./chartyaxisstyle%28content%29.md)
  Configures the y axis content of charts.
- [func chartZAxis(Visibility) -> some View](./chartzaxis%28_%29.md)
  Sets the visibility of the z axis.
- [func chartZAxis<Content>(content: () -> Content) -> some View](./chartzaxis%28content%29.md)
  Configures the z-axis for 3D charts in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartyaxis(content:))*