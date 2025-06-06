# ProgressViewStyleConfiguration

**Framework**: SwiftUI  
**Kind**: struct

The properties of a progress view instance.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
struct ProgressViewStyleConfiguration
```

## Topics

### Configuring the label
- [var label: ProgressViewStyleConfiguration.Label?](progressviewstyleconfiguration/label-swift.property.md)
  A view that describes the task represented by the progress view.
- [ProgressViewStyleConfiguration.Label](progressviewstyleconfiguration/label-swift.struct.md)
  A type-erased label describing the task represented by the progress view.
### Configuring the current value label
- [var currentValueLabel: ProgressViewStyleConfiguration.CurrentValueLabel?](progressviewstyleconfiguration/currentvaluelabel-swift.property.md)
  A view that describes the current value of a progress view.
- [ProgressViewStyleConfiguration.CurrentValueLabel](progressviewstyleconfiguration/currentvaluelabel-swift.struct.md)
  A type-erased label that describes the current value of a progress view.
### Configuring progress completion
- [let fractionCompleted: Double?](progressviewstyleconfiguration/fractioncompleted.md)
  The completed fraction of the task represented by the progress view, from `0.0` (not yet started) to `1.0` (fully complete), or `nil` if the progress is indeterminate or relative to a date interval.

## See Also

- [func gaugeStyle<S>(S) -> some View](view/gaugestyle(_:).md)
  Sets the style for gauges within this view.
- [protocol GaugeStyle](gaugestyle.md)
  Defines the implementation of all gauge instances within a view hierarchy.
- [struct GaugeStyleConfiguration](gaugestyleconfiguration.md)
  The properties of a gauge instance.
- [func progressViewStyle<S>(S) -> some View](view/progressviewstyle(_:).md)
  Sets the style for progress views in this view.
- [protocol ProgressViewStyle](progressviewstyle.md)
  A type that applies standard interaction behavior to all progress views within a view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressviewstyleconfiguration)*