# init(_:isPresented:presenting:actions:message:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an alert scene, using the given data to produce the alert’s content with a title, a set of actions, and a message.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
init<T>(_ title: Text, isPresented: Binding<Bool>, presenting data: T?, @ContentBuilder actions: (T) -> Actions, @ContentBuilder message: (T) -> Message)
```

**Other overloads**:

```swift
@export(implementation)
nonisolated init<T>(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, presenting data: T?, @ContentBuilder actions: (T) -> Actions, @ContentBuilder message: (T) -> Message)
```

```swift
nonisolated
init<S, T>(_ title: S, isPresented: Binding<Bool>, presenting data: T?, @ContentBuilder actions: (T) -> Actions, @ContentBuilder message: (T) -> Message) where S : StringProtocol
```

```swift
nonisolated
init<T>(_ titleKey: LocalizedStringKey, isPresented: Binding<Bool>, presenting data: T?, @ContentBuilder actions: (T) -> Actions, @ContentBuilder message: (T) -> Message)
```

## Parameters

- `title`: The title of the alert.
- `isPresented`: A binding to a Boolean value that determines whether to present the alert. When someone presses or taps one of the alert’s actions, the system sets this value to `false` and dismisses.
- `data`: A source of truth that is passed to the alert to populate the message and actions.
- `actions`: A [`ContentBuilder`](../contentbuilder.md) returning the actions for the dialog.
- `message`: A [`ContentBuilder`](../contentbuilder.md) returning the message for the dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alertscene/init(_:ispresented:presenting:actions:message:)-7r9as)*