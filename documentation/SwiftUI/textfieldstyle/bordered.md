# bordered

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A text field style with a system-defined border whose shape is determined by the [`textInputBorderShape(_:)`](../view/textinputbordershape%28_%29.md) modifier.

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
@export(implementation)
static var bordered: BorderedTextFieldStyle { get }
```

Available when `Self` is `BorderedTextFieldStyle`.

## See Also

### Getting built-in text field styles
- [static var automatic: DefaultTextFieldStyle](./automatic.md)
  The default text field style, based on the text field’s context.
- [static var plain: PlainTextFieldStyle](./plain.md)
  A text field style with no decoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfieldstyle/bordered)*