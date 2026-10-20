# menu

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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
var menu: UIMenu? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) UIMenu * menu;
```

#### Discussion

The default value is `nil`. When this property changes, the button automatically enables and disables the [`contextMenuInteraction`](../uicontrol/contextmenuinteraction.md).

## See Also

### Supporting menu and toggle buttons
- [var isHeld: Bool](./isheld.md)
  A Boolean value that indicates whether the button menu is visible.
- [var changesSelectionAsPrimaryAction: Bool](./changesselectionasprimaryaction.md)
  A Boolean value that indicates whether the button tracks a selection, either through a menu or a toggle.
- [var preferredMenuElementOrder: UIContextMenuConfiguration.ElementOrder](./preferredmenuelementorder.md)
  The preferred menu-element ordering strategy for the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/menu)*