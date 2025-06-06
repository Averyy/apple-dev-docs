# beginModalSession(for:)

**Framework**: AppKit  
**Kind**: method

Sets up a modal session with the given window and returns a pointer to the `NSModalSession` structure representing the session.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func beginModalSession(for window: NSWindow) -> NSApplication.ModalSession
```

#### Return Value

A pointer to the `NSModalSession` structure that represents the session.

#### Discussion

In a modal session, the app receives mouse events only if they occur in `aWindow`. The window is made key, and if not already visible is placed onscreen using the `NSWindow` method [`center()`](nswindow/center().md).

The [`beginModalSession(for:)`](nsapplication/beginmodalsession(for:).md) method only sets up the modal session. To actually run the session, use [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md). [`beginModalSession(for:)`](nsapplication/beginmodalsession(for:).md) should be balanced by [`endModalSession(_:)`](nsapplication/endmodalsession(_:).md). Make sure these two messages are sent within the same exception-handling scope. That is, if you send [`beginModalSession(for:)`](nsapplication/beginmodalsession(for:).md) inside an `NS_DURING` construct, you must send [`endModalSession(_:)`](nsapplication/endmodalsession(_:).md) before `NS_ENDHANDLER`.

If an exception is raised, [`beginModalSession(for:)`](nsapplication/beginmodalsession(for:).md) arranges for proper cleanup. Do not use `NS_DURING` constructs to send an [`endModalSession(_:)`](nsapplication/endmodalsession(_:).md) message in the event of an exception.

A loop using these methods is similar to a modal event loop run with [`runModal(for:)`](nsapplication/runmodal(for:).md), except the app can continue processing between method invocations.

## Parameters

- `window`: The window for the session.

## See Also

- [func runModal(for: NSWindow) -> NSApplication.ModalResponse](nsapplication/runmodal(for:).md)
  Starts a modal event loop for the specified window.
- [func stopModal()](nsapplication/stopmodal.md)
  Stops a modal event loop.
- [func stopModal(withCode: NSApplication.ModalResponse)](nsapplication/stopmodal(withcode:).md)
  Stops a modal event loop, allowing you to return a custom result code.
- [func abortModal()](nsapplication/abortmodal.md)
  Aborts the event loop started by [`runModal(for:)`](nsapplication/runmodal(for:).md) or [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md).
- [func runModalSession(NSApplication.ModalSession) -> NSApplication.ModalResponse](nsapplication/runmodalsession(_:).md)
  Runs a given modal session, as defined in a previous invocation of [`beginModalSession(for:)`](nsapplication/beginmodalsession(for:).md).
- [var modalWindow: NSWindow?](nsapplication/modalwindow.md)
  The modal window displayed by the app.
- [NSApplication.ModalResponse](nsapplication/modalresponse.md)
  A set of button return values for modal dialogs.
- [NSApplication.ModalSession](nsapplication/modalsession.md)
  Variables of type `NSModalSession` point to information used by the system between `NSApplication`’s [`beginModalSession(for:)`](nsapplication/beginmodalsession(for:).md) and [`endModalSession(_:)`](nsapplication/endmodalsession(_:).md) messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/beginmodalsession(for:))*