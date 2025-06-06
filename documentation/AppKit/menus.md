# Menus

**Framework**: AppKit

Access the app’s main menu items and update the window and services menus.

## Topics

### Accessing the Main Menu
- [var mainMenu: NSMenu?](nsapplication/mainmenu.md)
  The app’s main menu bar.
- [var isAutomaticCustomizeTouchBarMenuItemEnabled: Bool](nsapplication/isautomaticcustomizetouchbarmenuitemenabled.md)
  A Boolean value indicating whether the main menu contains an item for customizing the contents of the Touch Bar.
### Managing the Window Menu
- [var windowsMenu: NSMenu?](nsapplication/windowsmenu.md)
  The Window menu of the app.
- [func addWindowsItem(NSWindow, title: String, filename: Bool)](nsapplication/addwindowsitem(_:title:filename:).md)
  Adds an item to the Window menu for a given window.
- [func changeWindowsItem(NSWindow, title: String, filename: Bool)](nsapplication/changewindowsitem(_:title:filename:).md)
  Changes the item for a given window in the Window menu to a given string.
- [func removeWindowsItem(NSWindow)](nsapplication/removewindowsitem(_:).md)
  Removes the Window menu item for a given window.
- [func updateWindowsItem(NSWindow)](nsapplication/updatewindowsitem(_:).md)
  Updates the Window menu item for a given window to reflect the edited status of that window.
### Managing the Services Menu
- [func registerServicesMenuSendTypes([NSPasteboard.PasteboardType], returnTypes: [NSPasteboard.PasteboardType])](nsapplication/registerservicesmenusendtypes(_:returntypes:).md)
  Registers the pasteboard types the receiver can send and receive in response to service requests.
- [var servicesMenu: NSMenu?](nsapplication/servicesmenu.md)
  The app’s Services menu.

## See Also

- [App Windows](app-windows.md)
  Show, hide, minimize, arrange, and update your app’s windows.
- [Modal Windows and Panels](modal-windows-and-panels.md)
  Display a modal window or show one of the standard app panels, such as the app’s About panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/menus)*