# borderlessButton

**Framework**: SwiftUI  
**Kind**: property

A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static var borderlessButton: BorderlessButtonMenuStyle { get }
```

#### Discussion

On macOS, the button optionally displays an arrow indicating that it presents a menu.

Pressing and then dragging into the contents triggers the chosen action on release.

## See Also

- [static var automatic: DefaultMenuStyle](menustyle/automatic.md)
  The default menu style, based on the menu’s context.
- [static var button: ButtonMenuStyle](menustyle/button.md)
  A menu style that displays a button that toggles the display of the menu’s contents when pressed.
- [static var borderedButton: BorderedButtonMenuStyle](menustyle/borderedbutton.md)
  A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menustyle/borderlessbutton)*