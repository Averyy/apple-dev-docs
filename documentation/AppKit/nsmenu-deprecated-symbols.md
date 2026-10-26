# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

#### Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated methods
- [func helpRequested(with: NSEvent)](./nsmenu/helprequested%28with%29.md)
  Overridden by subclasses to implement specialized context-sensitive help behavior.
- [class func menuZone() -> NSZone!](./nsmenu/menuzone%28%29.md)
  Returns the zone from which `NSMenu` objects should be allocated.
- [- attachedMenu](./nsmenu/attachedmenu.md)
  Returns the menu currently attached to the menu.
- [- isAttached](./nsmenu/isattached.md)
  Returns a Boolean value that indicates whether the menu is currently attached to another menu.
- [- locationForSubmenu:](./nsmenu/locationforsubmenu_.md)
  Returns the location in screen coordinates where the given submenu is displayed when opened as a submenu of the menu.
- [- sizeToFit](./nsmenu/sizetofit.md)
  Resizes the menu to exactly fit its items.
- [+ setMenuZone:](./nsmenu/setmenuzone_.md)
  Sets the zone from which `NSMenu` objects should be allocated
- [- contextMenuRepresentation](./nsmenu/contextmenurepresentation.md)
  Deprecated.
- [- setContextMenuRepresentation:](./nsmenu/setcontextmenurepresentation_.md)
  Deprecated.
- [- tearOffMenuRepresentation](./nsmenu/tearoffmenurepresentation.md)
  Deprecated.
- [- setTearOffMenuRepresentation:](./nsmenu/settearoffmenurepresentation_.md)
  Deprecated.
- [- setMenuRepresentation:](./nsmenu/setmenurepresentation_.md)
  Deprecated.
- [- menuRepresentation](./nsmenu/menurepresentation.md)
  Deprecated.
### Deprecated properties
- [var isTornOff: Bool](./nsmenu/istornoff.md)
  Indicates whether the menu is offscreen or attached to another menu (or if it’s the main menu).
- [var menuChangedMessagesEnabled: Bool](./nsmenu/menuchangedmessagesenabled.md)
  Indicates whether messages are sent to the application’s windows each time the menu changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu-deprecated-symbols)*