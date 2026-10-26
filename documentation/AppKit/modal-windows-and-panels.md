# Modal Windows and Panels

**Framework**: AppKit  
**Role**: API Collection

Display a modal window or show one of the standard app panels, such as the app’s About panel.

## Topics

### Running a Modal Window
- [func runModal(for: NSWindow) -> NSApplication.ModalResponse](./nsapplication/runmodal%28for%29.md)
  Starts a modal event loop for the specified window.
- [func stopModal()](./nsapplication/stopmodal%28%29.md)
  Stops a modal event loop.
- [func stopModal(withCode: NSApplication.ModalResponse)](./nsapplication/stopmodal%28withcode%29.md)
  Stops a modal event loop, allowing you to return a custom result code.
- [func abortModal()](./nsapplication/abortmodal%28%29.md)
  Aborts the event loop started by [`runModal(for:)`](./nsapplication/runmodal%28for%29.md) or [`runModalSession(_:)`](./nsapplication/runmodalsession%28_%29.md).
- [func beginModalSession(for: NSWindow) -> NSApplication.ModalSession](./nsapplication/beginmodalsession%28for%29.md)
  Sets up a modal session with the given window and returns a pointer to the `NSModalSession` structure representing the session.
- [func runModalSession(NSApplication.ModalSession) -> NSApplication.ModalResponse](./nsapplication/runmodalsession%28_%29.md)
  Runs a given modal session, as defined in a previous invocation of [`beginModalSession(for:)`](./nsapplication/beginmodalsession%28for%29.md).
- [var modalWindow: NSWindow?](./nsapplication/modalwindow.md)
  The modal window displayed by the app.
- [NSApplication.ModalResponse](./nsapplication/modalresponse.md)
  A set of button return values for modal dialogs.
- [NSApplication.ModalSession](./nsapplication/modalsession.md)
  Variables of type `NSModalSession` point to information used by the system between `NSApplication`’s [`beginModalSession(for:)`](./nsapplication/beginmodalsession%28for%29.md) and [`endModalSession(_:)`](./nsapplication/endmodalsession%28_%29.md) messages.
- [NSModalPanelRunLoopMode](./nsmodalpanelrunloopmode.md)
  The mode set when waiting for input from a modal panel, such as a save or open panel.
### Managing Panels
- [func orderFrontColorPanel(Any?)](./nsapplication/orderfrontcolorpanel%28_%29.md)
  Brings up the color panel, an instance of `NSColorPanel`.
- [func orderFrontStandardAboutPanel(Any?)](./nsapplication/orderfrontstandardaboutpanel%28_%29.md)
  Displays a standard About window.
- [func orderFrontStandardAboutPanel(options: [NSApplication.AboutPanelOptionKey : Any])](./nsapplication/orderfrontstandardaboutpanel%28options%29.md)
  Displays a standard About window with information from a given options dictionary.
- [func orderFrontCharacterPalette(Any?)](./nsapplication/orderfrontcharacterpalette%28_%29.md)
  Opens the character palette.
- [func runPageLayout(Any?)](./nsapplication/runpagelayout%28_%29.md)
  Displays the receiver’s page layout panel, an instance of `NSPageLayout`.
- [NSApplication.AboutPanelOptionKey](./nsapplication/aboutpaneloptionkey.md)
  Keys to include in the options dictionary when displaying an About panel.

## See Also

### Managing windows, panels, and menus
- [App Windows](./app-windows.md)
  Show, hide, minimize, arrange, and update your app’s windows.
- [Menus](./menus.md)
  Access the app’s main menu items and update the window and services menus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/modal-windows-and-panels)*