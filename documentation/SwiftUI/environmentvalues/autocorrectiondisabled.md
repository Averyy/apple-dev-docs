# autocorrectionDisabled

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the view hierarchy has auto-correction enabled.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@export(implementation)
var autocorrectionDisabled: Bool { get set }
```

#### Discussion

The default value is `false`.

## See Also

### Managing text entry
- [func autocorrectionDisabled(Bool) -> some View](../view/autocorrectiondisabled%28_%29.md)
  Sets whether to disable autocorrection for this view.
- [func keyboardType(UIKeyboardType) -> some View](../view/keyboardtype%28_%29.md)
  Sets the keyboard type for this view.
- [func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View](../view/scrolldismisseskeyboard%28_%29.md)
  Configures the behavior in which scrollable content interacts with the software keyboard.
- [func textContentType(_:)](../view/textcontenttype%28_%29.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [func textInputAutocapitalization(TextInputAutocapitalization?) -> some View](../view/textinputautocapitalization%28_%29.md)
  Sets how often the shift key in the keyboard is automatically enabled.
- [struct TextInputAutocapitalization](../textinputautocapitalization.md)
  The kind of autocapitalization behavior applied during text input.
- [func textInputBorderShape(TextInputBorderShape) -> some View](../view/textinputbordershape%28_%29.md)
  Sets the border shape for text input controls in the view hierarchy.
- [struct TextInputBorderShape](../textinputbordershape.md)
  A shape used to draw the border of a text input control.
- [func textInputCompletion(String) -> some View](../view/textinputcompletion%28_%29.md)
  Associates a fully formed string with the value of this view when used as a text input suggestion
- [func textInputSuggestions<S>(() -> S) -> some View](../view/textinputsuggestions%28_%29.md)
  Configures the text input suggestions for this view.
- [func textInputSuggestions<Data, Content>(Data, content: (Data.Element) -> Content) -> some View](../view/textinputsuggestions%28_,content%29.md)
  Configures the text input suggestions for this view.
- [func textInputSuggestions<Data, ID, Content>(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) -> Content) -> some View](../view/textinputsuggestions%28_,id,content%29.md)
  Configures the text input suggestions for this view.
- [func textContentType(WKTextContentType?) -> some View](../view/textcontenttype%28_%29-4dqqb.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on a watchOS device.
- [func textContentType(NSTextContentType?) -> some View](../view/textcontenttype%28_%29-6fic1.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [func textContentType(UITextContentType?) -> some View](../view/textcontenttype%28_%29-ufdv.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/autocorrectiondisabled)*