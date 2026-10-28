# init(_:onIncrement:onDecrement:onEditingChanged:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a stepper using a title string and that executes closures you provide when the user clicks or taps the stepper’s increment or decrement buttons.

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
init<S>(_ title: S, onIncrement: (() -> Void)?, onDecrement: (() -> Void)?, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where S : StringProtocol
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, onIncrement: (() -> Void)?, onDecrement: (() -> Void)?, onEditingChanged: @escaping (Bool) -> Void = { _ in })
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, onIncrement: (() -> Void)?, onDecrement: (() -> Void)?, onEditingChanged: @escaping (Bool) -> Void = { _ in })
```

## Discussion

Use `Stepper(_:onIncrement:onDecrement:onEditingChanged:)` to create a control with a custom title that executes closures you provide when the user clicks or taps on the stepper’s increment or decrement buttons.

The example below uses an array that holds a number of [`Color`](../color.md) values, a local state variable, `value`, to set the control’s background color, and title label. When the user clicks or taps on the stepper’s increment or decrement buttons SwiftUI executes the relevant closure that updates `value`, wrapping the `value` to prevent overflow. SwiftUI then re-renders the view, updating the text and background color to match the current index:

```swift
struct StepperView: View {
    @State private var value = 0
    let title: String
    let colors: [Color] = [.orange, .red, .gray, .blue, .green,
                           .purple, .pink]

    func incrementStep() {
        value += 1
        if value >= colors.count { value = 0 }
    }

    func decrementStep() {
        value -= 1
        if value < 0 { value = colors.count - 1 }
    }

    var body: some View {
        Stepper(title, onIncrement: incrementStep, onDecrement: decrementStep)
            .padding(5)
            .background(colors[value])
    }
}
```

![A view displaying a stepper that uses a string for the stepper’s title](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-Stepper-increment-decrement-closures@2x.png)

## Parameters

- `title`: A string describing the purpose of the stepper.
- `onIncrement`: The closure to execute when the user clicks or taps the control’s plus button.
- `onDecrement`: The closure to execute when the user clicks or taps the control’s minus button.
- `onEditingChanged`: A closure that’s called when editing begins and ends. For example, on iOS, the user may touch and hold the increment or decrement buttons on a `Stepper` which causes the execution of the `onEditingChanged` closure at the start and end of the gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/stepper/init(_:onincrement:ondecrement:oneditingchanged:)-42t6m)*