# init(value:in:onEditingChanged:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a slider to select a value from a given range, which displays the provided label.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: Slider(value:in:label:onEditingChanged:))
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: Slider(value:in:label:onEditingChanged:))
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: Slider(value:in:label:onEditingChanged:))
- macOS 10.15+ - Deprecated in 27.2 (renamed: Slider(value:in:label:onEditingChanged:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: Slider(value:in:label:onEditingChanged:))
- watchOS 6.0+ - Deprecated in 27.2 (renamed: Slider(value:in:label:onEditingChanged:))

> **Deprecated**: Use [`init(value:in:label:onEditingChanged:)`](./init%28value,in,label,oneditingchanged%29.md) instead.

## Declaration

```swift
nonisolated
init<V>(value: Binding<V>, in bounds: ClosedRange<V> = 0...1, onEditingChanged: @escaping (Bool) -> Void = { _ in }, @ContentBuilder label: () -> Label) where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint
```

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

#### Discussion

The `value` of the created instance is equal to the position of the given value within `bounds`, mapped into `0...1`.

The slider calls `onEditingChanged` when editing begins and ends. For example, on iOS, editing begins when the user starts to drag the thumb along the slider’s track.

## Parameters

- `value`: The selected value within `bounds`.
- `bounds`: The range of the valid values. Defaults to `0...1`.
- `onEditingChanged`: A callback for when editing begins and ends.
- `label`: A `View` that describes the purpose of the instance. Not all slider styles show the label, but even in those cases, SwiftUI uses the label for accessibility. For example, VoiceOver uses the label to identify the purpose of the slider.

## See Also

### Deprecated
- [init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, onEditingChanged: (Bool) -> Void, label: () -> Label)](./init%28value,in,step,oneditingchanged,label%29.md)
  Creates a slider to select a value from a given range, subject to a step increment, which displays the provided label.
- [init<V>(value: Binding<V>, in: ClosedRange<V>, onEditingChanged: (Bool) -> Void, minimumValueLabel: ValueLabel, maximumValueLabel: ValueLabel, label: () -> Label)](./init%28value,in,oneditingchanged,minimumvaluelabel,maximumvaluelabel,label%29.md)
  Creates a slider to select a value from a given range, which displays the provided labels.
- [init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, onEditingChanged: (Bool) -> Void, minimumValueLabel: ValueLabel, maximumValueLabel: ValueLabel, label: () -> Label)](./init%28value,in,step,oneditingchanged,minimumvaluelabel,maximumvaluelabel,label%29.md)
  Creates a slider to select a value from a given range, subject to a step increment, which displays the provided labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/slider/init(value:in:oneditingchanged:label:))*