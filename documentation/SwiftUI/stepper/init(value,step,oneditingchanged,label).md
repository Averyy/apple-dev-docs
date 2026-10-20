# init(value:step:onEditingChanged:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a stepper configured to increment or decrement a binding to a value using a step value you provide.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: Stepper(value:step:label:onEditingChanged:))
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: Stepper(value:step:label:onEditingChanged:))
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: Stepper(value:step:label:onEditingChanged:))
- macOS 10.15+ - Deprecated in 27.2 (renamed: Stepper(value:step:label:onEditingChanged:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: Stepper(value:step:label:onEditingChanged:))
- watchOS 9.0+ - Deprecated in 27.2 (renamed: Stepper(value:step:label:onEditingChanged:))

> **Deprecated**: Use [`init(value:step:label:onEditingChanged:)`](./init%28value,step,label,oneditingchanged%29.md) instead.

## Declaration

```swift
nonisolated
init<V>(value: Binding<V>, step: V.Stride = 1, onEditingChanged: @escaping (Bool) -> Void = { _ in }, @ContentBuilder label: () -> Label) where V : Strideable
```

Available when `Label` conforms to `View`.

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

![A view displaying a stepper that increments or decrements a value by a specified amount each time the user clicks or taps the stepper’s increment or decrement buttons.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-Stepper-value-step@2x.png)

## Parameters

- `value`: The [`Binding`](../binding.md) to a value that you provide.
- `step`: The amount to increment or decrement `value` each time the user clicks or taps the stepper’s increment or decrement buttons. Defaults to `1`.
- `onEditingChanged`: A closure that’s called when editing begins and ends. For example, on iOS, the user may touch and hold the increment or decrement buttons on a stepper which causes the execution of the `onEditingChanged` closure at the start and end of the gesture.
- `label`: A view describing the purpose of this stepper.

## See Also

### Deprecated
- [init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, onEditingChanged: (Bool) -> Void, label: () -> Label)](./init%28value,in,step,oneditingchanged,label%29.md)
  Creates a stepper configured to increment or decrement a binding to a value using a step value and within a range of values you provide.
- [init(onIncrement: (() -> Void)?, onDecrement: (() -> Void)?, onEditingChanged: (Bool) -> Void, label: () -> Label)](./init%28onincrement,ondecrement,oneditingchanged,label%29.md)
  Creates a stepper instance that performs the closures you provide when the user increments or decrements the stepper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/stepper/init(value:step:oneditingchanged:label:))*