# init(_:value:in:step:onEditingChanged:)

**Framework**: SwiftUI  
**Kind**: init

Creates a stepper instance that increments and decrements a binding to a value, by a step size and within a closed range that you provide.

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
init<S, V>(_ title: S, value: Binding<V>, in bounds: ClosedRange<V>, step: V.Stride = 1, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where S : StringProtocol, V : Strideable
```

#### Discussion

Use `Stepper(_:value:in:step:onEditingChanged:)` to create a stepper that increments or decrements a value within a specific range of values by a specific step size. In the example below, a stepper increments or decrements a binding to value over a range of `1...50` by `5` each time the user clicks or taps the stepper’s increment or decrement buttons:

```swift
struct StepperView: View {
    @State private var value = 0
    let step = 5
    let range = 1...50

    var body: some View {
        Stepper("Current: \(value) in \(range.description) stepping by \(step)",
                value: $value,
                in: range,
                step: step)
            .padding(10)
    }
}
```

![A view displaying a stepper that increments or decrements within a](https://docs-assets.developer.apple.com/published/21941a9c414c8460cb45d5d7d33ce928/SwiftUI-Stepper-value-step-range%402x.png)

## Parameters

- `title`: A string describing the purpose of the stepper.
- `value`: A   to a value that your provide.
- `bounds`: A closed range that describes the upper and lower bounds   permitted by the stepper.
- `step`: The amount to increment or decrement   each time the   user clicks or taps the stepper’s increment or decrement button,   respectively. Defaults to  .
- `onEditingChanged`: A closure that’s called when editing begins and   ends. For example, on iOS, the user may touch and hold the increment   or decrement buttons on a   which causes the execution   of the   closure at the start and end of   the gesture.

## See Also

- [init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () -> Label, onEditingChanged: (Bool) -> Void)](stepper/init(value:in:step:label:oneditingchanged:).md)
  Creates a stepper configured to increment or decrement a binding to a value using a step value and within a range of values you provide.
- [init<F>(value: Binding<F.FormatInput>, in: ClosedRange<F.FormatInput>, step: F.FormatInput.Stride, format: F, label: () -> Label, onEditingChanged: (Bool) -> Void)](stepper/init(value:in:step:format:label:oneditingchanged:).md)
  Creates a stepper configured to increment or decrement a binding to a value using a step value and within a range of values you provide, displaying its value with an applied format style.
- [init(_:value:in:step:format:onEditingChanged:)](stepper/init(_:value:in:step:format:oneditingchanged:).md)
  Creates a stepper instance that increments and decrements a binding to a value, by a step size and within a closed range that you provide, displaying its value with an applied format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/stepper/init(_:value:in:step:oneditingchanged:))*