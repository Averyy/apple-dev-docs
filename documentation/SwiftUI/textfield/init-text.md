# init(_:text:)

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
init(_ titleKey: LocalizedStringKey, text: Binding<String>)
```

## Parameters

- `titleKey`: The key for the localized title of the text field,   describing its purpose.
- `text`: The text to display and edit.

## See Also

- [init(_:text:prompt:)](textfield/init(_:text:prompt:).md)
  Creates a text field with a text label generated from a localized title string.
- [init(text: Binding<String>, prompt: Text?, label: () -> Label)](textfield/init(text:prompt:label:).md)
  Creates a text field with a prompt generated from a `Text`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(_:text:))*