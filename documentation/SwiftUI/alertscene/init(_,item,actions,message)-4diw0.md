# init(_:item:actions:message:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an alert scene, using the given data to produce the alert’s content with a title, a set of actions, and a message. Note that this creates a text view on your behalf.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@export(implementation)
nonisolated init<T>(_ titleResource: LocalizedStringResource, item data: Binding<T?>, @ContentBuilder actions: (T) -> Actions, @ContentBuilder message: (T) -> Message)
```

**Other overloads**:

```swift
@export(implementation)
nonisolated init<S, T>(_ title: S, item data: Binding<T?>, @ContentBuilder actions: (T) -> Actions, @ContentBuilder message: (T) -> Message) where S : StringProtocol
```

```swift
@export(implementation)
nonisolated init<T>(_ title: Text, item data: Binding<T?>, @ContentBuilder actions: (T) -> Actions, @ContentBuilder message: (T) -> Message)
```

```swift
@export(implementation)
nonisolated init<T>(_ titleKey: LocalizedStringKey, item data: Binding<T?>, @ContentBuilder actions: (T) -> Actions, @ContentBuilder message: (T) -> Message)
```

## Parameters

- `titleResource`: Text resource for the localized string that is the title of the alert.
- `data`: A binding to optional source of truth for the alert. The system presents the alert when the binding’s value is non-nil. When someone presses or taps one of the alert’s actions, the system sets this value to `nil` and dismisses. The system passes the contents to the alert to populate the message and actions.
- `actions`: A [`ContentBuilder`](../contentbuilder.md) returning the actions for the dialog.
- `message`: A [`ContentBuilder`](../contentbuilder.md) returning the message for the dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alertscene/init(_:item:actions:message:)-4diw0)*