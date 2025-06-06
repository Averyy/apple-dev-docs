# DefaultGaugeStyle

**Framework**: SwiftUI  
**Kind**: struct

The default gauge view style in the current context of the view being styled.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency struct DefaultGaugeStyle
```

#### Overview

You can also use [`automatic`](gaugestyle/automatic.md) to construct this style.

## Topics

### Creating the gauge style
- [init()](defaultgaugestyle/init.md)
  Creates a default gauge style.

## Relationships

### Conforms To
- [GaugeStyle](gaugestyle.md)

## See Also

- [struct CircularGaugeStyle](circulargaugestyle.md)
  A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [struct AccessoryCircularGaugeStyle](accessorycirculargaugestyle.md)
  A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [struct AccessoryCircularCapacityGaugeStyle](accessorycircularcapacitygaugestyle.md)
  A gauge style that displays a closed ring that’s partially filled in to indicate the gauge’s current value.
- [struct LinearGaugeStyle](lineargaugestyle.md)
  A gauge style that displays a bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [struct LinearCapacityGaugeStyle](linearcapacitygaugestyle.md)
  A gauge style that displays bar that fills from leading to trailing edges as the gauge’s current value increases.
- [struct AccessoryLinearGaugeStyle](accessorylineargaugestyle.md)
  A gauge style that displays bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [struct AccessoryLinearCapacityGaugeStyle](accessorylinearcapacitygaugestyle.md)
  A gauge style that displays bar that fills from leading to trailing edges as the gauge’s current value increases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/defaultgaugestyle)*