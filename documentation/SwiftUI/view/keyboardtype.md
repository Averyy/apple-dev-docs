# keyboardType(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the keyboard type for this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func keyboardType(_ type: UIKeyboardType) -> some View
```

#### Discussion

Use `keyboardType(_:)` to specify the keyboard type to use for text entry. A number of different keyboard types are available to meet specialized input needs, such as entering email addresses or phone numbers.

The example below presents a [`TextField`](textfield.md) to input an email address. Setting the text field’s keyboard type to `.emailAddress` ensures the user can only enter correctly formatted email addresses.

```swift
TextField("someone@example.com", text: $emailAddress)
    .keyboardType(.emailAddress)
```

There are several different kinds of specialized keyboard types available though the [`UIKeyboardType`](https://developer.apple.com/documentation/UIKit/UIKeyboardType) enumeration. To specify the default system keyboard type, use `.default`.

![A screenshot showing the use of a specialized keyboard type with a](https://docs-assets.developer.apple.com/published/5a18abb1297dad5b4d3fa9a1616ef97c/SwiftUI-View-keyboardType%402x.png)

## Parameters

- `type`: One of the keyboard types defined in the    enumeration.

## See Also

- [func autocorrectionDisabled(Bool) -> some View](view/autocorrectiondisabled(_:).md)
  Sets whether to disable autocorrection for this view.
- [var autocorrectionDisabled: Bool](environmentvalues/autocorrectiondisabled.md)
  A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View](view/scrolldismisseskeyboard(_:).md)
  Configures the behavior in which scrollable content interacts with the software keyboard.
- [func textContentType(_:)](view/textcontenttype(_:).md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [func textInputAutocapitalization(TextInputAutocapitalization?) -> some View](view/textinputautocapitalization(_:).md)
  Sets how often the shift key in the keyboard is automatically enabled.
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
- [struct TextInputFormattingControlPlacement](textinputformattingcontrolplacement.md)
  A structure defining the system text formatting controls available on each platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/keyboardtype(_:))*