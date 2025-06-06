# init(text:prompt:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a text field with a prompt generated from a `Text`.

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
init(text: Binding<String>, prompt: Text? = nil, @ViewBuilder label: () -> Label)
```

#### Discussion

Use the [`onSubmit(of:_:)`](view/onsubmit(of:_:).md) modifier to invoke an action whenever the user submits this text field.

## Parameters

- `text`: The text to display and edit.
- `prompt`: A   representing the prompt of the text field   which provides users with guidance on what to type into the text   field.
- `label`: A view that describes the purpose of the text field.

## See Also

- [init(_:text:)](textfield/init(_:text:).md)
  Creates a text field with a text label generated from a localized title string.
- [init(_:text:prompt:)](textfield/init(_:text:prompt:).md)
  Creates a text field with a text label generated from a localized title string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(text:prompt:label:))*