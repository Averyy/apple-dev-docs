# squareBorder

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A text field style with a system-defined square border.

**Availability**:
- macOS 10.15+ - Deprecated in 27.2

> **Deprecated**: Use `textFieldStyle(.bordered)` instead. As of macOS 26, text fields no longer have a rectangular border.

## Declaration

```swift
@export(implementation)
static var squareBorder: SquareBorderTextFieldStyle { get }
```

Available when `Self` is `SquareBorderTextFieldStyle`.

## Discussion

As of macOS 26, text fields no longer have a rectangular border.

## See Also

### Deprecated
- [static var roundedBorder: RoundedBorderTextFieldStyle](./roundedborder.md)
  A text field style with a system-defined rounded border.
- [struct RoundedBorderTextFieldStyle](../roundedbordertextfieldstyle.md)
  A text field style with a system-defined rounded border.
- [struct SquareBorderTextFieldStyle](../squarebordertextfieldstyle.md)
  A text field style with a system-defined square border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfieldstyle/squareborder)*