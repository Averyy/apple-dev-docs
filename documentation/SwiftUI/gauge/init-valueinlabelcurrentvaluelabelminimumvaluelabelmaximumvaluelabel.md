# init(value:in:label:currentValueLabel:minimumValueLabel:maximumValueLabel:)

**Framework**: SwiftUI  
**Kind**: init

Creates a gauge showing a value within a range and describes the gauge’s current, minimum, and maximum values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init<V>(value: V, in bounds: ClosedRange<V> = 0...1, @ViewBuilder label: () -> Label, @ViewBuilder currentValueLabel: () -> CurrentValueLabel, @ViewBuilder minimumValueLabel: () -> BoundsLabel, @ViewBuilder maximumValueLabel: () -> BoundsLabel) where MarkedValueLabels == EmptyView, V : BinaryFloatingPoint
```

#### Discussion

Use this method to create a gauge that shows a value within a prescribed bounds. The gauge has labels that describe its purpose, and for the gauge’s current, minimum, and maximum values.

```swift
struct LabeledGauge: View {
    @State private var current = 67.0
    @State private var minValue = 0.0
    @State private var maxValue = 170.0

    var body: some View {
        Gauge(value: current, in: minValue...maxValue) {
            Text("BPM")
        } currentValueLabel: {
            Text("\(Int(current))")
        } minimumValueLabel: {
            Text("\(Int(minValue))")
        } maximumValueLabel: {
            Text("\(Int(maxValue))")
        }
    }
}
```

![A screenshot of a gauge, labeled BPM, that’s represented by a](https://docs-assets.developer.apple.com/published/f36677c0da94cb4224de1633c1367dd7/SwiftUI-Gauge-LabeledCircular%402x.png)

## Parameters

- `value`: The value to show on the gauge.
- `bounds`: The range of the valid values. Defaults to  .
- `label`: A view that describes the purpose of the gauge.
- `currentValueLabel`: A view that describes the current value of   the gauge.
- `minimumValueLabel`: A view that describes the lower bounds of the   gauge.
- `maximumValueLabel`: A view that describes the upper bounds of the   gauge.

## See Also

- [init<V>(value: V, in: ClosedRange<V>, label: () -> Label)](gauge/init(value:in:label:).md)
  Creates a gauge showing a value within a range and describes the gauge’s purpose and current value.
- [init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel: () -> CurrentValueLabel)](gauge/init(value:in:label:currentvaluelabel:).md)
  Creates a gauge showing a value within a range and that describes the gauge’s purpose and current value.
- [init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel: () -> CurrentValueLabel, markedValueLabels: () -> MarkedValueLabels)](gauge/init(value:in:label:currentvaluelabel:markedvaluelabels:).md)
  Creates a gauge representing a value within a range.
- [init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel: () -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel, maximumValueLabel: () -> BoundsLabel, markedValueLabels: () -> MarkedValueLabels)](gauge/init(value:in:label:currentvaluelabel:minimumvaluelabel:maximumvaluelabel:markedvaluelabels:).md)
  Creates a gauge representing a value within a range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gauge/init(value:in:label:currentvaluelabel:minimumvaluelabel:maximumvaluelabel:))*