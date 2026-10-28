# init(_:text:onEditingChanged:onCommit:)

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

> **Deprecated**: Use [`init(_:text:prompt:)`](./init%28_,text,prompt%29-4kzyv.md) instead. Add the [`onSubmit(of:_:)`](../view/onsubmit%28of,_%29.md) view modifier for the `onCommit` behavior. Use [`FocusState`](../focusstate.md) and [`focused(_:equals:)`](../view/focused%28_,equals%29.md) for the `onEditingChanged` behavior.

## Declaration

```swift
nonisolated
init<S>(_ title: S, text: Binding<String>, onEditingChanged: @escaping (Bool) -> Void, onCommit: @escaping () -> Void) where S : StringProtocol
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, text: Binding<String>, onEditingChanged: @escaping (Bool) -> Void, onCommit: @escaping () -> Void)
```

## Parameters

- `title`: The title of the text view, describing its purpose.
- `text`: The text to display and edit.
- `onEditingChanged`: The action to perform when the user begins editing `text` and after the user finishes editing `text`. The closure receives a Boolean value that indicates the editing status: `true` when the user begins editing, `false` when they finish.
- `onCommit`: An action to perform when the user performs an action (for example, when the user presses the Return key) while the text field has focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(_:text:oneditingchanged:oncommit:)-588cl)*