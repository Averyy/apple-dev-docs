# button

**Framework**: SwiftUI  
**Kind**: property

A menu style that displays a button that toggles the display of the menu’s contents when pressed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static var button: ButtonMenuStyle { get }
```

#### Discussion

On macOS, the button displays an arrow to indicate that it presents a menu.

Pressing and then dragging into the contents activates the selected action on release.

## See Also

- [static var automatic: DefaultMenuStyle](menustyle/automatic.md)
  The default menu style, based on the menu’s context.
- [static var borderedButton: BorderedButtonMenuStyle](menustyle/borderedbutton.md)
  A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed.
- [static var borderlessButton: BorderlessButtonMenuStyle](menustyle/borderlessbutton.md)
  A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menustyle/button)*