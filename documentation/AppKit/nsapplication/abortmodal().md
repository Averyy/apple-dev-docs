# abortModal()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Aborts the event loop started by [`runModal(for:)`](./runmodal%28for%29.md) or [`runModalSession(_:)`](./runmodalsession%28_%29.md).

**Availability**:
- macOS

## Declaration

```swift
func abortModal()
```

```objc
- (void) abortModal;
```

## Discussion

When stopped with this method, [`runModal(for:)`](./runmodal%28for%29.md) and [`runModalSession(_:)`](./runmodalsession%28_%29.md) return `NSModalResponseAbort`.

[`abortModal()`](./abortmodal%28%29.md) must be used instead of [`stopModal()`](./stopmodal%28%29.md) or [`stopModal(withCode:)`](./stopmodal%28withcode%29.md) when you need to stop a modal event loop from anywhere other than a callout from that event loop. In other words, if you want to stop the loop in response to a user’s actions within the modal window, use [`stopModal()`](./stopmodal%28%29.md); otherwise, use [`abortModal()`](./abortmodal%28%29.md). For example, use [`abortModal()`](./abortmodal%28%29.md) when running in a different thread from AppKit’s main thread or when responding to an `NSTimer` that you have added to the `NSModalPanelRunLoopMode` mode of the default `NSRunLoop`.

## See Also

### Related Documentation
- [func endModalSession(NSApplication.ModalSession)](./endmodalsession%28_%29.md)
  Finishes a modal session.
### Running a Modal Window
- [func runModal(for: NSWindow) -> NSApplication.ModalResponse](./runmodal%28for%29.md)
  Starts a modal event loop for the specified window.
- [func stopModal()](./stopmodal%28%29.md)
  Stops a modal event loop.
- [func stopModal(withCode: NSApplication.ModalResponse)](./stopmodal%28withcode%29.md)
  Stops a modal event loop, allowing you to return a custom result code.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/abortmodal())*