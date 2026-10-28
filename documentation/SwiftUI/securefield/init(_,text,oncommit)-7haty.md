# init(_:text:onCommit:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [`init(_:text:prompt:)`](./init%28_,text,prompt%29-40n4d.md) instead. Add the [`onSubmit(of:_:)`](../view/onsubmit%28of,_%29.md) view modifier for the `onCommit` behavior.

## Declaration

```swift
nonisolated
init<S>(_ title: S, text: Binding<String>, onCommit: @escaping () -> Void) where S : StringProtocol
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, text: Binding<String>, onCommit: @escaping () -> Void)
```

## Parameters

- `title`: The title of `self`, describing its purpose.
- `text`: The text to display and edit.
- `onCommit`: The action to perform when the user performs an action (usually pressing the Return key) while the secure field has focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/securefield/init(_:text:oncommit:)-7haty)*