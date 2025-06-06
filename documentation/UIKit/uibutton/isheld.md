# isHeld

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the button menu is visible.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isHeld: Bool { get }
```

#### Discussion

The property is [`true`](https://developer.apple.com/documentation/swift/true) if the button is presenting a menu in response to a long press. Buttons that set [`showsMenuAsPrimaryAction`](uicontrol/showsmenuasprimaryaction.md) to present a menu don’t set this property.

## See Also

- [var menu: UIMenu?](uibutton/menu.md)
  A menu that the button displays.
- [var changesSelectionAsPrimaryAction: Bool](uibutton/changesselectionasprimaryaction.md)
  A Boolean value that indicates whether the button tracks a selection, either through a menu or a toggle.
- [var preferredMenuElementOrder: UIContextMenuConfiguration.ElementOrder](uibutton/preferredmenuelementorder.md)
  The preferred menu-element ordering strategy for the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/isheld)*