# init(_:isPresented:actions:message:)

**Framework**: SwiftUI  
**Kind**: init

Creates an alert scene with a title, a set of actions, and a message. Note that this creates a text view on your behalf.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, @ContentBuilder actions: () -> Actions, @ContentBuilder message: () -> Message)
```

## Parameters

- `titleResource`: Text resource for the localized string that is the title of the alert.
- `isPresented`: A binding to a Boolean value that determines whether to present the alert. When someone presses or taps one of the alert’s actions, the system sets this value to `false` and dismisses.
- `actions`: A [`ContentBuilder`](contentbuilder.md) returning the actions for the dialog.
- `message`: A [`ContentBuilder`](contentbuilder.md) returning the message for the dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alertscene/init(_:ispresented:actions:message:))*