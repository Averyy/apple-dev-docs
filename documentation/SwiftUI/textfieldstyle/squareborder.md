# squareBorder

**Framework**: SwiftUI  
**Kind**: property

A text field style with a system-defined square border.

**Availability**:
- macOS 10.15+

## Declaration

```swift
static var squareBorder: SquareBorderTextFieldStyle { get }
```

#### Discussion

As of macOS 26, text fields no longer have a rectangular border.

## See Also

- [static var automatic: DefaultTextFieldStyle](textfieldstyle/automatic.md)
  The default text field style, based on the text field’s context.
- [static var bordered: BorderedTextFieldStyle](textfieldstyle/bordered.md)
  A text field style with a system-defined border whose shape is determined by the [`textInputBorderShape(_:)`](view/textinputbordershape(_:).md) modifier.
- [static var plain: PlainTextFieldStyle](textfieldstyle/plain.md)
  A text field style with no decoration.
- [static var roundedBorder: RoundedBorderTextFieldStyle](textfieldstyle/roundedborder.md)
  A text field style with a system-defined rounded border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfieldstyle/squareborder)*