# runModal(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Starts a modal event loop for the specified window.

**Availability**:
- macOS

## Declaration

```swift
func runModal(for window: NSWindow) -> NSApplication.ModalResponse
```

```objc
- (NSModalResponse) runModalForWindow:(NSWindow *) window;
```

#### Return Value

An integer indicating the reason that this method returned. See [`NSApplication.ModalResponse`](./modalresponse.md) possible return values.

#### Discussion

This method runs a modal event loop for the specified window synchronously. It displays the specified window, makes it key, starts the run loop, and processes events for that window. (You do not need to show the window yourself.) While the app is in that loop, it does not respond to any other events (including mouse, keyboard, or window-close events) unless they are associated with the window. It also does not perform any tasks (such as firing timers) that are not associated with the modal run loop. In other words, this method consumes only enough CPU time to process events and dispatch them to the action methods associated with the modal window.

You can exit the modal loop by calling the [`stopModal()`](./stopmodal%28%29.md), [`stopModal(withCode:)`](./stopmodal%28withcode%29.md), or [`abortModal()`](./abortmodal%28%29.md) methods from your modal window code. If you use the [`stopModal(withCode:)`](./stopmodal%28withcode%29.md) method to stop the modal event loop, this method returns the argument passed to [`stopModal(withCode:)`](./stopmodal%28withcode%29.md). If you use [`stopModal()`](./stopmodal%28%29.md) instead, this method returns the constant [`stop`](./modalresponse/stop.md). If you use [`abortModal()`](./abortmodal%28%29.md), this method returns the constant [`abort`](./modalresponse/abort.md).

## Parameters

- `window`: The window to be displayed modally. If it is not already visible, the window is centered on the screen using the value in its [`center()`](../nswindow/center%28%29.md) method and made visible and key. If it is already visible, it is simply made key.

## See Also

### Related Documentation
- [func run()](./run%28%29.md)
  Starts the main event loop.
### Running a Modal Window
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
- [var modalWindow: NSWindow?](./modalwindow.md)
  The modal window displayed by the app.
- [NSApplication.ModalResponse](./modalresponse.md)
  A set of button return values for modal dialogs.
- [NSApplication.ModalSession](./modalsession.md)
  Variables of type `NSModalSession` point to information used by the system between `NSApplication`’s [`beginModalSession(for:)`](./beginmodalsession%28for%29.md) and [`endModalSession(_:)`](./endmodalsession%28_%29.md) messages.
- [NSModalPanelRunLoopMode](../nsmodalpanelrunloopmode.md)
  The mode set when waiting for input from a modal panel, such as a save or open panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/runmodal(for:))*