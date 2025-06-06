# init(_:text:onCommit:)

**Framework**: SwiftUI  
**Kind**: init

Creates a text field with a text label generated from a localized title string.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, text: Binding<String>, onCommit: @escaping () -> Void)
```

## Parameters

- `titleKey`: The key for the localized title of the text field,   describing its purpose.
- `text`: The text to display and edit.
- `onCommit`: An action to perform when the user performs an action   (for example, when the user presses the Return key) while the text   field has focus.

## See Also

- [init(_:text:onEditingChanged:onCommit:)](textfield/init(_:text:oneditingchanged:oncommit:).md)
  Creates a text field with a text label generated from a localized title string.
- [init(_:text:onEditingChanged:)](textfield/init(_:text:oneditingchanged:).md)
  Creates a text field with a text label generated from a localized title string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(_:text:oncommit:))*