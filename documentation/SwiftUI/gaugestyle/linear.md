# linear

**Framework**: SwiftUI  
**Kind**: property

A gauge style that displays a bar with a marker that appears at a point along the bar to indicate the gauge’s current value.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency static var linear: LinearGaugeStyle { get }
```

#### Discussion

Apply this style to a [`Gauge`](gauge.md) or to a view hierarchy that contains gauges using the [`gaugeStyle(_:)`](view/gaugestyle(_:).md) modifier:

```swift
Gauge(value: batteryLevel, in: 0...100) {
    Text("Battery Level")
}
.gaugeStyle(.linear)
```

If you provide `minimumValueLabel` and `maximumValueLabel` parameters when you create the gauge, they appear on leading and trailing edges of the bar, respectively. Otherwise, the gauge displays the `currentValueLabel` value on the leading edge.

## See Also

- [static var linearCapacity: LinearCapacityGaugeStyle](gaugestyle/linearcapacity.md)
  A gauge style that displays a bar that fills from leading to trailing edges as the gauge’s current value increases.
- [static var accessoryLinear: AccessoryLinearGaugeStyle](gaugestyle/accessorylinear.md)
  A gauge style that displays bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [static var accessoryLinearCapacity: AccessoryLinearCapacityGaugeStyle](gaugestyle/accessorylinearcapacity.md)
  A gauge style that displays bar that fills from leading to trailing edges as the gauge’s current value increases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gaugestyle/linear)*