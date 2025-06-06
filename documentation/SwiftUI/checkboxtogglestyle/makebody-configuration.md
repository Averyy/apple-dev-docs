# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method

Creates a view that represents the body of a toggle checkbox.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency func makeBody(configuration: CheckboxToggleStyle.Configuration) -> some View
```

#### Return Value

A view that represents a checkbox.

#### Discussion

SwiftUI implements this required method of the [`ToggleStyle`](togglestyle.md) protocol to define the behavior and appearance of the [`checkbox`](togglestyle/checkbox.md) toggle style. Don’t call this method directly. Rather, the system calls this method for each [`Toggle`](toggle.md) instance in a view hierarchy that’s styled as a checkbox.

## Parameters

- `configuration`: The properties of the toggle, including a   label and a binding to the toggle’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/checkboxtogglestyle/makebody(configuration:))*