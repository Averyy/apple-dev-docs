# GaugeStyleConfiguration

**Framework**: SwiftUI  
**Kind**: struct

The properties of a gauge instance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
struct GaugeStyleConfiguration
```

## Topics

### Describing the purpose of the gauge
- [var label: GaugeStyleConfiguration.Label](gaugestyleconfiguration/label-swift.property.md)
  A view that describes the purpose of the gauge.
- [GaugeStyleConfiguration.Label](gaugestyleconfiguration/label-swift.struct.md)
  A type-erased label of a gauge, describing its purpose.
### Reporting the range
- [var minimumValueLabel: GaugeStyleConfiguration.MinimumValueLabel?](gaugestyleconfiguration/minimumvaluelabel-swift.property.md)
  A view that describes the minimum of the range for the current value.
- [GaugeStyleConfiguration.MinimumValueLabel](gaugestyleconfiguration/minimumvaluelabel-swift.struct.md)
  A type-erased value label of a gauge describing the minimum value.
- [var maximumValueLabel: GaugeStyleConfiguration.MaximumValueLabel?](gaugestyleconfiguration/maximumvaluelabel-swift.property.md)
  A view that describes the maximum of the range for the current value.
- [GaugeStyleConfiguration.MaximumValueLabel](gaugestyleconfiguration/maximumvaluelabel-swift.struct.md)
  A type-erased value label of a gauge describing the maximum value.
### Setting the value
- [var value: Double](gaugestyleconfiguration/value.md)
  The current value of the gauge.
- [var currentValueLabel: GaugeStyleConfiguration.CurrentValueLabel?](gaugestyleconfiguration/currentvaluelabel-swift.property.md)
  A view that describes the current value.
- [GaugeStyleConfiguration.CurrentValueLabel](gaugestyleconfiguration/currentvaluelabel-swift.struct.md)
  A type-erased value label of a gauge that contains the current value.
- [GaugeStyleConfiguration.MarkedValueLabel](gaugestyleconfiguration/markedvaluelabel.md)
  A type-erased label describing a specific value of a gauge.

## See Also

- [func gaugeStyle<S>(S) -> some View](view/gaugestyle(_:).md)
  Sets the style for gauges within this view.
- [protocol GaugeStyle](gaugestyle.md)
  Defines the implementation of all gauge instances within a view hierarchy.
- [func progressViewStyle<S>(S) -> some View](view/progressviewstyle(_:).md)
  Sets the style for progress views in this view.
- [protocol ProgressViewStyle](progressviewstyle.md)
  A type that applies standard interaction behavior to all progress views within a view hierarchy.
- [struct ProgressViewStyleConfiguration](progressviewstyleconfiguration.md)
  The properties of a progress view instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gaugestyleconfiguration)*