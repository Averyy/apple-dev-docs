# changesSelectionAsPrimaryAction

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the button tracks a selection, either through a menu or a toggle.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var changesSelectionAsPrimaryAction: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite) BOOL changesSelectionAsPrimaryAction;
```

## Discussion

This behavior of this property composes with [`showsMenuAsPrimaryAction`](../uicontrol/showsmenuasprimaryaction.md) and the [`menu`](./menu.md) property.

If [`menu`](./menu.md) is `nil`, setting this property to [`true`](../../Swift/true.md) makes the button toggle its [`selected`](../uicontrol/state-swift.struct/selected.md) state.

If you set a menu and [`showsMenuAsPrimaryAction`](../uicontrol/showsmenuasprimaryaction.md) is [`false`](../../Swift/false.md), setting this property to [`true`](../../Swift/true.md) makes the button a toggle button. The menu functions as a contextual menu, which appears after a long press.

If you set a menu and [`showsMenuAsPrimaryAction`](../uicontrol/showsmenuasprimaryaction.md) is [`true`](../../Swift/true.md), setting this property to [`true`](../../Swift/true.md) makes the button function as a pop-up. The button presents the menu on touch, the menu tracks the selection in its [`selectedElements`](../uimenu/selectedelements.md) property, and the button title updates to reflect the selection.

## See Also

### Supporting menu and toggle buttons
- [var menu: UIMenu?](./menu.md)
  A menu that the button displays.
- [var isHeld: Bool](./isheld.md)
  A Boolean value that indicates whether the button menu is visible.
- [var preferredMenuElementOrder: UIContextMenuConfiguration.ElementOrder](./preferredmenuelementorder.md)
  The preferred menu-element ordering strategy for the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/changesselectionasprimaryaction)*