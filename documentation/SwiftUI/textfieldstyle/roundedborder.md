# roundedBorder

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A text field style with a system-defined rounded border.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+

> **Deprecated**: Use `textFieldStyle(.bordered)` with `textInputBorderShape(.roundedRectangle)`

## Declaration

```swift
@export(implementation)
static var roundedBorder: RoundedBorderTextFieldStyle { get }
```

Available when `Self` is `RoundedBorderTextFieldStyle`.

#### Discussion

Use [`textFieldStyle(_:)`](../view/textfieldstyle%28_%29.md) to apply the [`bordered`](./bordered.md) style with [`textInputBorderShape(_:)`](../view/textinputbordershape%28_%29.md) to apply the [`roundedRectangle`](../textinputbordershape/roundedrectangle.md) shape instead.

## See Also

### Deprecated
- [static var squareBorder: SquareBorderTextFieldStyle](./squareborder.md)
  A text field style with a system-defined square border.
- [struct RoundedBorderTextFieldStyle](../roundedbordertextfieldstyle.md)
  A text field style with a system-defined rounded border.
- [struct SquareBorderTextFieldStyle](../squarebordertextfieldstyle.md)
  A text field style with a system-defined square border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfieldstyle/roundedborder)*