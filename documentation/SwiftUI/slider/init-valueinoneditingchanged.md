# init(value:in:onEditingChanged:)

**Framework**: SwiftUI  
**Kind**: init

Creates a slider to select a value from a given range.

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
init<V>(value: Binding<V>, in bounds: ClosedRange<V> = 0...1, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint
```

#### Discussion

The `value` of the created instance is equal to the position of the given value within `bounds`, mapped into `0...1`.

The slider calls `onEditingChanged` when editing begins and ends. For example, on iOS, editing begins when the user starts to drag the thumb along the slider’s track.

## Parameters

- `value`: The selected value within  .
- `bounds`: The range of the valid values. Defaults to  .
- `onEditingChanged`: A callback for when editing begins and ends.

## See Also

- [init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, onEditingChanged: (Bool) -> Void)](slider/init(value:in:step:oneditingchanged:).md)
  Creates a slider to select a value from a given range, subject to a step increment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/slider/init(value:in:oneditingchanged:))*