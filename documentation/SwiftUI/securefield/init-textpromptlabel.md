# init(text:prompt:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a secure field with a prompt generated from a `Text`.

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

Use the [`onSubmit(of:_:)`](view/onsubmit(of:_:).md) modifier to invoke an action whenever someone submits this secure field — for example, by pressing the Return key.

## Parameters

- `text`: A binding to the text that the field displays and edits.
- `prompt`: A   view that represents the secure field’s prompt.   The prompt provides guidance on what people should type into the   secure field.
- `label`: A view that describes the purpose of the secure field.

## See Also

- [init(_:text:)](securefield/init(_:text:).md)
  Creates a secure field with a prompt generated from a `Text`.
- [init(_:text:prompt:)](securefield/init(_:text:prompt:).md)
  Creates a secure field with a prompt generated from a `Text`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/securefield/init(text:prompt:label:))*