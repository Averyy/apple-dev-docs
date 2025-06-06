# init(value:in:label:currentValueLabel:markedValueLabels:)

**Framework**: SwiftUI  
**Kind**: init

Creates a gauge representing a value within a range.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init<V>(value: V, in bounds: ClosedRange<V> = 0...1, @ViewBuilder label: () -> Label, @ViewBuilder currentValueLabel: () -> CurrentValueLabel, @ViewBuilder markedValueLabels: () -> MarkedValueLabels) where BoundsLabel == EmptyView, V : BinaryFloatingPoint
```

## Parameters

- `value`: The value to show in the instance.
- `bounds`: The range of the valid values. Defaults to  .
- `label`: A view that describes the purpose of the gauge.
- `currentValueLabel`: A view that describes the current value of   the gauge.
- `markedValueLabels`: A view builder containing tagged views,   each of which describes a particular value of the gauge.   The method ignores this parameter.

## See Also

- [init<V>(value: V, in: ClosedRange<V>, label: () -> Label)](gauge/init(value:in:label:).md)
  Creates a gauge showing a value within a range and describes the gauge’s purpose and current value.
- [init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel: () -> CurrentValueLabel)](gauge/init(value:in:label:currentvaluelabel:).md)
  Creates a gauge showing a value within a range and that describes the gauge’s purpose and current value.
- [init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel: () -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel, maximumValueLabel: () -> BoundsLabel)](gauge/init(value:in:label:currentvaluelabel:minimumvaluelabel:maximumvaluelabel:).md)
  Creates a gauge showing a value within a range and describes the gauge’s current, minimum, and maximum values.
- [init<V>(value: V, in: ClosedRange<V>, label: () -> Label, currentValueLabel: () -> CurrentValueLabel, minimumValueLabel: () -> BoundsLabel, maximumValueLabel: () -> BoundsLabel, markedValueLabels: () -> MarkedValueLabels)](gauge/init(value:in:label:currentvaluelabel:minimumvaluelabel:maximumvaluelabel:markedvaluelabels:).md)
  Creates a gauge representing a value within a range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gauge/init(value:in:label:currentvaluelabel:markedvaluelabels:))*