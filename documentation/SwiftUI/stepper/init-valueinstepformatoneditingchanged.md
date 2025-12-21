# init(_:value:in:step:format:onEditingChanged:)

**Framework**: SwiftUI  
**Kind**: init

Creates a stepper instance that increments and decrements a binding to a value, by a step size and within a closed range that you provide, displaying its value with an applied format style.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init<F>(_ titleKey: LocalizedStringKey, value: Binding<F.FormatInput>, in bounds: ClosedRange<F.FormatInput>, step: F.FormatInput.Stride = 1, format: F, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where F : ParseableFormatStyle, F.FormatInput : BinaryFloatingPoint, F.FormatOutput == String
```

#### Discussion

Use `Stepper(_:value:in:step:format:onEditingChanged:)` to create a stepper that increments or decrements a value within a specific range of values by a specific step size, while displaying the current value. In the example below, a stepper increments or decrements a binding to value over a range of `1...50` by `5` each time the user clicks or taps the stepper’s increment or decrement buttons:

```swift
struct StepperView: View {
    @State private var value = 0
    private let step = 5.0
    private let range = 1.0...50.0

    var body: some View {
        Stepper("Stepping by \(step) in \(range.description)",
            value: $value,
            in: range,
            step: step,
            format: .number
        )
        .padding()
    }
}
```

## Parameters

- `titleKey`: The key for the stepper’s localized title describing   the purpose of the stepper.
- `value`: A   to a value that your provide.
- `bounds`: A closed range that describes the upper and lower bounds   permitted by the stepper.
- `step`: The amount to increment or decrement   each time the   user clicks or taps the stepper’s increment or decrement button,   respectively. Defaults to  .
- `format`: A format style of type   to use when converting between   the string the user edits and the underlying value of type   . If   can’t perform the conversion, the   stepper leaves   unchanged. If the user stops editing the   text in an invalid state, the stepper updates the text to the last   known valid value.
- `onEditingChanged`: A closure that’s called when editing begins and   ends. For example, on iOS, the user may touch and hold the increment   or decrement buttons on a   which causes the execution   of the   closure at the start and end of   the gesture.

## See Also

- [init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () -> Label, onEditingChanged: (Bool) -> Void)](stepper/init(value:in:step:label:oneditingchanged:).md)
  Creates a stepper configured to increment or decrement a binding to a value using a step value and within a range of values you provide.
- [init<F>(value: Binding<F.FormatInput>, in: ClosedRange<F.FormatInput>, step: F.FormatInput.Stride, format: F, label: () -> Label, onEditingChanged: (Bool) -> Void)](stepper/init(value:in:step:format:label:oneditingchanged:).md)
  Creates a stepper configured to increment or decrement a binding to a value using a step value and within a range of values you provide, displaying its value with an applied format style.
- [init(_:value:in:step:onEditingChanged:)](stepper/init(_:value:in:step:oneditingchanged:).md)
  Creates a stepper instance that increments and decrements a binding to a value, by a step size and within a closed range that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/stepper/init(_:value:in:step:format:oneditingchanged:))*