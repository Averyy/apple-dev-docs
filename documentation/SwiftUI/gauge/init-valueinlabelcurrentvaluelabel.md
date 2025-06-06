# init(value:in:label:currentValueLabel:)

**Framework**: SwiftUI  
**Kind**: init

Creates a gauge showing a value within a range and that describes the gauge’s purpose and current value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init<V>(value: V, in bounds: ClosedRange<V> = 0...1, @ViewBuilder label: () -> Label, @ViewBuilder currentValueLabel: () -> CurrentValueLabel) where BoundsLabel == EmptyView, MarkedValueLabels == EmptyView, V : BinaryFloatingPoint
```

#### Discussion

Use this method to create a gauge that displays a value within a range you supply with labels that describe the purpose of the gauge and its current value. In the example below, a gauge using the [`circular`](gaugestyle/circular.md) style shows its current value of `67` along with a label describing the (BPM) for the gauge:

```swift
struct SimpleGauge: View {
    @State private var current = 67.0

    var body: some View {
        Gauge(value: currrent, in: 0...170) {
            Text("BPM")
        } currentValueLabel: {
            Text("\(current)")
        }
        .gaugeStyle(.circular)
   }
}
```

![A screenshot showing a circular gauge describing heart rate in beats](https://docs-assets.developer.apple.com/published/e39aab1677b1eba8885745e659503b54/SwiftUI-Gauge-LabelCurrentValueCircular%402x.png)

## Parameters

- `value`: The value to show on the gauge.
- `bounds`: The range of the valid values. Defaults to  .
- `label`: A view that describes the purpose of the gauge.
- `currentValueLabel`: A view that describes the current value of   the gauge.

## See Also

- [init<V>(value: V, in: ClosedRange<V>, label: () -> Label)](gauge/init(value:in:label:).md)
  Creates a gauge showing a value within a range and describes the gauge’s purpose and current value.
- [init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel: () -> CurrentValueLabel, markedValueLabels: () -> MarkedValueLabels)](gauge/init(value:in:label:currentvaluelabel:markedvaluelabels:).md)
  Creates a gauge representing a value within a range.
- [init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel: () -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel, maximumValueLabel: () -> BoundsLabel)](gauge/init(value:in:label:currentvaluelabel:minimumvaluelabel:maximumvaluelabel:).md)
  Creates a gauge showing a value within a range and describes the gauge’s current, minimum, and maximum values.
- [init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel: () -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel, maximumValueLabel: () -> BoundsLabel, markedValueLabels: () -> MarkedValueLabels)](gauge/init(value:in:label:currentvaluelabel:minimumvaluelabel:maximumvaluelabel:markedvaluelabels:).md)
  Creates a gauge representing a value within a range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gauge/init(value:in:label:currentvaluelabel:))*