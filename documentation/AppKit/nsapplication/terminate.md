# terminate(_:)

**Framework**: AppKit  
**Kind**: method

Terminates the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func terminate(_ sender: Any?)
```

#### Discussion

This method is typically invoked when the user chooses Quit or Exit from the app’s menu.

When invoked, this method performs several steps to process the termination request. First, it asks the app’s document controller (if one exists) to save any unsaved changes in its documents. During this process, the document controller can cancel termination in response to input from the user. If the document controller doesn’t cancel the operation, this method then calls the delegate’s [`applicationShouldTerminate(_:)`](nsapplicationdelegate/applicationshouldterminate(_:).md) method. If [`applicationShouldTerminate(_:)`](nsapplicationdelegate/applicationshouldterminate(_:).md) returns [`NSApplication.TerminateReply.terminateCancel`](nsapplication/terminatereply/terminatecancel.md), the termination process is aborted and control is handed back to the main event loop. If the method returns [`NSApplication.TerminateReply.terminateLater`](nsapplication/terminatereply/terminatelater.md), the app runs its run loop in the [`NSModalPanelRunLoopMode`](nsmodalpanelrunloopmode.md) mode until the [`reply(toApplicationShouldTerminate:)`](nsapplication/reply(toapplicationshouldterminate:).md) method is called with the value [`true`](https://developer.apple.com/documentation/swift/true) or [`false`](https://developer.apple.com/documentation/swift/false). If the [`applicationShouldTerminate(_:)`](nsapplicationdelegate/applicationshouldterminate(_:).md) method returns [`NSApplication.TerminateReply.terminateNow`](nsapplication/terminatereply/terminatenow.md), this method posts a [`willTerminateNotification`](nsapplication/willterminatenotification.md) notification to the default notification center.

Don’t bother to put final cleanup code in your app’s `main()` function—it will never be executed. If cleanup is necessary, perform that cleanup in the delegate’s [`applicationWillTerminate(_:)`](nsapplicationdelegate/applicationwillterminate(_:).md) method.

## Parameters

- `sender`: Typically, this parameter contains the object that initiated the termination request.

## See Also

- [func stop(Any?)](nsapplication/stop(_:).md)
  Stops the main event loop.
- [func applicationShouldTerminate(NSApplication) -> NSApplication.TerminateReply](nsapplicationdelegate/applicationshouldterminate(_:).md)
  Returns a value that indicates if the app should terminate.
- [func run()](nsapplication/run.md)
  Starts the main event loop.
- [func applicationWillTerminate(Notification)](nsapplicationdelegate/applicationwillterminate(_:).md)
  Tells the delegate that the app is about to terminate.
- [class let willTerminateNotification: NSNotification.Name](nsapplication/willterminatenotification.md)
  Sends a notification to termintate the app.
- [func reply(toApplicationShouldTerminate: Bool)](nsapplication/reply(toapplicationshouldterminate:).md)
  Responds to `NSTerminateLater` once the app knows whether it can terminate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/terminate(_:))*