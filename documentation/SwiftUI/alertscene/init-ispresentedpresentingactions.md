# init(_:isPresented:presenting:actions:)

**Framework**: SwiftUI  
**Kind**: init

Creates an alert scene, using the given data to produce the alert’s content with a title, and a set of actions. Note that this creates a text view on your behalf.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@export(implementation)
nonisolated init<T>(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, presenting data: T?, @ContentBuilder actions: (T) -> Actions) where Message == EmptyView
```

## Parameters

- `titleResource`: The title of the alert.
- `isPresented`: A binding to a Boolean value that determines whether to present the alert. When someone presses or taps one of the alert’s actions, the system sets this value to `false` and dismisses.
- `data`: A source of truth that is passed to the alert to populate the message and actions.
- `actions`: A [`ContentBuilder`](contentbuilder.md) returning the actions for the dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alertscene/init(_:ispresented:presenting:actions:))*