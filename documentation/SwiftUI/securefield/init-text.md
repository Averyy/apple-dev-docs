# init(_:text:)

**Framework**: SwiftUI  
**Kind**: init

Creates a secure field with a prompt generated from a `Text`.

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
init(_ titleKey: LocalizedStringKey, text: Binding<String>)
```

#### Discussion

Use the [`onSubmit(of:_:)`](view/onsubmit(of:_:).md) modifier to invoke an action whenever someone submits this secure field — for example, by pressing the Return key.

## Parameters

- `titleKey`: The key for the field’s localized title. The title   describes the purpose of the field.
- `text`: A binding to the text that the field displays and edits.

## See Also

- [init(_:text:prompt:)](securefield/init(_:text:prompt:).md)
  Creates a secure field with a prompt generated from a `Text`.
- [init(text: Binding<String>, prompt: Text?, label: () -> Label)](securefield/init(text:prompt:label:).md)
  Creates a secure field with a prompt generated from a `Text`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/securefield/init(_:text:))*