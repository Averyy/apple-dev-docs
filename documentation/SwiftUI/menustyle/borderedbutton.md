# borderedButton

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed.

**Availability**:
- macOS 11.0+ - Deprecated in 27.2

> **Deprecated**: Use [`menuStyle(_:)`](../view/menustyle%28_%29.md) with [`button`](./button.md) and [`buttonStyle(_:)`](../view/buttonstyle%28_%29-66fbx.md) with [`bordered`](../primitivebuttonstyle/bordered.md).

## Declaration

```swift
@MainActor
@export(implementation) @preconcurrency static var borderedButton: BorderedButtonMenuStyle { get }
```

Available when `Self` is `BorderedButtonMenuStyle`.

## Discussion

On macOS, the button displays an arrow indicating that it presents a menu.

Pressing and then dragging into the contents triggers the chosen action on release.

## See Also

### Deprecated
- [static var borderlessButton: BorderlessButtonMenuStyle](./borderlessbutton.md)
  A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed.
- [struct BorderlessButtonMenuStyle](../borderlessbuttonmenustyle.md)
  A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed.
- [struct BorderedButtonMenuStyle](../borderedbuttonmenustyle.md)
  A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menustyle/borderedbutton)*