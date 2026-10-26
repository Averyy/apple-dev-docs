# NSModalPanelRunLoopMode

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The mode set when waiting for input from a modal panel, such as a save or open panel.

**Availability**:
- macOS

## Declaration

```c
extern NSRunLoopMode NSModalPanelRunLoopMode;
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmodalpanelrunloopmode)*