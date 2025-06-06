# Modal Windows and Panels

**Framework**: AppKit

Display a modal window or show one of the standard app panels, such as the app’s About panel.

## Topics

### Running a Modal Window
- [func runModal(for: NSWindow) -> NSApplication.ModalResponse](nsapplication/runmodal(for:).md)
  Starts a modal event loop for the specified window.
- [func stopModal()](nsapplication/stopmodal.md)
  Stops a modal event loop.
- [func stopModal(withCode: NSApplication.ModalResponse)](nsapplication/stopmodal(withcode:).md)
  Stops a modal event loop, allowing you to return a custom result code.
- [func abortModal()](nsapplication/abortmodal.md)
  Aborts the event loop started by [`runModal(for:)`](nsapplication/runmodal(for:).md) or [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md).
- [func beginModalSession(for: NSWindow) -> NSApplication.ModalSession](nsapplication/beginmodalsession(for:).md)
  Sets up a modal session with the given window and returns a pointer to the `NSModalSession` structure representing the session.
- [func runModalSession(NSApplication.ModalSession) -> NSApplication.ModalResponse](nsapplication/runmodalsession(_:).md)
  Runs a given modal session, as defined in a previous invocation of [`beginModalSession(for:)`](nsapplication/beginmodalsession(for:).md).
- [var modalWindow: NSWindow?](nsapplication/modalwindow.md)
  The modal window displayed by the app.
- [NSApplication.ModalResponse](nsapplication/modalresponse.md)
  A set of button return values for modal dialogs.
- [NSApplication.ModalSession](nsapplication/modalsession.md)
  Variables of type `NSModalSession` point to information used by the system between `NSApplication`’s [`beginModalSession(for:)`](nsapplication/beginmodalsession(for:).md) and [`endModalSession(_:)`](nsapplication/endmodalsession(_:).md) messages.
### Managing Panels
- [func orderFrontColorPanel(Any?)](nsapplication/orderfrontcolorpanel(_:).md)
  Brings up the color panel, an instance of `NSColorPanel`.
- [func orderFrontStandardAboutPanel(Any?)](nsapplication/orderfrontstandardaboutpanel(_:).md)
  Displays a standard About window.
- [func orderFrontStandardAboutPanel(options: [NSApplication.AboutPanelOptionKey : Any])](nsapplication/orderfrontstandardaboutpanel(options:).md)
  Displays a standard About window with information from a given options dictionary.
- [func orderFrontCharacterPalette(Any?)](nsapplication/orderfrontcharacterpalette(_:).md)
  Opens the character palette.
- [func runPageLayout(Any?)](nsapplication/runpagelayout(_:).md)
  Displays the receiver’s page layout panel, an instance of `NSPageLayout`.
- [NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey.md)
  Keys to include in the options dictionary when displaying an About panel.

## See Also

- [App Windows](app-windows.md)
  Show, hide, minimize, arrange, and update your app’s windows.
- [Menus](menus.md)
  Access the app’s main menu items and update the window and services menus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/modal-windows-and-panels)*