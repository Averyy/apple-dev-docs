# accessoryLinearCapacity

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A gauge style that displays bar that fills from leading to trailing edges as the gauge’s current value increases.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@export(implementation) @preconcurrency static var accessoryLinearCapacity: AccessoryLinearCapacityGaugeStyle { get }
```

Available when `Self` is `AccessoryLinearCapacityGaugeStyle`.

#### Discussion

Apply this style to a [`Gauge`](../gauge.md) or to a view hierarchy that contains gauges using the [`gaugeStyle(_:)`](../view/gaugestyle%28_%29.md) modifier:

```swift
Gauge(value: batteryLevel, in: 0...100) {
    Text("Battery Level")
}
.gaugeStyle(.accessoryLinearCapacity)
```

If you provide `minimumValueLabel` and `maximumValueLabel` parameters when you create the gauge, they appear on leading and trailing edges of the bar, respectively. The `label` appears above the gauge, and the `currentValueLabel` appears below.

## See Also

### Getting linear gauge styles
- [static var linear: LinearGaugeStyle](./linear.md)
  A gauge style that displays a bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [static var linearCapacity: LinearCapacityGaugeStyle](./linearcapacity.md)
  A gauge style that displays a bar that fills from leading to trailing edges as the gauge’s current value increases.
- [static var accessoryLinear: AccessoryLinearGaugeStyle](./accessorylinear.md)
  A gauge style that displays bar with a marker that appears at a point along the bar to indicate the gauge’s current value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gaugestyle/accessorylinearcapacity)*