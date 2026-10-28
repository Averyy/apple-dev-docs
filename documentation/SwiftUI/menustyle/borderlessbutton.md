# borderlessButton

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- tvOS 17.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`menuStyle(_:)`](../view/menustyle%28_%29.md) with [`button`](./button.md) and [`buttonStyle(_:)`](../view/buttonstyle%28_%29-66fbx.md) with [`borderless`](../primitivebuttonstyle/borderless.md).

## Declaration

```swift
@export(implementation)
nonisolated static var borderlessButton: BorderlessButtonMenuStyle { get }
```

Available when `Self` is `BorderlessButtonMenuStyle`.

## Discussion

On macOS, the button optionally displays an arrow indicating that it presents a menu.

Pressing and then dragging into the contents triggers the chosen action on release.

## See Also

### Deprecated
- [static var borderedButton: BorderedButtonMenuStyle](./borderedbutton.md)
  A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed.
- [struct BorderlessButtonMenuStyle](../borderlessbuttonmenustyle.md)
  A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed.
- [struct BorderedButtonMenuStyle](../borderedbuttonmenustyle.md)
  A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menustyle/borderlessbutton)*