# textInputAutocapitalization(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets how often the shift key in the keyboard is automatically enabled.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func textInputAutocapitalization(_ autocapitalization: TextInputAutocapitalization?) -> some View
```

## Discussion

Use `textInputAutocapitalization(_:)` when you need to automatically capitalize words, sentences, or other text like proper nouns.

In example below, as the user enters text the shift key is automatically enabled before every word:

```swift
TextField("Last, First", text: $fullName)
    .textInputAutocapitalization(.words)
```

The [`TextInputAutocapitalization`](../textinputautocapitalization.md) struct defines the available autocapitalizing behavior. Providing `nil` to  this view modifier does not change the autocapitalization behavior. The default is `TextInputAutocapitalization.sentences`.

## Parameters

- `autocapitalization`: One of the capitalizing behaviors defined in the [`TextInputAutocapitalization`](../textinputautocapitalization.md) struct or nil.

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
- [struct TextInputAutocapitalization](../textinputautocapitalization.md)
  The kind of autocapitalization behavior applied during text input.
- [func textInputBorderShape(TextInputBorderShape) -> some View](./textinputbordershape%28_%29.md)
  Sets the border shape for text input controls in the view hierarchy.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/textinputautocapitalization(_:))*