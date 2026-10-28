# init(_:item:actions:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an alert scene, using the given data to produce the alert’s content with a title, and a set of actions.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@export(implementation)
nonisolated init<T>(_ title: Text, item data: Binding<T?>, @ContentBuilder actions: (T) -> Actions) where Message == EmptyView
```

**Other overloads**:

```swift
@export(implementation)
nonisolated init<S, T>(_ title: S, item data: Binding<T?>, @ContentBuilder actions: (T) -> Actions) where Message == EmptyView, S : StringProtocol
```

```swift
@export(implementation)
nonisolated init<T>(_ titleKey: LocalizedStringKey, item data: Binding<T?>, @ContentBuilder actions: (T) -> Actions) where Message == EmptyView
```

```swift
@export(implementation)
nonisolated init<T>(_ titleResource: LocalizedStringResource, item data: Binding<T?>, @ContentBuilder actions: (T) -> Actions) where Message == EmptyView
```

## Parameters

- `title`: The title of the alert.
- `data`: A binding to optional source of truth for the alert. The system presents the alert when the binding’s value is non-nil. When someone presses or taps one of the alert’s actions, the system sets this value to `nil` and dismisses. The system passes the contents to the alert to populate the message and actions.
- `actions`: A [`ContentBuilder`](../contentbuilder.md) returning the actions for the dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alertscene/init(_:item:actions:)-4zbwj)*