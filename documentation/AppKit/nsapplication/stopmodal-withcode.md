# stopModal(withCode:)

**Framework**: AppKit  
**Kind**: method

Stops a modal event loop, allowing you to return a custom result code.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func stopModal(withCode returnCode: NSApplication.ModalResponse)
```

#### Discussion

This method should always be paired with a previous invocation of [`runModal(for:)`](nsapplication/runmodal(for:).md) or [`beginModalSession(for:)`](nsapplication/beginmodalsession(for:).md). When [`runModal(for:)`](nsapplication/runmodal(for:).md) is stopped with this method, it returns the given `returnCode`. In macOS 10.9 and later, you can use this method to stop a [`runModal(for:)`](nsapplication/runmodal(for:).md) loop outside of an event callback, such as from within a method repeatedly invoked by an [`Timer`](https://developer.apple.com/documentation/Foundation/Timer) object or a method running in a different thread.

## Parameters

- `returnCode`: The result code you want returned from the   or   method. The meaning of this result code is up to you.

## See Also

- [func runModal(for: NSWindow) -> NSApplication.ModalResponse](nsapplication/runmodal(for:).md)
  Starts a modal event loop for the specified window.
- [func stopModal()](nsapplication/stopmodal.md)
  Stops a modal event loop.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/stopmodal(withcode:))*