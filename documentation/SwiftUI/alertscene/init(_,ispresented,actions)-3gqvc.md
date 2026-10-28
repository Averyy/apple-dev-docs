# init(_:isPresented:actions:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an alert scene with a title and a set of actions.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
init(_ title: Text, isPresented: Binding<Bool>, @ContentBuilder actions: () -> Actions) where Message == EmptyView
```

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, @ContentBuilder actions: () -> Actions) where Message == EmptyView
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, isPresented: Binding<Bool>, @ContentBuilder actions: () -> Actions) where Message == EmptyView
```

```swift
nonisolated
init<S>(_ title: S, isPresented: Binding<Bool>, @ContentBuilder actions: () -> Actions) where Message == EmptyView, S : StringProtocol
```

## Parameters

- `title`: The title of the alert.
- `isPresented`: A binding to a Boolean value that determines whether to present the alert. When someone presses or taps one of the alert’s actions, the system sets this value to `false` and dismisses.
- `actions`: A [`ContentBuilder`](../contentbuilder.md) returning the actions for the dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alertscene/init(_:ispresented:actions:)-3gqvc)*