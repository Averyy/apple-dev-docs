# init(value:step:onEditingChanged:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a stepper configured to increment or decrement a binding to a value using a step value you provide.

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
init<V>(value: Binding<V>, step: V.Stride = 1, onEditingChanged: @escaping (Bool) -> Void = { _ in }, @ViewBuilder label: () -> Label) where V : Strideable
```

#### Discussion

Use this initializer to create a stepper that increments or decrements a bound value by a specific amount each time the user clicks or taps the stepper’s increment or decrement buttons.

In the example below, a stepper increments or decrements `value` by the `step` value of 5 at each click or tap of the control’s increment or decrement button:

```swift
struct StepperView: View {
    @State private var value = 1
    let step = 5
    var body: some View {
        Stepper(value: $value,
                step: step) {
            Text("Current value: \(value), step: \(step)")
        }
            .padding(10)
    }
}
```

![A view displaying a stepper that increments or decrements a value by a specified amount each time the user clicks or taps the stepper’s increment or decrement buttons.](https://docs-assets.developer.apple.com/published/a85ed9351b703c8cc865d291ef62b2e9/SwiftUI-Stepper-value-step%402x.png)

## Parameters

- `value`: The   to a value that you provide.
- `step`: The amount to increment or decrement   each time the   user clicks or taps the stepper’s increment or decrement buttons.   Defaults to  .
- `onEditingChanged`: A closure that’s called when editing begins and   ends. For example, on iOS, the user may touch and hold the increment   or decrement buttons on a stepper which causes the execution   of the   closure at the start and end of   the gesture.
- `label`: A view describing the purpose of this stepper.

## See Also

- [init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, onEditingChanged: (Bool) -> Void, label: () -> Label)](stepper/init(value:in:step:oneditingchanged:label:).md)
  Creates a stepper configured to increment or decrement a binding to a value using a step value and within a range of values you provide.
- [init(onIncrement: (() -> Void)?, onDecrement: (() -> Void)?, onEditingChanged: (Bool) -> Void, label: () -> Label)](stepper/init(onincrement:ondecrement:oneditingchanged:label:).md)
  Creates a stepper instance that performs the closures you provide when the user increments or decrements the stepper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/stepper/init(value:step:oneditingchanged:label:))*