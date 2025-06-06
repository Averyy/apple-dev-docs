# runModal(for:)

**Framework**: AppKit  
**Kind**: method

Starts a modal event loop for the specified window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func runModal(for window: NSWindow) -> NSApplication.ModalResponse
```

#### Return Value

An integer indicating the reason that this method returned. See [`NSApplication.ModalResponse`](nsapplication/modalresponse.md) possible return values.

#### Discussion

This method runs a modal event loop for the specified window synchronously. It displays the specified window, makes it key, starts the run loop, and processes events for that window. (You do not need to show the window yourself.) While the app is in that loop, it does not respond to any other events (including mouse, keyboard, or window-close events) unless they are associated with the window. It also does not perform any tasks (such as firing timers) that are not associated with the modal run loop. In other words, this method consumes only enough CPU time to process events and dispatch them to the action methods associated with the modal window.

You can exit the modal loop by calling the [`stopModal()`](nsapplication/stopmodal().md), [`stopModal(withCode:)`](nsapplication/stopmodal(withcode:).md), or [`abortModal()`](nsapplication/abortmodal().md) methods from your modal window code. If you use the [`stopModal(withCode:)`](nsapplication/stopmodal(withcode:).md) method to stop the modal event loop, this method returns the argument passed to [`stopModal(withCode:)`](nsapplication/stopmodal(withcode:).md). If you use [`stopModal()`](nsapplication/stopmodal().md) instead, this method returns the constant [`stop`](nsapplication/modalresponse/stop.md). If you use [`abortModal()`](nsapplication/abortmodal().md), this method returns the constant [`abort`](nsapplication/modalresponse/abort.md).

## Parameters

- `window`: The window to be displayed modally. If it is not already visible, the window is centered on the screen using the value in its   method and made visible and key. If it is already visible, it is simply made key.

## See Also

- [func run()](nsapplication/run.md)
  Starts the main event loop.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/runmodal(for:))*