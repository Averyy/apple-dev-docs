# textInputFormattingControlVisibility(_:for:)

**Framework**: SwiftUI  
**Kind**: method

Specifies which system text formatting controls are available for people to format text.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
nonisolated
func textInputFormattingControlVisibility(_ visibility: Visibility, for placement: TextInputFormattingControlPlacement.Set) -> some View
```

#### Discussion

A [`TextEditor`](texteditor.md) with a binding to an `AttributedString` offers built-in controls for formatting text. These controls appear in different placements depending on the platform. By default, `TextEditor` shows them in the context menu and in the keyboard toolbar on iOS. See [`TextInputFormattingControlPlacement.Set`](textinputformattingcontrolplacement/set.md) for the available placements.

In this example, the formatting accessory bar is shown in a macOS editor:

```swift
struct StyledTextEditingView: View {
    @State private var text: AttributedString = ""

    var body: some View {
        TextEditor(text: $text)
            .textInputFormattingControlVisibility(.visible, for: .accessoryBar)
    }
}
```

## Parameters

- `visibility`: Whether the controls in the given placements may become visible.
- `placement`: The onscreen control to modify.

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
- [func textInputAutocapitalization(TextInputAutocapitalization?) -> some View](view/textinputautocapitalization(_:).md)
  Sets how often the shift key in the keyboard is automatically enabled.
- [struct TextInputAutocapitalization](textinputautocapitalization.md)
  The kind of autocapitalization behavior applied during text input.
- [func textInputBorderShape(TextInputBorderShape) -> some View](view/textinputbordershape(_:).md)
  Sets the border shape for text input controls in the view hierarchy.
- [struct TextInputBorderShape](textinputbordershape.md)
  A shape used to draw the border of a text input control.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/textinputformattingcontrolvisibility(_:for:))*