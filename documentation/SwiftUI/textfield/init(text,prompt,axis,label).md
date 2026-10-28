# init(text:prompt:axis:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a text field with a preferred axis and a prompt generated from a `Text`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init(text: Binding<String>, prompt: Text? = nil, axis: Axis, @ContentBuilder label: () -> Label)
```

Available when `Label` conforms to `View`.

## Discussion

Specify a preferred axis in which the text field should scroll its content when it does not fit in the available space. Depending on the style of the field, this axis may not be respected.

Use the [`onSubmit(of:_:)`](../view/onsubmit%28of,_%29.md) modifier to invoke an action whenever the user submits this text field.

## Parameters

- `text`: The text to display and edit.
- `prompt`: A `Text` representing the prompt of the text field which provides users with guidance on what to type into the text field.
- `axis`: The axis in which to scroll text when it doesn’t fit in the available space.
- `label`: A view that describes the purpose of the text field.

## See Also

### Creating a scrollable text field
- [init(_:text:axis:)](./init%28_,text,axis%29.md)
  Creates a text field with a preferred axis and a text label generated from a localized title string resource.
- [init(_:text:prompt:axis:)](./init%28_,text,prompt,axis%29.md)
  Creates a text field with a preferred axis and a text label generated from a localized title string resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(text:prompt:axis:label:))*