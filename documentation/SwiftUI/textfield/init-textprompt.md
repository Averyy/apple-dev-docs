# init(_:text:prompt:)

**Framework**: SwiftUI  
**Kind**: init

Creates a text field with a text label generated from a localized title string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, text: Binding<String>, prompt: Text?)
```

#### Discussion

Use the [`onSubmit(of:_:)`](view/onsubmit(of:_:).md) modifier to invoke an action whenever the user submits this text field.

## Parameters

- `titleKey`: The key for the localized title of the text field,   describing its purpose.
- `text`: The text to display and edit.
- `prompt`: A   representing the prompt of the text field   which provides users with guidance on what to type into the text   field.

## See Also

- [init(_:text:)](textfield/init(_:text:).md)
  Creates a text field with a text label generated from a localized title string.
- [init(text: Binding<String>, prompt: Text?, label: () -> Label)](textfield/init(text:prompt:label:).md)
  Creates a text field with a prompt generated from a `Text`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(_:text:prompt:))*