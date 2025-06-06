# init(label:onIncrement:onDecrement:onEditingChanged:)

**Framework**: SwiftUI  
**Kind**: init

Creates a stepper instance that performs the closures you provide when the user increments or decrements the stepper.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(@ViewBuilder label: () -> Label, onIncrement: (() -> Void)?, onDecrement: (() -> Void)?, onEditingChanged: @escaping (Bool) -> Void = { _ in })
```

#### Discussion

Use this initializer to create a control with a custom title that executes closures you provide when the user clicks or taps the stepper’s increment or decrement buttons.

The example below uses an array that holds a number of [`Color`](color.md) values, a local state variable, `value`, to set the control’s background color, and title label. When the user clicks or taps on the stepper’s increment or decrement buttons SwiftUI executes the relevant closure that updates `value`, wrapping the `value` to prevent overflow. SwiftUI then re-renders the view, updating the text and background color to match the current index:

```swift
struct StepperView: View {
    @State private var value = 0
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
        Stepper {
            Text("Value: \(value) Color: \(colors[value].description)")
        } onIncrement: {
            incrementStep()
        } onDecrement: {
            decrementStep()
        }
        .padding(5)
        .background(colors[value])
    }
```

}

![A view displaying a stepper that uses a text view for stepper’s title](https://docs-assets.developer.apple.com/published/454b319c800c954fe79070014aaa7d83/SwiftUI-Stepper-increment-decrement-closures%402x.png)

## Parameters

- `label`: A view describing the purpose of this stepper.
- `onIncrement`: The closure to execute when the user clicks or taps   the control’s plus button.
- `onDecrement`: The closure to execute when the user clicks or taps   the control’s minus button.
- `onEditingChanged`: A closure called when editing begins and ends.   For example, on iOS, the user may touch and hold the increment   or decrement buttons on a   which causes the execution   of the   closure at the start and end of   the gesture.

## See Also

- [init(_:onIncrement:onDecrement:onEditingChanged:)](stepper/init(_:onincrement:ondecrement:oneditingchanged:).md)
  Creates a stepper that uses a title key and executes the closures you provide when the user clicks or taps the stepper’s increment and decrement buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/stepper/init(label:onincrement:ondecrement:oneditingchanged:))*