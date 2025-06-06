# NSMenuDelegate

**Framework**: AppKit  
**Kind**: protocol

The optional methods implemented by delegates of [`NSMenu`](nsmenu.md) objects to manage menu display and handle some events.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSMenuDelegate : NSObjectProtocol
```

## Topics

### Handling Keyboard Equivalents
- [func menuHasKeyEquivalent(NSMenu, for: NSEvent, target: AutoreleasingUnsafeMutablePointer<AnyObject?>, action: UnsafeMutablePointer<Selector?>) -> Bool](nsmenudelegate/menuhaskeyequivalent(_:for:target:action:).md)
  Invoked to allow the delegate to return the target and action for a key-down event.
### Updating Menu Layout
- [func menu(NSMenu, update: NSMenuItem, at: Int, shouldCancel: Bool) -> Bool](nsmenudelegate/menu(_:update:at:shouldcancel:).md)
  Invoked to let the delegate update a menu item before it is displayed.
- [func confinementRect(for: NSMenu, on: NSScreen?) -> NSRect](nsmenudelegate/confinementrect(for:on:).md)
  Invoked to allow the delegate to specify a display location for the menu.
### Handling Highlighting
- [func menu(NSMenu, willHighlight: NSMenuItem?)](nsmenudelegate/menu(_:willhighlight:).md)
  Invoked to indicate that a menu is about to highlight a given item.
### Handling Open and Close Events
- [func menuWillOpen(NSMenu)](nsmenudelegate/menuwillopen(_:).md)
  Invoked when a menu is about to open.
- [func menuDidClose(NSMenu)](nsmenudelegate/menudidclose(_:).md)
  Invoked after a menu closed.
### Handling Tracking
- [func numberOfItems(in: NSMenu) -> Int](nsmenudelegate/numberofitems(in:).md)
  Invoked when a menu is about to be displayed at the start of a tracking session so the delegate can specify the number of items in the menu.
- [func menuNeedsUpdate(NSMenu)](nsmenudelegate/menuneedsupdate(_:).md)
  Invoked when a menu is about to be displayed at the start of a tracking session.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSMenu](nsmenu.md)
  An object that manages an app’s menus.
- [class NSMenuItem](nsmenuitem.md)
  A command item in an app menu.
- [class NSMenuItemBadge](nsmenuitembadge.md)
  A control that provides additional quantitative information specific to a menu item, such as the number of available updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenudelegate)*