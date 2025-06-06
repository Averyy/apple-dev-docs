# init(_:isPresented:actions:message:)

**Framework**: SwiftUI  
**Kind**: init

Creates an alert scene with a title, a set of actions, and a message.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init(_ title: Text, isPresented: Binding<Bool>, @ViewBuilder actions: () -> Actions, @ViewBuilder message: () -> Message)
```

## Parameters

- `title`: The title of the alert.
- `isPresented`: A binding to a Boolean value that determines whether to   present the alert. When the user presses or taps one of the alert’s   actions, the system sets this value to   and dismisses.
- `actions`: A view builder returning the actions for the dialog.
- `message`: A view builder returning the message for the dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alertscene/init(_:ispresented:actions:message:))*