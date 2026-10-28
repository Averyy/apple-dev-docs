# init(_:value:step:format:onEditingChanged:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a stepper with a title and configured to increment and decrement a binding to a value and step amount you provide, displaying its value with an applied format style.

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
init<S, F>(_ title: S, value: Binding<F.FormatInput>, step: F.FormatInput.Stride = 1, format: F, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where S : StringProtocol, F : ParseableFormatStyle, F.FormatInput : BinaryFloatingPoint, F.FormatOutput == String
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<F>(_ titleResource: LocalizedStringResource, value: Binding<F.FormatInput>, step: F.FormatInput.Stride = 1, format: F, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where F : ParseableFormatStyle, F.FormatInput : BinaryFloatingPoint, F.FormatOutput == String
```

```swift
nonisolated
init<F>(_ titleKey: LocalizedStringKey, value: Binding<F.FormatInput>, step: F.FormatInput.Stride = 1, format: F, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where F : ParseableFormatStyle, F.FormatInput : BinaryFloatingPoint, F.FormatOutput == String
```

## Discussion

Use `Stepper(_:value:step:format:onEditingChanged:)` to create a stepper with a custom title that increments or decrements a binding to value by the step size you specify, while displaying the current value.

In the example below, the stepper increments or decrements the binding value by `5` each time one of the user clicks or taps the control’s increment or decrement buttons:

```swift
struct StepperView: View {
    let title: String
    @State private var value = 1.0

    var body: some View {
        Stepper(title, value: $value, step: 5, format: .number)
            .padding(10)
    }
}
```

## Parameters

- `title`: A string describing the purpose of the stepper.
- `value`: The [`Binding`](../binding.md) to a value that you provide.
- `step`: The amount to increment or decrement `value` each time the user clicks or taps the stepper’s increment or decrement button, respectively. Defaults to `1`.
- `format`: A format style of type `F` to use when converting between the string the user edits and the underlying value of type `F.FormatInput`. If `format` can’t perform the conversion, the stepper leaves `value` unchanged. If the user stops editing the text in an invalid state, the stepper updates the text to the last known valid value.
- `onEditingChanged`: A closure that’s called when editing begins and ends. For example, on iOS, the user may touch and hold the increment or decrement buttons on a `Stepper` which causes the execution of the `onEditingChanged` closure at the start and end of the gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/stepper/init(_:value:step:format:oneditingchanged:)-164rp)*