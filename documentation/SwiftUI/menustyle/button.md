# button

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

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
@export(implementation)
nonisolated static var button: ButtonMenuStyle { get }
```

Available when `Self` is `ButtonMenuStyle`.

#### Discussion

On macOS, the button displays an arrow to indicate that it presents a menu.

Pressing and then dragging into the contents activates the selected action on release.

## See Also

### Getting built-in menu styles
- [static var automatic: DefaultMenuStyle](./automatic.md)
  The default menu style, based on the menu’s context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menustyle/button)*