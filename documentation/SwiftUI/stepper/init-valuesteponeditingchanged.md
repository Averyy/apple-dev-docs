# init(_:value:step:onEditingChanged:)

**Framework**: SwiftUI  
**Kind**: init

Creates a stepper with a title and configured to increment and decrement a binding to a value and step amount you provide.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init<S, V>(_ title: S, value: Binding<V>, step: V.Stride = 1, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where S : StringProtocol, V : Strideable
```

#### Discussion

Use `Stepper(_:value:step:onEditingChanged:)` to create a stepper with a custom title that increments or decrements a binding to value by the step size you specify.

In the example below, the stepper increments or decrements the binding value by `5` each time one of the user clicks or taps the control’s increment or decrement buttons:

```swift
struct StepperView: View {
    @State private var value = 1
    let step = 5
    let title: String

    var body: some View {
        Stepper(title, value: $value, step: step)
            .padding(10)
    }
}
```

![A view displaying a stepper that increments or decrements by 1 each](https://docs-assets.developer.apple.com/published/a85ed9351b703c8cc865d291ef62b2e9/SwiftUI-Stepper-value-step%402x.png)

## Parameters

- `title`: A string describing the purpose of the stepper.
- `value`: The   to a value that you provide.
- `step`: The amount to increment or decrement   each time the   user clicks or taps the stepper’s increment or decrement button,   respectively. Defaults to  .
- `onEditingChanged`: A closure that’s called when editing begins and   ends. For example, on iOS, the user may touch and hold the   increment or decrement buttons on a   which causes the   execution of the   closure at the start and end   of the gesture.

## See Also

- [init<V>(value: Binding<V>, step: V.Stride, label: () -> Label, onEditingChanged: (Bool) -> Void)](stepper/init(value:step:label:oneditingchanged:).md)
  Creates a stepper configured to increment or decrement a binding to a value using a step value you provide.
- [init<F>(value: Binding<F.FormatInput>, step: F.FormatInput.Stride, format: F, label: () -> Label, onEditingChanged: (Bool) -> Void)](stepper/init(value:step:format:label:oneditingchanged:).md)
  Creates a stepper configured to increment or decrement a binding to a value using a step value you provide, displaying its value with an applied format style.
- [init(_:value:step:format:onEditingChanged:)](stepper/init(_:value:step:format:oneditingchanged:).md)
  Creates a stepper with a title key and configured to increment and decrement a binding to a value and step amount you provide, displaying its value with an applied format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/stepper/init(_:value:step:oneditingchanged:))*