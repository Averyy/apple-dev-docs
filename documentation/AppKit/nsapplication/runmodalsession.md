# runModalSession(_:)

**Framework**: AppKit  
**Kind**: method

Runs a given modal session, as defined in a previous invocation of [`beginModalSession(for:)`](nsapplication/beginmodalsession(for:).md).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func runModalSession(_ session: NSApplication.ModalSession) -> NSApplication.ModalResponse
```

#### Return Value

An integer indicating the reason that this method returned. See the discussion for a description of possible return values.

#### Discussion

A loop that uses this method is similar in some ways to a modal event loop run with [`runModal(for:)`](nsapplication/runmodal(for:).md), except with this method your code can do some additional work between method invocations. When you invoke this method, events for the `NSWindow` object of this session are dispatched as normal. This method returns when there are no more events. You must invoke this method frequently enough in your loop that the window remains responsive to events. However, you should not invoke this method in a tight loop because it returns immediately if there are no events, and consequently you could end up polling for events rather than blocking.

Typically, you use this method in situations where you want to do some additional processing on the current thread while the modal loop runs. For example, while processing a large data set, you might want to use a modal dialog to display progress and give the user a chance to cancel the operation. If you want to display a modal dialog and do not need to do any additional work in parallel, use [`runModal(for:)`](nsapplication/runmodal(for:).md) instead. When there are no pending events, that method waits idly instead of consuming CPU time.

The following code shows a sample loop you can use in your code:

```objc
NSModalSession session = [NSApp beginModalSessionForWindow:theWindow];
for (;;) {
    if ([NSApp runModalSession:session] != NSModalResponseContinue)
        break;
    [self doSomeWork];
}
[NSApp endModalSession:session];
```

If the modal session was not stopped, this method returns `NSModalResponseContinue`. At this point, your app can do some work before the next invocation of [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md) (as indicated in the example’s `doSomeWork` call). If [`stopModal()`](nsapplication/stopmodal().md) was invoked as the result of event processing, [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md) returns `NSModalResponseStop`. If [`stopModal(withCode:)`](nsapplication/stopmodal(withcode:).md) was invoked, this method returns the value passed to [`stopModal(withCode:)`](nsapplication/stopmodal(withcode:).md). If [`abortModal()`](nsapplication/abortmodal().md) was invoked, this method returns `NSModalResponseAbort`.

The window is placed on the screen and made key as a result of the [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md) message. Do not send a separate [`makeKeyAndOrderFront(_:)`](nswindow/makekeyandorderfront(_:).md) message.

## Parameters

- `session`: A pointer to the modal session structure returned by the   method for the window to be displayed.

## See Also

- [func endModalSession(NSApplication.ModalSession)](nsapplication/endmodalsession(_:).md)
  Finishes a modal session.
- [func run()](nsapplication/run.md)
  Starts the main event loop.
- [func runModal(for: NSWindow) -> NSApplication.ModalResponse](nsapplication/runmodal(for:).md)
  Starts a modal event loop for the specified window.
- [func stopModal()](nsapplication/stopmodal.md)
  Stops a modal event loop.
- [func stopModal(withCode: NSApplication.ModalResponse)](nsapplication/stopmodal(withcode:).md)
  Stops a modal event loop, allowing you to return a custom result code.
- [func abortModal()](nsapplication/abortmodal.md)
  Aborts the event loop started by [`runModal(for:)`](nsapplication/runmodal(for:).md) or [`runModalSession(_:)`](nsapplication/runmodalsession(_:).md).
- [func beginModalSession(for: NSWindow) -> NSApplication.ModalSession](nsapplication/beginmodalsession(for:).md)
  Sets up a modal session with the given window and returns a pointer to the `NSModalSession` structure representing the session.
- [var modalWindow: NSWindow?](nsapplication/modalwindow.md)
  The modal window displayed by the app.
- [NSApplication.ModalResponse](nsapplication/modalresponse.md)
  A set of button return values for modal dialogs.
- [NSApplication.ModalSession](nsapplication/modalsession.md)
  Variables of type `NSModalSession` point to information used by the system between `NSApplication`’s [`beginModalSession(for:)`](nsapplication/beginmodalsession(for:).md) and [`endModalSession(_:)`](nsapplication/endmodalsession(_:).md) messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/runmodalsession(_:))*