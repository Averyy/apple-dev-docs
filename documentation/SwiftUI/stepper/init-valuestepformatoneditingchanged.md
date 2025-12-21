# init(_:value:step:format:onEditingChanged:)

**Framework**: SwiftUI  
**Kind**: init

Creates a stepper with a title key and configured to increment and decrement a binding to a value and step amount you provide, displaying its value with an applied format style.

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
init<F>(_ titleKey: LocalizedStringKey, value: Binding<F.FormatInput>, step: F.FormatInput.Stride = 1, format: F, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where F : ParseableFormatStyle, F.FormatInput : BinaryFloatingPoint, F.FormatOutput == String
```

#### Discussion

Use `Stepper(_:value:step:onEditingChanged:)` to create a stepper with a custom title that increments or decrements a binding to value by the step size you specify, while displaying the current value.

In the example below, the stepper increments or decrements the binding value by `5` each time the user clicks or taps on the control’s increment or decrement buttons, respectively:

```swift
struct StepperView: View {
    @State private var value = 1.0
    private let step = 5.0

    var body: some View {
        Stepper("Stepping by \(step)",
            value: $value,
            step: step,
            format: .number
        )
        .padding(10)
    }
}
```

![A view displaying a stepper that increments or decrements by 5 each](https://docs-assets.developer.apple.com/published/a85ed9351b703c8cc865d291ef62b2e9/SwiftUI-Stepper-value-step%402x.png)

## Parameters

- `titleKey`: The key for the stepper’s localized title describing   the purpose of the stepper.
- `value`: A   to a value that you provide.
- `step`: The amount to increment or decrement   each time the   user clicks or taps the stepper’s plus or minus button,   respectively.  Defaults to  .
- `format`: A format style of type   to use when converting between   the string the user edits and the underlying value of type   . If   can’t perform the conversion, the   stepper leaves   unchanged. If the user stops editing the   text in an invalid state, the stepper updates the text to the last   known valid value.
- `onEditingChanged`: A closure that’s called when editing begins and   ends. For example, on iOS, the user may touch and hold the   increment or decrement buttons on a   which causes the   execution of the   closure at the start and end   of the gesture.

## See Also

- [init<V>(value: Binding<V>, step: V.Stride, label: () -> Label, onEditingChanged: (Bool) -> Void)](stepper/init(value:step:label:oneditingchanged:).md)
  Creates a stepper configured to increment or decrement a binding to a value using a step value you provide.
- [init<F>(value: Binding<F.FormatInput>, step: F.FormatInput.Stride, format: F, label: () -> Label, onEditingChanged: (Bool) -> Void)](stepper/init(value:step:format:label:oneditingchanged:).md)
  Creates a stepper configured to increment or decrement a binding to a value using a step value you provide, displaying its value with an applied format style.
- [init(_:value:step:onEditingChanged:)](stepper/init(_:value:step:oneditingchanged:).md)
  Creates a stepper with a title and configured to increment and decrement a binding to a value and step amount you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/stepper/init(_:value:step:format:oneditingchanged:))*