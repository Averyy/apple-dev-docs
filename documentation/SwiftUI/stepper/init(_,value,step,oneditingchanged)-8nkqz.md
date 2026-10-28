# init(_:value:step:onEditingChanged:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<V>(_ titleResource: LocalizedStringResource, value: Binding<V>, step: V.Stride = 1, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where V : Strideable
```

```swift
nonisolated
init<V>(_ titleKey: LocalizedStringKey, value: Binding<V>, step: V.Stride = 1, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where V : Strideable
```

## Discussion

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

![A view displaying a stepper that increments or decrements by 1 each](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-Stepper-value-step@2x.png)

## Parameters

- `title`: A string describing the purpose of the stepper.
- `value`: The [`Binding`](../binding.md) to a value that you provide.
- `step`: The amount to increment or decrement `value` each time the user clicks or taps the stepper’s increment or decrement button, respectively. Defaults to `1`.
- `onEditingChanged`: A closure that’s called when editing begins and ends. For example, on iOS, the user may touch and hold the increment or decrement buttons on a `Stepper` which causes the execution of the `onEditingChanged` closure at the start and end of the gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/stepper/init(_:value:step:oneditingchanged:)-8nkqz)*