# isHeld

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the button menu is visible.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var isHeld: Bool { get }
```

```objc
@property (nonatomic, assign, readonly, getter=isHeld) BOOL held;
```

## Discussion

The property is [`true`](../../Swift/true.md) if the button is presenting a menu in response to a long press. Buttons that set [`showsMenuAsPrimaryAction`](../uicontrol/showsmenuasprimaryaction.md) to present a menu don’t set this property.

## See Also

### Supporting menu and toggle buttons
- [var menu: UIMenu?](./menu.md)
  A menu that the button displays.
- [var changesSelectionAsPrimaryAction: Bool](./changesselectionasprimaryaction.md)
  A Boolean value that indicates whether the button tracks a selection, either through a menu or a toggle.
- [var preferredMenuElementOrder: UIContextMenuConfiguration.ElementOrder](./preferredmenuelementorder.md)
  The preferred menu-element ordering strategy for the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/isheld)*