# init(text:selection:prompt:axis:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a text field with a binding to the current selection and a prompt generated from a `Text`.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
init(text: Binding<String>, selection: Binding<TextSelection?>, prompt: Text? = nil, axis: Axis? = nil, @ContentBuilder label: () -> Label)
```

#### Discussion

The following example shows a text field with a binding to the current selection:

```swift
@State private var message: String = ""
@State private var selection: TextSelection? = nil

var body: some View {
    TextField(text: $message, selection: $selection) {
        Text("Message")
    }
}
```

Use the [`onSubmit(of:_:)`](view/onsubmit(of:_:).md) modifier to invoke an action whenever the user submits this text field.

## Parameters

- `text`: The text to display and edit.
- `selection`: A [`Binding`](binding.md) to the variable containing the selection.
- `prompt`: A `Text` representing the prompt of the text field which provides users with guidance on what to type into the text field. Defaults to `nil`.
- `axis`: The axis in which to scroll text when it doesn’t fit in the available space. Defaults to `nil`.
- `label`: A view that describes the purpose of the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfield/init(text:selection:prompt:axis:label:))*