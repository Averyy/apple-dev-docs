# textInputBorderShape(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the border shape for text input controls in the view hierarchy.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
nonisolated
func textInputBorderShape(_ shape: TextInputBorderShape) -> some View
```

#### Discussion

Use this modifier to customize the border shape of [`TextField`](../textfield.md) and other text input controls. The shape can be applied to individual controls or to a container to affect all text input controls within it.

In this example, a search field and button both use a capsule shape:

```swift
HStack {
    TextField("Search", text: $searchText)
    Button("Go", action: search)
}
.buttonBorderShape(.capsule)
.textInputBorderShape(.capsule)
```

## Parameters

- `shape`: The shape to use for the border of text input controls.

## See Also

### Managing text entry
- [func autocorrectionDisabled(Bool) -> some View](./autocorrectiondisabled%28_%29.md)
  Sets whether to disable autocorrection for this view.
- [var autocorrectionDisabled: Bool](../environmentvalues/autocorrectiondisabled.md)
  A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [func keyboardType(UIKeyboardType) -> some View](./keyboardtype%28_%29.md)
  Sets the keyboard type for this view.
- [func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View](./scrolldismisseskeyboard%28_%29.md)
  Configures the behavior in which scrollable content interacts with the software keyboard.
- [func textContentType(_:)](./textcontenttype%28_%29.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [func textInputAutocapitalization(TextInputAutocapitalization?) -> some View](./textinputautocapitalization%28_%29.md)
  Sets how often the shift key in the keyboard is automatically enabled.
- [struct TextInputAutocapitalization](../textinputautocapitalization.md)
  The kind of autocapitalization behavior applied during text input.
- [struct TextInputBorderShape](../textinputbordershape.md)
  A shape used to draw the border of a text input control.
- [func textInputCompletion(String) -> some View](./textinputcompletion%28_%29.md)
  Associates a fully formed string with the value of this view when used as a text input suggestion
- [func textInputSuggestions<S>(() -> S) -> some View](./textinputsuggestions%28_%29.md)
  Configures the text input suggestions for this view.
- [func textInputSuggestions<Data, Content>(Data, content: (Data.Element) -> Content) -> some View](./textinputsuggestions%28_,content%29.md)
  Configures the text input suggestions for this view.
- [func textInputSuggestions<Data, ID, Content>(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) -> Content) -> some View](./textinputsuggestions%28_,id,content%29.md)
  Configures the text input suggestions for this view.
- [func textContentType(WKTextContentType?) -> some View](./textcontenttype%28_%29-4dqqb.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on a watchOS device.
- [func textContentType(NSTextContentType?) -> some View](./textcontenttype%28_%29-6fic1.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [func textContentType(UITextContentType?) -> some View](./textcontenttype%28_%29-ufdv.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/textinputbordershape(_:))*