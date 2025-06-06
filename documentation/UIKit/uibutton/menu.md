# menu

**Framework**: UIKit  
**Kind**: property

A menu that the button displays.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var menu: UIMenu? { get set }
```

#### Discussion

The default value is `nil`. When this property changes, the button automatically enables and disables the [`contextMenuInteraction`](uicontrol/contextmenuinteraction.md).

## See Also

- [var isHeld: Bool](uibutton/isheld.md)
  A Boolean value that indicates whether the button menu is visible.
- [var changesSelectionAsPrimaryAction: Bool](uibutton/changesselectionasprimaryaction.md)
  A Boolean value that indicates whether the button tracks a selection, either through a menu or a toggle.
- [var preferredMenuElementOrder: UIContextMenuConfiguration.ElementOrder](uibutton/preferredmenuelementorder.md)
  The preferred menu-element ordering strategy for the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/menu)*