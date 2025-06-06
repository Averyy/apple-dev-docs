# init(value:in:step:label:minimumValueLabel:maximumValueLabel:onEditingChanged:)

**Framework**: SwiftUI  
**Kind**: init

Creates a slider to select a value from a given range, subject to a step increment, which displays the provided labels.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
init<V>(value: Binding<V>, in bounds: ClosedRange<V>, step: V.Stride = 1, @ViewBuilder label: () -> Label, @ViewBuilder minimumValueLabel: () -> ValueLabel, @ViewBuilder maximumValueLabel: () -> ValueLabel, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint
```

#### Discussion

The `value` of the created instance is equal to the position of the given value within `bounds`, mapped into `0...1`.

The slider calls `onEditingChanged` when editing begins and ends. For example, on iOS, editing begins when the user starts to drag the thumb along the slider’s track.

## Parameters

- `value`: The selected value within  .
- `bounds`: The range of the valid values.
- `step`: The distance between each valid value.
- `label`: A   that describes the purpose of the instance. Not all   slider styles show the label, but even in those cases, SwiftUI   uses the label for accessibility. For example, VoiceOver uses the   label to identify the purpose of the slider.
- `minimumValueLabel`: A view that describes  .
- `maximumValueLabel`: A view that describes  .
- `onEditingChanged`: A callback for when editing begins and ends.

## See Also

- [init<V>(value: Binding<V>, in: ClosedRange<V>, label: () -> Label, onEditingChanged: (Bool) -> Void)](slider/init(value:in:label:oneditingchanged:).md)
  Creates a slider to select a value from a given range, which displays the provided label.
- [init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () -> Label, onEditingChanged: (Bool) -> Void)](slider/init(value:in:step:label:oneditingchanged:).md)
  Creates a slider to select a value from a given range, subject to a step increment, which displays the provided label.
- [init<V>(value: Binding<V>, in: ClosedRange<V>, label: () -> Label, minimumValueLabel: () -> ValueLabel, maximumValueLabel: () -> ValueLabel, onEditingChanged: (Bool) -> Void)](slider/init(value:in:label:minimumvaluelabel:maximumvaluelabel:oneditingchanged:).md)
  Creates a slider to select a value from a given range, which displays the provided labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/slider/init(value:in:step:label:minimumvaluelabel:maximumvaluelabel:oneditingchanged:))*