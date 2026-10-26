# beginModalSession(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets up a modal session with the given window and returns a pointer to the `NSModalSession` structure representing the session.

**Availability**:
- macOS

## Declaration

```swift
func beginModalSession(for window: NSWindow) -> NSApplication.ModalSession
```

```objc
- (NSModalSession) beginModalSessionForWindow:(NSWindow *) window;
```

#### Return Value

A pointer to the `NSModalSession` structure that represents the session.

#### Discussion

In a modal session, the app receives mouse events only if they occur in `aWindow`. The window is made key, and if not already visible is placed onscreen using the `NSWindow` method [`center()`](../nswindow/center%28%29.md).

The [`beginModalSession(for:)`](./beginmodalsession%28for%29.md) method only sets up the modal session. To actually run the session, use [`runModalSession(_:)`](./runmodalsession%28_%29.md). [`beginModalSession(for:)`](./beginmodalsession%28for%29.md) should be balanced by [`endModalSession(_:)`](./endmodalsession%28_%29.md). Make sure these two messages are sent within the same exception-handling scope. That is, if you send [`beginModalSession(for:)`](./beginmodalsession%28for%29.md) inside an `NS_DURING` construct, you must send [`endModalSession(_:)`](./endmodalsession%28_%29.md) before `NS_ENDHANDLER`.

If an exception is raised, [`beginModalSession(for:)`](./beginmodalsession%28for%29.md) arranges for proper cleanup. Do not use `NS_DURING` constructs to send an [`endModalSession(_:)`](./endmodalsession%28_%29.md) message in the event of an exception.

A loop using these methods is similar to a modal event loop run with [`runModal(for:)`](./runmodal%28for%29.md), except the app can continue processing between method invocations.

## Parameters

- `window`: The window for the session.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/beginmodalsession(for:))*