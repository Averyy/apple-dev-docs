# init(_:text:onCommit:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a text field with a text label generated from a title string.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Renamed TextField.init(_:text:onEditingChanged:). Use View.onSubmit(of:_:) for functionality previously provided by the onCommit parameter. Use FocusState<T> and View.focused(_:equals:) for functionality previously provided by the onEditingChanged parameter.

## Declaration

```swift
@export(implementation)
nonisolated init<S>(_ title: S, text: Binding<String>, onCommit: @escaping () -> Void) where S : StringProtocol
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleKey: LocalizedStringKey, text: Binding<String>, onCommit: @escaping () -> Void)
```

## Parameters

- `title`: The title of the text view, describing its purpose.
- `text`: The text to display and edit.
- `onCommit`: An action to perform when the user performs an action (for example, when the user presses the Return key) while the text field has focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(_:text:oncommit:)-1zeco)*