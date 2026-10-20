# init(_:value:in:step:onEditingChanged:)

**Framework**: SwiftUI  
**Kind**: init

Creates a stepper instance that increments and decrements a binding to a value, by a step size and within a closed range that you provide.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@export(implementation)
nonisolated init<V>(_ titleResource: LocalizedStringResource, value: Binding<V>, in bounds: ClosedRange<V>, step: V.Stride = 1, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where V : Strideable
```

#### Discussion

Use `Stepper(_:value:in:step:onEditingChanged:)` to create a stepper that increments or decrements a value within a specific range of values by a specific step size. In the example below, a stepper increments or decrements a binding to value over a range of `1...50` by `5` at each press of the stepper’s increment or decrement buttons:

```swift
struct StepperView: View {
    @State private var value = 0
    @State private var titleKey = "Stepper"

    let step = 5
    let range = 1...50

    var body: some View {
        VStack(spacing: 20) {
            Text("Current Stepper Value: \(value)")
            Stepper(titleKey, value: $value, in: range, step: step)
        }
    }
}
```

![A view displaying a stepper that increments or decrements within a](/images/com.apple.SwiftUI/SwiftUI-Stepper-value-step-range@2x.png)

## Parameters

- `titleResource`: Text resource for the stepper’s localized title describing the purpose of the stepper.
- `value`: A [`Binding`](binding.md) to a value that your provide.
- `bounds`: A closed range that describes the upper and lower bounds permitted by the stepper.
- `step`: The amount to increment or decrement `value` each time the user clicks or taps the stepper’s increment or decrement button, respectively. Defaults to `1`.
- `onEditingChanged`: A closure that’s called when editing begins and ends. For example, on iOS, the user may touch and hold the increment or decrement buttons on a `Stepper` which causes the execution  of the `onEditingChanged` closure at the start and end of the gesture.

## See Also

- [init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () -> Label, onEditingChanged: (Bool) -> Void)](stepper/init(value:in:step:label:oneditingchanged:).md)
  Creates a stepper configured to increment or decrement a binding to a value using a step value and within a range of values you provide.
- [init<F>(value: Binding<F.FormatInput>, in: ClosedRange<F.FormatInput>, step: F.FormatInput.Stride, format: F, label: () -> Label, onEditingChanged: (Bool) -> Void)](stepper/init(value:in:step:format:label:oneditingchanged:).md)
  Creates a stepper configured to increment or decrement a binding to a value using a step value and within a range of values you provide, displaying its value with an applied format style.
- [init(_:value:in:step:format:onEditingChanged:)](stepper/init(_:value:in:step:format:oneditingchanged:).md)
  Creates a stepper instance that increments and decrements a binding to a value, by a step size and within a closed range that you provide, displaying its value with an applied format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/stepper/init(_:value:in:step:oneditingchanged:))*