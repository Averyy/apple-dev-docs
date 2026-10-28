# terminate(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Terminates the receiver.

**Availability**:
- macOS

## Declaration

```swift
func terminate(_ sender: Any?)
```

```objc
- (void) terminate:(id) sender;
```

## Discussion

This method is typically invoked when the user chooses Quit or Exit from the app’s menu.

When invoked, this method performs several steps to process the termination request. First, it asks the app’s document controller (if one exists) to save any unsaved changes in its documents. During this process, the document controller can cancel termination in response to input from the user. If the document controller doesn’t cancel the operation, this method then calls the delegate’s [`applicationShouldTerminate(_:)`](../nsapplicationdelegate/applicationshouldterminate%28_%29.md) method. If [`applicationShouldTerminate(_:)`](../nsapplicationdelegate/applicationshouldterminate%28_%29.md) returns [`NSApplication.TerminateReply.terminateCancel`](./terminatereply/terminatecancel.md), the termination process is aborted and control is handed back to the main event loop. If the method returns [`NSApplication.TerminateReply.terminateLater`](./terminatereply/terminatelater.md), the app runs its run loop in the [`NSModalPanelRunLoopMode`](../nsmodalpanelrunloopmode.md) mode until the [`reply(toApplicationShouldTerminate:)`](./reply%28toapplicationshouldterminate%29.md) method is called with the value [`true`](../../Swift/true.md) or [`false`](../../Swift/false.md). If the [`applicationShouldTerminate(_:)`](../nsapplicationdelegate/applicationshouldterminate%28_%29.md) method returns [`NSApplication.TerminateReply.terminateNow`](./terminatereply/terminatenow.md), this method posts a [`willTerminateNotification`](./willterminatenotification.md) notification to the default notification center.

Don’t bother to put final cleanup code in your app’s `main()` function—it will never be executed. If cleanup is necessary, perform that cleanup in the delegate’s [`applicationWillTerminate(_:)`](../nsapplicationdelegate/applicationwillterminate%28_%29.md) method.

## Parameters

- `sender`: Typically, this parameter contains the object that initiated the termination request.

## See Also

### Related Documentation
- [func stop(Any?)](./stop%28_%29.md)
  Stops the main event loop.
- [func applicationShouldTerminate(NSApplication) -> NSApplication.TerminateReply](../nsapplicationdelegate/applicationshouldterminate%28_%29.md)
  Returns a value that indicates if the app should terminate.
- [func run()](./run%28%29.md)
  Starts the main event loop.
- [func applicationWillTerminate(Notification)](../nsapplicationdelegate/applicationwillterminate%28_%29.md)
  Tells the delegate that the app is about to terminate.
- [class let willTerminateNotification: NSNotification.Name](./willterminatenotification.md)
  Sends a notification to terminate the app.
### Terminating the app
- [func reply(toApplicationShouldTerminate: Bool)](./reply%28toapplicationshouldterminate%29.md)
  Responds to `NSTerminateLater` once the app knows whether it can terminate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/terminate(_:))*