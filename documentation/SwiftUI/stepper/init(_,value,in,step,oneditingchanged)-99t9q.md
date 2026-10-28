# init(_:value:in:step:onEditingChanged:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<V>(_ titleResource: LocalizedStringResource, value: Binding<V>, in bounds: ClosedRange<V>, step: V.Stride = 1, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where V : Strideable
```

```swift
nonisolated
init<V>(_ titleKey: LocalizedStringKey, value: Binding<V>, in bounds: ClosedRange<V>, step: V.Stride = 1, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where V : Strideable
```

## Discussion

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

![A view displaying a stepper that increments or decrements within a](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-Stepper-value-step-range@2x.png)

## Parameters

- `title`: A string describing the purpose of the stepper.
- `value`: A [`Binding`](../binding.md) to a value that your provide.
- `bounds`: A closed range that describes the upper and lower bounds permitted by the stepper.
- `step`: The amount to increment or decrement `value` each time the user clicks or taps the stepper’s increment or decrement button, respectively. Defaults to `1`.
- `onEditingChanged`: A closure that’s called when editing begins and ends. For example, on iOS, the user may touch and hold the increment or decrement buttons on a `Stepper` which causes the execution of the `onEditingChanged` closure at the start and end of the gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/stepper/init(_:value:in:step:oneditingchanged:)-99t9q)*