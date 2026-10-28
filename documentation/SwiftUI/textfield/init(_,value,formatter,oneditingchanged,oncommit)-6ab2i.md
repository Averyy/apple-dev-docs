# init(_:value:formatter:onEditingChanged:onCommit:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance which binds over an arbitrary type, `T`.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [`init(_:value:formatter:prompt:)`](./init%28_,value,formatter,prompt%29-8kpfa.md) instead. Add the [`onSubmit(of:_:)`](../view/onsubmit%28of,_%29.md) view modifier for the `onCommit` behavior. Use [`FocusState`](../focusstate.md) and [`focused(_:equals:)`](../view/focused%28_,equals%29.md) for the `onEditingChanged` behavior.

## Declaration

```swift
nonisolated
init<V>(_ titleKey: LocalizedStringKey, value: Binding<V>, formatter: Formatter, onEditingChanged: @escaping (Bool) -> Void, onCommit: @escaping () -> Void)
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
nonisolated
init<S, V>(_ title: S, value: Binding<V>, formatter: Formatter, onEditingChanged: @escaping (Bool) -> Void, onCommit: @escaping () -> Void) where S : StringProtocol
```

## Parameters

- `titleKey`: The key for the localized title of the text field, describing its purpose.
- `value`: The underlying value to be edited.
- `formatter`: A formatter to use when converting between the string the user edits and the underlying value of type `T`. In the event that `formatter` is unable to perform the conversion, `binding.value` isn’t modified.
- `onEditingChanged`: The action to perform when the user begins editing `text` and after the user finishes editing `text`. The closure receives a Boolean value that indicates the editing status: `true` when the user begins editing, `false` when they finish.
- `onCommit`: An action to perform when the user performs an action (for example, when the user presses the Return key) while the text field has focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(_:value:formatter:oneditingchanged:oncommit:)-6ab2i)*