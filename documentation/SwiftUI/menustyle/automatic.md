# automatic

**Framework**: SwiftUI  
**Kind**: property

The default menu style, based on the menu’s context.

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
@preconcurrency static var automatic: DefaultMenuStyle { get }
```

#### Discussion

The default menu style can vary by platform. By default, macOS uses the bordered button style.

If you create a menu inside a container, the style resolves to the recommended style for menus inside that container for that specific platform. For example, a menu nested within another menu will resolve to a submenu:

```swift
Menu("Edit") {
    Menu("Arrange") {
        Button("Bring to Front", action: moveSelectionToFront)
        Button("Send to Back", action: moveSelectionToBack)
    }
    Button("Delete", action: deleteSelection)
}
```

You can override a menu’s style. To apply the default style to a menu, or to a view that contains a menu, use the [`menuStyle(_:)`](view/menustyle(_:).md) modifier.

## See Also

- [static var button: ButtonMenuStyle](menustyle/button.md)
  A menu style that displays a button that toggles the display of the menu’s contents when pressed.
- [static var borderedButton: BorderedButtonMenuStyle](menustyle/borderedbutton.md)
  A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed.
- [static var borderlessButton: BorderlessButtonMenuStyle](menustyle/borderlessbutton.md)
  A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menustyle/automatic)*