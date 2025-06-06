# init(_:isPresented:presenting:actions:message:)

**Framework**: SwiftUI  
**Kind**: init

Creates an alert scene, using the given data to produce the alert’s content with a title, a set of actions, and a message. Note that this creates a text view on your behalf.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init<S, T>(_ title: S, isPresented: Binding<Bool>, presenting data: T?, @ViewBuilder actions: (T) -> Actions, @ViewBuilder message: (T) -> Message) where S : StringProtocol
```

## Parameters

- `title`: A text string used as the title of the alert.
- `isPresented`: A binding to a Boolean value that determines whether to   present the alert. When the user presses or taps one of the alert’s   actions, the system sets this value to   and dismisses.
- `data`: A source of truth that is passed to the alert to   populate the message and actions.
- `actions`: A view builder returning the actions for the dialog.
- `message`: A view builder returning the message for the dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alertscene/init(_:ispresented:presenting:actions:message:))*