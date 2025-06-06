# abortModal()

**Framework**: AppKit  
**Kind**: method

Aborts the event loop started by [`runModal(for:)`](nsapplication/runmodal(for:).md) or [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func abortModal()
```

#### Discussion

When stopped with this method, [`runModal(for:)`](nsapplication/runmodal(for:).md) and [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md) return `NSModalResponseAbort`.

[`abortModal()`](nsapplication/abortmodal().md) must be used instead of [`stopModal()`](nsapplication/stopmodal().md) or [`stopModal(withCode:)`](nsapplication/stopmodal(withcode:).md) when you need to stop a modal event loop from anywhere other than a callout from that event loop. In other words, if you want to stop the loop in response to a user’s actions within the modal window, use [`stopModal()`](nsapplication/stopmodal().md); otherwise, use [`abortModal()`](nsapplication/abortmodal().md). For example, use [`abortModal()`](nsapplication/abortmodal().md) when running in a different thread from AppKit’s main thread or when responding to an `NSTimer` that you have added to the `NSModalPanelRunLoopMode` mode of the default `NSRunLoop`.

## See Also

- [func endModalSession(NSApplication.ModalSession)](nsapplication/endmodalsession(_:).md)
  Finishes a modal session.
- [func runModal(for: NSWindow) -> NSApplication.ModalResponse](nsapplication/runmodal(for:).md)
  Starts a modal event loop for the specified window.
- [func stopModal()](nsapplication/stopmodal.md)
  Stops a modal event loop.
- [func stopModal(withCode: NSApplication.ModalResponse)](nsapplication/stopmodal(withcode:).md)
  Stops a modal event loop, allowing you to return a custom result code.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/abortmodal())*