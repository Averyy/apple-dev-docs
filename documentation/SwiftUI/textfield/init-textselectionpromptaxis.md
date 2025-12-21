# init(_:text:selection:prompt:axis:)

**Framework**: SwiftUI  
**Kind**: init

Creates a text field with a binding to the current selection and a text label generated from a localized title string.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, text: Binding<String>, selection: Binding<TextSelection?>, prompt: Text? = nil, axis: Axis? = nil)
```

#### Discussion

The following example shows a text field with a binding to the current selection:

```swift
@State private var message: String = ""
@State private var selection: TextSelection? = nil

var body: some View {
    TextField(
        "Message",
        text: $message,
        selection: $selection
    )
}
```

Use the [`onSubmit(of:_:)`](view/onsubmit(of:_:).md) modifier to invoke an action whenever the user submits this text field.

## Parameters

- `titleKey`: The key for the localized title of the text field,   describing its purpose.
- `text`: The text to display and edit.
- `selection`: A   to the variable containing the selection.
- `prompt`: A   representing the prompt of the text field   which provides users with guidance on what to type into the text   field. Defaults to  .
- `axis`: The axis in which to scroll text when it doesn’t fit   in the available space. Defaults to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(_:text:selection:prompt:axis:))*