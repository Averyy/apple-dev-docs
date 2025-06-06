# Menus, Cursors, and the Dock

**Framework**: AppKit

Implement menus and cursors to facilitate interactions with your app, and use your app’s Dock tile to convey updated information.

## Topics

### Menus
- [class NSMenu](nsmenu.md)
  An object that manages an app’s menus.
- [class NSMenuItem](nsmenuitem.md)
  A command item in an app menu.
- [class NSMenuItemBadge](nsmenuitembadge.md)
  A control that provides additional quantitative information specific to a menu item, such as the number of available updates.
- [protocol NSMenuDelegate](nsmenudelegate.md)
  The optional methods implemented by delegates of [`NSMenu`](nsmenu.md) objects to manage menu display and handle some events.
### Menu Validation
- [protocol NSMenuItemValidation](nsmenuitemvalidation.md)
### Menu Bar Items
- [class NSStatusBar](nsstatusbar.md)
  An object that manages a collection of status items displayed within the system-wide menu bar.
- [class NSStatusItem](nsstatusitem.md)
  An individual element displayed in the system menu bar.
- [class NSStatusBarButton](nsstatusbarbutton.md)
  The appearance and behavior of an item in the systemwide menu bar.
### Cursors
- [class NSCursor](nscursor.md)
  A pointer (also called a cursor).
- [class NSTrackingArea](nstrackingarea.md)
  A region of a view that generates mouse-tracking and cursor-update events when the pointer is over that region.
### The Dock
- [class NSDockTile](nsdocktile.md)
  The visual representation of your app’s miniaturized windows and app icon as they appear in the Dock.
- [protocol NSDockTilePlugIn](nsdocktileplugin.md)
  A set of methods implemented by plug-ins that allow an app’s Dock tile to be customized while the app is not running.

## See Also

- [Mouse, Keyboard, and Trackpad](mouse-keyboard-and-trackpad.md)
  Handle events related to mouse, keyboard, and trackpad input.
- [Gestures](gestures.md)
  Encapsulate your app’s event-handling logic in gesture recognizers so that you can reuse that code throughout your app.
- [Touch Bar](touch-bar.md)
  Display interactive content and controls in the Touch Bar.
- [Drag and Drop](drag-and-drop.md)
  Support the direct manipulation of your app’s content using drag and drop.
- [Accessibility for AppKit](accessibility-for-appkit.md)
  Make your AppKit apps accessible to everyone who uses macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/menus-cursors-and-the-dock)*