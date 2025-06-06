# textInputAutocapitalization(_:)

**Framework**: SwiftUI  
**Kind**: method

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

#### Discussion

Use `textInputAutocapitalization(_:)` when you need to automatically capitalize words, sentences, or other text like proper nouns.

In example below, as the user enters text the shift key is automatically enabled before every word:

```swift
TextField("Last, First", text: $fullName)
    .textInputAutocapitalization(.words)
```

The [`TextInputAutocapitalization`](textinputautocapitalization.md) struct defines the available autocapitalizing behavior. Providing `nil` to  this view modifier does not change the autocapitalization behavior. The default is `TextInputAutocapitalization.sentences`.

## Parameters

- `autocapitalization`: One of the capitalizing behaviors   defined in the   struct or nil.

## See Also

- [func autocorrectionDisabled(Bool) -> some View](view/autocorrectiondisabled(_:).md)
  Sets whether to disable autocorrection for this view.
- [var autocorrectionDisabled: Bool](environmentvalues/autocorrectiondisabled.md)
  A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [func keyboardType(UIKeyboardType) -> some View](view/keyboardtype(_:).md)
  Sets the keyboard type for this view.
- [func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View](view/scrolldismisseskeyboard(_:).md)
  Configures the behavior in which scrollable content interacts with the software keyboard.
- [func textContentType(_:)](view/textcontenttype(_:).md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [struct TextInputAutocapitalization](textinputautocapitalization.md)
  The kind of autocapitalization behavior applied during text input.
- [func textInputCompletion(String) -> some View](view/textinputcompletion(_:).md)
  Associates a fully formed string with the value of this view when used as a text input suggestion
- [func textInputSuggestions<S>(() -> S) -> some View](view/textinputsuggestions(_:).md)
  Configures the text input suggestions for this view.
- [func textInputSuggestions<Data, Content>(Data, content: (Data.Element) -> Content) -> some View](view/textinputsuggestions(_:content:).md)
  Configures the text input suggestions for this view.
- [func textInputSuggestions<Data, ID, Content>(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) -> Content) -> some View](view/textinputsuggestions(_:id:content:).md)
  Configures the text input suggestions for this view.
- [func textContentType(WKTextContentType?) -> some View](view/textcontenttype(_:)-4dqqb.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on a watchOS device.
- [func textContentType(NSTextContentType?) -> some View](view/textcontenttype(_:)-6fic1.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [func textContentType(UITextContentType?) -> some View](view/textcontenttype(_:)-ufdv.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/textinputautocapitalization(_:))*