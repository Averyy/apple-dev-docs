# confirmationDialog(_:item:titleVisibility:actions:message:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a confirmation dialog with a message using data to produce the dialog’s content and a localized string resource for the title.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@export(implementation)
nonisolated func confirmationDialog<A, M, T>(_ titleResource: LocalizedStringResource, item data: Binding<T?>, titleVisibility: Visibility = .automatic, @ContentBuilder actions: (T) -> A, @ContentBuilder message: (T) -> M) -> some View where A : View, M : View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func confirmationDialog<A, M, T>(_ title: Text, item data: Binding<T?>, titleVisibility: Visibility = .automatic, @ContentBuilder actions: (T) -> A, @ContentBuilder message: (T) -> M) -> some View where A : View, M : View
```

```swift
@export(implementation)
nonisolated func confirmationDialog<A, M, T>(_ titleKey: LocalizedStringKey, item data: Binding<T?>, titleVisibility: Visibility = .automatic, @ContentBuilder actions: (T) -> A, @ContentBuilder message: (T) -> M) -> some View where A : View, M : View
```

```swift
@export(implementation)
nonisolated func confirmationDialog<S, A, M, T>(_ title: S, item data: Binding<T?>, titleVisibility: Visibility = .automatic, @ContentBuilder actions: (T) -> A, @ContentBuilder message: (T) -> M) -> some View where S : StringProtocol, A : View, M : View
```

## Parameters

- `titleResource`: Text resource for the localized string that describes the title of the dialog.
- `data`: A binding to optional source of truth for the confirmation dialog. The system presents the dialog when the binding’s value is non-nil. When the user presses or taps the dialog’s default action button, the system sets this value to `nil` and dismisses. The system passes the contents to the modifier’s closures. You use this data to populate the fields of a confirmation dialog that you create that the system displays to the user.
- `titleVisibility`: The visibility of the dialog’s title. The default value is [`Visibility.automatic`](../visibility/automatic.md).
- `actions`: A [`ContentBuilder`](../contentbuilder.md) returning the dialog’s actions given the currently available data.
- `message`: A [`ContentBuilder`](../contentbuilder.md) returning the message for the dialog given the currently available data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/confirmationdialog(_:item:titlevisibility:actions:message:)-8tfy5)*