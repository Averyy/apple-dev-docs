# init(value:in:step:onEditingChanged:label:)

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
init<V>(value: Binding<V>, in bounds: ClosedRange<V>, step: V.Stride = 1, onEditingChanged: @escaping (Bool) -> Void = { _ in }, @ViewBuilder label: () -> Label) where V : Strideable
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

![A view displaying a stepper with a step size of five, and a prescribed range of 1 though 50.](https://docs-assets.developer.apple.com/published/21941a9c414c8460cb45d5d7d33ce928/SwiftUI-Stepper-value-step-range%402x.png)

## Parameters

- `value`: A   to a value that you provide.
- `bounds`: A closed range that describes the upper and lower bounds   permitted by the stepper.
- `step`: The amount to increment or decrement the stepper when the   user clicks or taps the stepper’s increment or decrement buttons,   respectively.
- `onEditingChanged`: A closure that’s called when editing begins and   ends. For example, on iOS, the user may touch and hold the increment   or decrement buttons on a stepper which causes the execution   of the   closure at the start and end of   the gesture.
- `label`: A view describing the purpose of this stepper.

## See Also

- [init<V>(value: Binding<V>, step: V.Stride, onEditingChanged: (Bool) -> Void, label: () -> Label)](stepper/init(value:step:oneditingchanged:label:).md)
  Creates a stepper configured to increment or decrement a binding to a value using a step value you provide.
- [init(onIncrement: (() -> Void)?, onDecrement: (() -> Void)?, onEditingChanged: (Bool) -> Void, label: () -> Label)](stepper/init(onincrement:ondecrement:oneditingchanged:label:).md)
  Creates a stepper instance that performs the closures you provide when the user increments or decrements the stepper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/stepper/init(value:in:step:oneditingchanged:label:))*