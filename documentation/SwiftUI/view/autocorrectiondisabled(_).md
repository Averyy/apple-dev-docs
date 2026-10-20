# autocorrectionDisabled(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets whether to disable autocorrection for this view.

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
nonisolated func autocorrectionDisabled(_ disable: Bool = true) -> some View
```

#### Discussion

Use this method when the effect of autocorrection would make it more difficult for the user to input information. The entry of proper names and street addresses are examples where autocorrection can negatively affect the user’s ability complete a data entry task.

The example below configures a [`TextField`](../textfield.md) with the default keyboard. Disabling autocorrection allows the user to enter arbitrary text without the autocorrection system offering suggestions or attempting to override their input.

```swift
TextField("1234 Main St.", text: $address)
    .keyboardType(.default)
    .autocorrectionDisabled(true)
```

## Parameters

- `disable`: A Boolean value that indicates whether autocorrection is disabled for this view. The default value is `true`.

## See Also

### Managing text entry
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/autocorrectiondisabled(_:))*