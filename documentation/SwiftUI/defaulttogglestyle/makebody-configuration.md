# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method

Creates a view that represents the body of a toggle.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency func makeBody(configuration: DefaultToggleStyle.Configuration) -> some View
```

#### Return Value

A view that acts as a toggle.

#### Discussion

SwiftUI implements this required method of the [`ToggleStyle`](togglestyle.md) protocol to define the behavior and appearance of the [`automatic`](togglestyle/automatic.md) toggle style. Don’t call this method directly. Rather, the system calls this method for each [`Toggle`](toggle.md) instance in a view hierarchy that needs the default style.

## Parameters

- `configuration`: The properties of the toggle, including a   label and a binding to the toggle’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/defaulttogglestyle/makebody(configuration:))*