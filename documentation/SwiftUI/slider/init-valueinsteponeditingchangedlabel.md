# init(value:in:step:onEditingChanged:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a slider to select a value from a given range, subject to a step increment, which displays the provided label.

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
init<V>(value: Binding<V>, in bounds: ClosedRange<V>, step: V.Stride = 1, onEditingChanged: @escaping (Bool) -> Void = { _ in }, @ViewBuilder label: () -> Label) where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint
```

#### Discussion

The `value` of the created instance is equal to the position of the given value within `bounds`, mapped into `0...1`.

The slider calls `onEditingChanged` when editing begins and ends. For example, on iOS, editing begins when the user starts to drag the thumb along the slider’s track.

## Parameters

- `value`: The selected value within  .
- `bounds`: The range of the valid values. Defaults to  .
- `step`: The distance between each valid value.
- `onEditingChanged`: A callback for when editing begins and ends.
- `label`: A   that describes the purpose of the instance. Not all   slider styles show the label, but even in those cases, SwiftUI   uses the label for accessibility. For example, VoiceOver uses the   label to identify the purpose of the slider.

## See Also

- [init<V>(value: Binding<V>, in: ClosedRange<V>, onEditingChanged: (Bool) -> Void, label: () -> Label)](slider/init(value:in:oneditingchanged:label:).md)
  Creates a slider to select a value from a given range, which displays the provided label.
- [init<V>(value: Binding<V>, in: ClosedRange<V>, onEditingChanged: (Bool) -> Void, minimumValueLabel: ValueLabel, maximumValueLabel: ValueLabel, label: () -> Label)](slider/init(value:in:oneditingchanged:minimumvaluelabel:maximumvaluelabel:label:).md)
  Creates a slider to select a value from a given range, which displays the provided labels.
- [init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, onEditingChanged: (Bool) -> Void, minimumValueLabel: ValueLabel, maximumValueLabel: ValueLabel, label: () -> Label)](slider/init(value:in:step:oneditingchanged:minimumvaluelabel:maximumvaluelabel:label:).md)
  Creates a slider to select a value from a given range, subject to a step increment, which displays the provided labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/slider/init(value:in:step:oneditingchanged:label:))*