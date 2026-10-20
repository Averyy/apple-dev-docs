# TextFieldStyle

**Framework**: SwiftUI  
**Kind**: protocol  
**Role**: Protocol

A specification for the appearance and interaction of a text field.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol TextFieldStyle
```

## Topics

### Getting built-in text field styles
- [static var automatic: DefaultTextFieldStyle](./textfieldstyle/automatic.md)
  The default text field style, based on the text field’s context.
- [static var bordered: BorderedTextFieldStyle](./textfieldstyle/bordered.md)
  A text field style with a system-defined border whose shape is determined by the [`textInputBorderShape(_:)`](./view/textinputbordershape%28_%29.md) modifier.
- [static var plain: PlainTextFieldStyle](./textfieldstyle/plain.md)
  A text field style with no decoration.
### Supporting types
- [struct BorderedTextFieldStyle](./borderedtextfieldstyle.md)
  A text field style with a system-defined border.
- [struct DefaultTextFieldStyle](./defaulttextfieldstyle.md)
  The default text field style, based on the text field’s context.
- [struct PlainTextFieldStyle](./plaintextfieldstyle.md)
  A text field style with no decoration.
### Deprecated
- [static var roundedBorder: RoundedBorderTextFieldStyle](./textfieldstyle/roundedborder.md)
  A text field style with a system-defined rounded border.
- [static var squareBorder: SquareBorderTextFieldStyle](./textfieldstyle/squareborder.md)
  A text field style with a system-defined square border.
- [struct RoundedBorderTextFieldStyle](./roundedbordertextfieldstyle.md)
  A text field style with a system-defined rounded border.
- [struct SquareBorderTextFieldStyle](./squarebordertextfieldstyle.md)
  A text field style with a system-defined square border.

## Relationships

### Conforming Types
- [BorderedTextFieldStyle](./borderedtextfieldstyle.md)
- [DefaultTextFieldStyle](./defaulttextfieldstyle.md)
- [PlainTextFieldStyle](./plaintextfieldstyle.md)
- [RoundedBorderTextFieldStyle](./roundedbordertextfieldstyle.md)
- [SquareBorderTextFieldStyle](./squarebordertextfieldstyle.md)

## See Also

### Styling views that display text
- [func labelStyle<S>(S) -> some View](./view/labelstyle%28_%29.md)
  Sets the style for labels within this view.
- [protocol LabelStyle](./labelstyle.md)
  A type that applies a custom appearance to all labels within a view.
- [struct LabelStyleConfiguration](./labelstyleconfiguration.md)
  The properties of a label.
- [func textFieldStyle<S>(S) -> some View](./view/textfieldstyle%28_%29.md)
  Sets the style for text fields within this view.
- [func textEditorStyle(some TextEditorStyle) -> some View](./view/texteditorstyle%28_%29.md)
  Sets the style for text editors within this view.
- [protocol TextEditorStyle](./texteditorstyle.md)
  A specification for the appearance and interaction of a text editor.
- [struct TextEditorStyleConfiguration](./texteditorstyleconfiguration.md)
  The properties of a text editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfieldstyle)*