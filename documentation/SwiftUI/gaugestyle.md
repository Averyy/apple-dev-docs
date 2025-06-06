# GaugeStyle

**Framework**: SwiftUI  
**Kind**: protocol

Defines the implementation of all gauge instances within a view hierarchy.

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
@preconcurrency protocol GaugeStyle
```

#### Overview

To configure the style for all the [`Gauge`](gauge.md) instances in a view hierarchy, use the [`gaugeStyle(_:)`](view/gaugestyle(_:).md) modifier. For example, you can configure a gauge to use the [`circular`](gaugestyle/circular.md) style:

```swift
Gauge(value: batteryLevel, in: 0...100) {
    Text("Battery Level")
}
.gaugeStyle(.circular)
```

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Topics

### Getting the automatic style
- [static var automatic: DefaultGaugeStyle](gaugestyle/automatic.md)
  The default gauge view style in the current context of the view being styled.
### Getting circular gauge styles
- [static var circular: CircularGaugeStyle](gaugestyle/circular.md)
  A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [static var accessoryCircular: AccessoryCircularGaugeStyle](gaugestyle/accessorycircular.md)
  A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [static var accessoryCircularCapacity: AccessoryCircularCapacityGaugeStyle](gaugestyle/accessorycircularcapacity.md)
  A gauge style that displays a closed ring that’s partially filled in to indicate the gauge’s current value.
### Getting linear gauge styles
- [static var linear: LinearGaugeStyle](gaugestyle/linear.md)
  A gauge style that displays a bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [static var linearCapacity: LinearCapacityGaugeStyle](gaugestyle/linearcapacity.md)
  A gauge style that displays a bar that fills from leading to trailing edges as the gauge’s current value increases.
- [static var accessoryLinear: AccessoryLinearGaugeStyle](gaugestyle/accessorylinear.md)
  A gauge style that displays bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [static var accessoryLinearCapacity: AccessoryLinearCapacityGaugeStyle](gaugestyle/accessorylinearcapacity.md)
  A gauge style that displays bar that fills from leading to trailing edges as the gauge’s current value increases.
### Creating custom gauge styles
- [func makeBody(configuration: Self.Configuration) -> Self.Body](gaugestyle/makebody(configuration:).md)
  Creates a view representing the body of a gauge.
- [GaugeStyle.Configuration](gaugestyle/configuration.md)
  The properties of a gauge instance.
- [associatedtype Body : View](gaugestyle/body.md)
  A view representing the body of a gauge.
### Supporting types
- [struct DefaultGaugeStyle](defaultgaugestyle.md)
  The default gauge view style in the current context of the view being styled.
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

## Relationships

### Conforming Types
- [AccessoryCircularCapacityGaugeStyle](accessorycircularcapacitygaugestyle.md)
- [AccessoryCircularGaugeStyle](accessorycirculargaugestyle.md)
- [AccessoryLinearCapacityGaugeStyle](accessorylinearcapacitygaugestyle.md)
- [AccessoryLinearGaugeStyle](accessorylineargaugestyle.md)
- [CircularGaugeStyle](circulargaugestyle.md)
- [DefaultGaugeStyle](defaultgaugestyle.md)
- [LinearCapacityGaugeStyle](linearcapacitygaugestyle.md)
- [LinearGaugeStyle](lineargaugestyle.md)

## See Also

- [func gaugeStyle<S>(S) -> some View](view/gaugestyle(_:).md)
  Sets the style for gauges within this view.
- [struct GaugeStyleConfiguration](gaugestyleconfiguration.md)
  The properties of a gauge instance.
- [func progressViewStyle<S>(S) -> some View](view/progressviewstyle(_:).md)
  Sets the style for progress views in this view.
- [protocol ProgressViewStyle](progressviewstyle.md)
  A type that applies standard interaction behavior to all progress views within a view hierarchy.
- [struct ProgressViewStyleConfiguration](progressviewstyleconfiguration.md)
  The properties of a progress view instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gaugestyle)*