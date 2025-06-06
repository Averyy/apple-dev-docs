# init(value:in:step:label:onEditingChanged:)

**Framework**: SwiftUI  
**Kind**: init

Creates a stepper configured to increment or decrement a binding to a value using a step value and within a range of values you provide.

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
init<V>(value: Binding<V>, in bounds: ClosedRange<V>, step: V.Stride = 1, @ViewBuilder label: () -> Label, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where V : Strideable
```

#### Discussion

Use this initializer to create a stepper that increments or decrements a binding to value by the step size you provide within the given bounds. By setting the bounds, you ensure that the value never goes below or above the lowest or highest value, respectively.

The example below shows a stepper that displays the effect of incrementing or decrementing a value with the step size of `step` with the bounds defined by `range`:

```swift
struct StepperView: View {
    @State private var value = 0
    let step = 5
    let range = 1...50

    var body: some View {
        Stepper(value: $value,
                in: range,
                step: step) {
            Text("Current: \(value) in \(range.description) " +
                 "stepping by \(step)")
        }
            .padding(10)
    }
}
```

![A view displaying a stepper with a step size of five, and a](https://docs-assets.developer.apple.com/published/21941a9c414c8460cb45d5d7d33ce928/SwiftUI-Stepper-value-step-range%402x.png)

## Parameters

- `value`: A   to a value that you provide.
- `bounds`: A closed range that describes the upper and lower bounds   permitted by the stepper.
- `step`: The amount to increment or decrement the stepper when the   user clicks or taps the stepper’s increment or decrement buttons,   respectively.
- `label`: A view describing the purpose of this stepper.
- `onEditingChanged`: A closure that’s called when editing begins and   ends. For example, on iOS, the user may touch and hold the increment   or decrement buttons on a stepper which causes the execution   of the   closure at the start and end of   the gesture.

## See Also

- [init<F>(value: Binding<F.FormatInput>, in: ClosedRange<F.FormatInput>, step: F.FormatInput.Stride, format: F, label: () -> Label, onEditingChanged: (Bool) -> Void)](stepper/init(value:in:step:format:label:oneditingchanged:).md)
  Creates a stepper configured to increment or decrement a binding to a value using a step value and within a range of values you provide, displaying its value with an applied format style.
- [init(_:value:in:step:onEditingChanged:)](stepper/init(_:value:in:step:oneditingchanged:).md)
  Creates a stepper instance that increments and decrements a binding to a value, by a step size and within a closed range that you provide.
- [init(_:value:in:step:format:onEditingChanged:)](stepper/init(_:value:in:step:format:oneditingchanged:).md)
  Creates a stepper instance that increments and decrements a binding to a value, by a step size and within a closed range that you provide, displaying its value with an applied format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/stepper/init(value:in:step:label:oneditingchanged:))*