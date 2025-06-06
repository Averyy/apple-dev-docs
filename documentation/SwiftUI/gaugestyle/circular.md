# circular

**Framework**: SwiftUI  
**Kind**: property

A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency static var circular: CircularGaugeStyle { get }
```

#### Discussion

Apply this style to a [`Gauge`](gauge.md) or to a view hierarchy that contains gauges using the [`gaugeStyle(_:)`](view/gaugestyle(_:).md) modifier:

```swift
Gauge(value: batteryLevel, in: 0...100) {
    Text("Battery Level")
}
.gaugeStyle(.circular)
```

This style displays the gauge’s `currentValueLabel` value at the center of the gauge. If you provide `minimumValueLabel` and `maximumValueLabel` parameters when you create the gauge, they appear in the opening at the bottom of the ring. Otherwise, the gauge places its label in that location.

## See Also

- [static var accessoryCircular: AccessoryCircularGaugeStyle](gaugestyle/accessorycircular.md)
  A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [static var accessoryCircularCapacity: AccessoryCircularCapacityGaugeStyle](gaugestyle/accessorycircularcapacity.md)
  A gauge style that displays a closed ring that’s partially filled in to indicate the gauge’s current value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gaugestyle/circular)*