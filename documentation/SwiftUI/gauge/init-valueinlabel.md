# init(value:in:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a gauge showing a value within a range and describes the gauge’s purpose and current value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init<V>(value: V, in bounds: ClosedRange<V> = 0...1, @ViewBuilder label: () -> Label) where CurrentValueLabel == EmptyView, BoundsLabel == EmptyView, MarkedValueLabels == EmptyView, V : BinaryFloatingPoint
```

#### Discussion

Use this modifier to create a gauge that shows the value at its relative position along the gauge and a label describing the gauge’s purpose. In the example below, the gauge has a range of `0...1`, the indicator is set to `0.4`, or 40 percent of the distance along the gauge:

```swift
struct SimpleGauge: View {
    @State private var batteryLevel = 0.4

    var body: some View {
        Gauge(value: batteryLevel) {
            Text("Battery Level")
        }
    }
}
```

![A linear gauge that shows an indicator at 40 percent along the length](https://docs-assets.developer.apple.com/published/294460fde9fad086627bca9bbcea396f/SwiftUI-Gauge-ValueLabelLinear%402x.png)

## Parameters

- `value`: The value to show in the gauge.
- `bounds`: The range of the valid values. Defaults to  .
- `label`: A view that describes the purpose of the gauge.

## See Also

- [init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel: () -> CurrentValueLabel)](gauge/init(value:in:label:currentvaluelabel:).md)
  Creates a gauge showing a value within a range and that describes the gauge’s purpose and current value.
- [init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel: () -> CurrentValueLabel, markedValueLabels: () -> MarkedValueLabels)](gauge/init(value:in:label:currentvaluelabel:markedvaluelabels:).md)
  Creates a gauge representing a value within a range.
- [init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel: () -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel, maximumValueLabel: () -> BoundsLabel)](gauge/init(value:in:label:currentvaluelabel:minimumvaluelabel:maximumvaluelabel:).md)
  Creates a gauge showing a value within a range and describes the gauge’s current, minimum, and maximum values.
- [init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel: () -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel, maximumValueLabel: () -> BoundsLabel, markedValueLabels: () -> MarkedValueLabels)](gauge/init(value:in:label:currentvaluelabel:minimumvaluelabel:maximumvaluelabel:markedvaluelabels:).md)
  Creates a gauge representing a value within a range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gauge/init(value:in:label:))*