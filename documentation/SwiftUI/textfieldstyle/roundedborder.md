# roundedBorder

**Framework**: SwiftUI  
**Kind**: property

A text field style with a system-defined rounded border.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
static var roundedBorder: RoundedBorderTextFieldStyle { get }
```

#### Discussion

Use [`textFieldStyle(_:)`](view/textfieldstyle(_:).md) to apply the [`bordered`](textfieldstyle/bordered.md) style with [`textInputBorderShape(_:)`](view/textinputbordershape(_:).md) to apply the [`roundedRectangle`](textinputbordershape/roundedrectangle.md) shape instead.

## See Also

- [static var automatic: DefaultTextFieldStyle](textfieldstyle/automatic.md)
  The default text field style, based on the text field’s context.
- [static var bordered: BorderedTextFieldStyle](textfieldstyle/bordered.md)
  A text field style with a system-defined border whose shape is determined by the [`textInputBorderShape(_:)`](view/textinputbordershape(_:).md) modifier.
- [static var plain: PlainTextFieldStyle](textfieldstyle/plain.md)
  A text field style with no decoration.
- [static var squareBorder: SquareBorderTextFieldStyle](textfieldstyle/squareborder.md)
  A text field style with a system-defined square border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfieldstyle/roundedborder)*