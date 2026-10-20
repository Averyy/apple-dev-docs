# init(_:value:formatter:onEditingChanged:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Create an instance which binds over an arbitrary type, `V`.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Renamed TextField.init(_:value:formatter:onEditingChanged:). Use View.onSubmit(of:_:) for functionality previously provided by the onCommit parameter. Use FocusState<T> and View.focused(_:equals:) for functionality previously provided by the onEditingChanged parameter.

## Declaration

```swift
@export(implementation)
nonisolated init<S, V>(_ title: S, value: Binding<V>, formatter: Formatter, onEditingChanged: @escaping (Bool) -> Void) where S : StringProtocol
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<V>(_ titleKey: LocalizedStringKey, value: Binding<V>, formatter: Formatter, onEditingChanged: @escaping (Bool) -> Void)
```

## Parameters

- `title`: The title of the text field, describing its purpose.
- `value`: The underlying value to be edited.
- `formatter`: A formatter to use when converting between the string the user edits and the underlying value of type `V`. In the event that `formatter` is unable to perform the conversion, `binding.value` isn’t modified.
- `onEditingChanged`: The action to perform when the user begins editing `text` and after the user finishes editing `text`. The closure receives a Boolean value that indicates the editing status: `true` when the user begins editing, `false` when they finish.

## See Also

### Creating a text field with a value
- [init(_:value:formatter:onEditingChanged:onCommit:)](./init%28_,value,formatter,oneditingchanged,oncommit%29.md)
  Create an instance which binds over an arbitrary type, `V`.
- [init(_:value:formatter:onCommit:)](./init%28_,value,formatter,oncommit%29.md)
  Create an instance which binds over an arbitrary type, `V`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(_:value:formatter:oneditingchanged:))*