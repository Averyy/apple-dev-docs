# runModalSession(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Runs a given modal session, as defined in a previous invocation of [`beginModalSession(for:)`](./beginmodalsession%28for%29.md).

**Availability**:
- macOS

## Declaration

```swift
func runModalSession(_ session: NSApplication.ModalSession) -> NSApplication.ModalResponse
```

```objc
- (NSModalResponse) runModalSession:(NSModalSession) session;
```

#### Return Value

An integer indicating the reason that this method returned. See the discussion for a description of possible return values.

#### Discussion

A loop that uses this method is similar in some ways to a modal event loop run with [`runModal(for:)`](./runmodal%28for%29.md), except with this method your code can do some additional work between method invocations. When you invoke this method, events for the `NSWindow` object of this session are dispatched as normal. This method returns when there are no more events. You must invoke this method frequently enough in your loop that the window remains responsive to events. However, you should not invoke this method in a tight loop because it returns immediately if there are no events, and consequently you could end up polling for events rather than blocking.

Typically, you use this method in situations where you want to do some additional processing on the current thread while the modal loop runs. For example, while processing a large data set, you might want to use a modal dialog to display progress and give the user a chance to cancel the operation. If you want to display a modal dialog and do not need to do any additional work in parallel, use [`runModal(for:)`](./runmodal%28for%29.md) instead. When there are no pending events, that method waits idly instead of consuming CPU time.

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

If the modal session was not stopped, this method returns `NSModalResponseContinue`. At this point, your app can do some work before the next invocation of [`runModalSession(_:)`](./runmodalsession%28_%29.md) (as indicated in the example’s `doSomeWork` call). If [`stopModal()`](./stopmodal%28%29.md) was invoked as the result of event processing, [`runModalSession(_:)`](./runmodalsession%28_%29.md) returns `NSModalResponseStop`. If [`stopModal(withCode:)`](./stopmodal%28withcode%29.md) was invoked, this method returns the value passed to [`stopModal(withCode:)`](./stopmodal%28withcode%29.md). If [`abortModal()`](./abortmodal%28%29.md) was invoked, this method returns `NSModalResponseAbort`.

The window is placed on the screen and made key as a result of the [`runModalSession(_:)`](./runmodalsession%28_%29.md) message. Do not send a separate [`makeKeyAndOrderFront(_:)`](../nswindow/makekeyandorderfront%28_%29.md) message.

## Parameters

- `session`: A pointer to the modal session structure returned by the [`beginModalSession(for:)`](./beginmodalsession%28for%29.md) method for the window to be displayed.

## See Also

### Related Documentation
- [func endModalSession(NSApplication.ModalSession)](./endmodalsession%28_%29.md)
  Finishes a modal session.
- [func run()](./run%28%29.md)
  Starts the main event loop.
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
- [var modalWindow: NSWindow?](./modalwindow.md)
  The modal window displayed by the app.
- [NSApplication.ModalResponse](./modalresponse.md)
  A set of button return values for modal dialogs.
- [NSApplication.ModalSession](./modalsession.md)
  Variables of type `NSModalSession` point to information used by the system between `NSApplication`’s [`beginModalSession(for:)`](./beginmodalsession%28for%29.md) and [`endModalSession(_:)`](./endmodalsession%28_%29.md) messages.
- [NSModalPanelRunLoopMode](../nsmodalpanelrunloopmode.md)
  The mode set when waiting for input from a modal panel, such as a save or open panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/runmodalsession(_:))*