# borderedButton

**Framework**: SwiftUI  
**Kind**: property

A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@MainActor
@export(implementation) @preconcurrency static var borderedButton: BorderedButtonMenuStyle { get }
```

#### Discussion

On macOS, the button displays an arrow indicating that it presents a menu.

Pressing and then dragging into the contents triggers the chosen action on release.

## See Also

- [static var borderlessButton: BorderlessButtonMenuStyle](menustyle/borderlessbutton.md)
  A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed.
- [struct BorderlessButtonMenuStyle](borderlessbuttonmenustyle.md)
  A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed.
- [struct BorderedButtonMenuStyle](borderedbuttonmenustyle.md)
  A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menustyle/borderedbutton)*