# borderedButton

**Framework**: SwiftUI  
**Kind**: property

A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency static var borderedButton: BorderedButtonMenuStyle { get }
```

#### Discussion

On macOS, the button displays an arrow indicating that it presents a menu.

Pressing and then dragging into the contents triggers the chosen action on release.

## See Also

- [static var automatic: DefaultMenuStyle](menustyle/automatic.md)
  The default menu style, based on the menu’s context.
- [static var button: ButtonMenuStyle](menustyle/button.md)
  A menu style that displays a button that toggles the display of the menu’s contents when pressed.
- [static var borderlessButton: BorderlessButtonMenuStyle](menustyle/borderlessbutton.md)
  A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menustyle/borderedbutton)*