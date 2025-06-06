# TextEditorStyle

**Framework**: SwiftUI  
**Kind**: protocol

A specification for the appearance and interaction of a text editor.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol TextEditorStyle
```

#### Overview

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Topics

### Getting built-in styles
- [static var automatic: AutomaticTextEditorStyle](texteditorstyle/automatic.md)
  The default text editor style, based on the text editor’s context.
- [static var plain: PlainTextEditorStyle](texteditorstyle/plain.md)
  A text editor style with no decoration.
- [static var roundedBorder: RoundedBorderTextEditorStyle](texteditorstyle/roundedborder.md)
  A text editor style with a system-defined rounded border.
### Creating custom styles
- [func makeBody(configuration: Self.Configuration) -> Self.Body](texteditorstyle/makebody(configuration:).md)
  Creates a view that represents the body of a text editor.
- [TextEditorStyle.Configuration](texteditorstyle/configuration.md)
  The properties of a text editor.
- [associatedtype Body : View](texteditorstyle/body.md)
  A view that represents the body of a text editor.
### Supporting types
- [struct AutomaticTextEditorStyle](automatictexteditorstyle.md)
  The default text editor style, based on the text editor’s context.
- [struct PlainTextEditorStyle](plaintexteditorstyle.md)
  A text editor style with no decoration.
- [struct RoundedBorderTextEditorStyle](roundedbordertexteditorstyle.md)
  A text editor style with a system-defined rounded border.

## Relationships

### Conforming Types
- [AutomaticTextEditorStyle](automatictexteditorstyle.md)
- [PlainTextEditorStyle](plaintexteditorstyle.md)
- [RoundedBorderTextEditorStyle](roundedbordertexteditorstyle.md)

## See Also

- [func labelStyle<S>(S) -> some View](view/labelstyle(_:).md)
  Sets the style for labels within this view.
- [protocol LabelStyle](labelstyle.md)
  A type that applies a custom appearance to all labels within a view.
- [struct LabelStyleConfiguration](labelstyleconfiguration.md)
  The properties of a label.
- [func textFieldStyle<S>(S) -> some View](view/textfieldstyle(_:).md)
  Sets the style for text fields within this view.
- [protocol TextFieldStyle](textfieldstyle.md)
  A specification for the appearance and interaction of a text field.
- [func textEditorStyle(some TextEditorStyle) -> some View](view/texteditorstyle(_:).md)
  Sets the style for text editors within this view.
- [struct TextEditorStyleConfiguration](texteditorstyleconfiguration.md)
  The properties of a text editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/texteditorstyle)*