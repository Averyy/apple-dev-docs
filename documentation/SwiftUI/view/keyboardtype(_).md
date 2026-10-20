# keyboardType(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

The example below presents a [`TextField`](../textfield.md) to input an email address. Setting the text field’s keyboard type to `.emailAddress` ensures the user can only enter correctly formatted email addresses.

```swift
TextField("someone@example.com", text: $emailAddress)
    .keyboardType(.emailAddress)
```

There are several different kinds of specialized keyboard types available though the [`UIKeyboardType`](../../UIKit/uikeyboardtype.md) enumeration. To specify the default system keyboard type, use `.default`.

![A screenshot showing the use of a specialized keyboard type with a](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-keyboardType@2x.png)

## Parameters

- `type`: One of the keyboard types defined in the [`UIKeyboardType`](../../UIKit/uikeyboardtype.md) enumeration.

## See Also

### Managing text entry
- [func autocorrectionDisabled(Bool) -> some View](./autocorrectiondisabled%28_%29.md)
  Sets whether to disable autocorrection for this view.
- [var autocorrectionDisabled: Bool](../environmentvalues/autocorrectiondisabled.md)
  A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View](./scrolldismisseskeyboard%28_%29.md)
  Configures the behavior in which scrollable content interacts with the software keyboard.
- [func textContentType(_:)](./textcontenttype%28_%29.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [func textInputAutocapitalization(TextInputAutocapitalization?) -> some View](./textinputautocapitalization%28_%29.md)
  Sets how often the shift key in the keyboard is automatically enabled.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/keyboardtype(_:))*