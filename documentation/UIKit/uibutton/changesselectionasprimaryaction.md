# changesSelectionAsPrimaryAction

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the button tracks a selection, either through a menu or a toggle.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var changesSelectionAsPrimaryAction: Bool { get set }
```

#### Discussion

This behavior of this property composes with [`showsMenuAsPrimaryAction`](uicontrol/showsmenuasprimaryaction.md) and the [`menu`](uibutton/menu.md) property.

If [`menu`](uibutton/menu.md) is `nil`, setting this property to [`true`](https://developer.apple.com/documentation/Swift/true) makes the button toggle its [`selected`](uicontrol/state-swift.struct/selected.md) state.

If you set a menu and [`showsMenuAsPrimaryAction`](uicontrol/showsmenuasprimaryaction.md) is [`false`](https://developer.apple.com/documentation/Swift/false), setting this property to [`true`](https://developer.apple.com/documentation/Swift/true) makes the button a toggle button. The menu functions as a contextual menu, which appears after a long press.

If you set a menu and [`showsMenuAsPrimaryAction`](uicontrol/showsmenuasprimaryaction.md) is [`true`](https://developer.apple.com/documentation/Swift/true), setting this property to [`true`](https://developer.apple.com/documentation/Swift/true) makes the button function as a pop-up. The button presents the menu on touch, the menu tracks the selection in its [`selectedElements`](uimenu/selectedelements.md) property, and the button title updates to reflect the selection.

## See Also

- [var menu: UIMenu?](uibutton/menu.md)
  A menu that the button displays.
- [var isHeld: Bool](uibutton/isheld.md)
  A Boolean value that indicates whether the button menu is visible.
- [var preferredMenuElementOrder: UIContextMenuConfiguration.ElementOrder](uibutton/preferredmenuelementorder.md)
  The preferred menu-element ordering strategy for the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/changesselectionasprimaryaction)*