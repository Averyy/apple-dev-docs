# init(text:prompt:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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
init(text: Binding<String>, prompt: Text? = nil, @ContentBuilder label: () -> Label)
```

Available when `Label` conforms to `View`.

## Discussion

Use the [`onSubmit(of:_:)`](../view/onsubmit%28of,_%29.md) modifier to invoke an action whenever the user submits this text field.

## Parameters

- `text`: The text to display and edit.
- `prompt`: A `Text` representing the prompt of the text field which provides users with guidance on what to type into the text field.
- `label`: A view that describes the purpose of the text field.

## See Also

### Creating a text field with a string
- [init(_:text:)](./init%28_,text%29.md)
  Creates a text field with a text label generated from a localized title string.
- [init(_:text:prompt:)](./init%28_,text,prompt%29.md)
  Creates a text field with a text label generated from a localized title string resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(text:prompt:label:))*