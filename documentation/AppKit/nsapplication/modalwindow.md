# modalWindow

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The modal window displayed by the app.

**Availability**:
- macOS

## Declaration

```swift
var modalWindow: NSWindow? { get }
```

```objc
@property (strong, readonly, nullable) NSWindow * modalWindow;
```

#### Discussion

This property contains the current standalone modal window or `nil` if no modal window is being displayed. This property does not contain sheets that are attached to other windows. To retrieve a sheet, use the [`attachedSheet`](../nswindow/attachedsheet.md) method of [`NSWindow`](../nswindow.md).

## See Also

### Running a Modal Window
- [func runModal(for: NSWindow) -> NSApplication.ModalResponse](./runmodal%28for%29.md)
  Starts a modal event loop for the specified window.
- [func stopModal()](./stopmodal%28%29.md)
  Stops a modal event loop.
- [func stopModal(withCode: NSApplication.ModalResponse)](./stopmodal%28withcode%29.md)
  Stops a modal event loop, allowing you to return a custom result code.
- [func abortModal()](./abortmodal%28%29.md)
  Aborts the event loop started by [`runModal(for:)`](./runmodal%28for%29.md) or [`runModalSession(_:)`](./runmodalsession%28_%29.md).
- [func beginModalSession(for: NSWindow) -> NSApplication.ModalSession](./beginmodalsession%28for%29.md)
  Sets up a modal session with the given window and returns a pointer to the `NSModalSession` structure representing the session.
- [func runModalSession(NSApplication.ModalSession) -> NSApplication.ModalResponse](./runmodalsession%28_%29.md)
  Runs a given modal session, as defined in a previous invocation of [`beginModalSession(for:)`](./beginmodalsession%28for%29.md).
- [NSApplication.ModalResponse](./modalresponse.md)
  A set of button return values for modal dialogs.
- [NSApplication.ModalSession](./modalsession.md)
  Variables of type `NSModalSession` point to information used by the system between `NSApplication`’s [`beginModalSession(for:)`](./beginmodalsession%28for%29.md) and [`endModalSession(_:)`](./endmodalsession%28_%29.md) messages.
- [NSModalPanelRunLoopMode](../nsmodalpanelrunloopmode.md)
  The mode set when waiting for input from a modal panel, such as a save or open panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/modalwindow)*