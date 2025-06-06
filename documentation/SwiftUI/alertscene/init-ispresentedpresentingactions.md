# init(_:isPresented:presenting:actions:)

**Framework**: SwiftUI  
**Kind**: init

Creates an alert scene, using the given data to produce the alert’s content with a title, and a set of actions. Note that this creates a text view on your behalf.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init<S, T>(_ title: S, isPresented: Binding<Bool>, presenting data: T?, @ViewBuilder actions: (T) -> Actions) where Message == EmptyView, S : StringProtocol
```

## Parameters

- `title`: The title of the alert.
- `isPresented`: A binding to a Boolean value that determines whether to   present the alert. When the user presses or taps one of the alert’s   actions, the system sets this value to   and dismisses.
- `data`: A source of truth that is passed to the alert to   populate the message and actions.
- `actions`: A view builder returning the actions for the dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alertscene/init(_:ispresented:presenting:actions:))*