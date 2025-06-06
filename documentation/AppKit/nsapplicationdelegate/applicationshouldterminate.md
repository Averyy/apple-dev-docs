# applicationShouldTerminate(_:)

**Framework**: AppKit  
**Kind**: method

Returns a value that indicates if the app should terminate.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func applicationShouldTerminate(_ sender: NSApplication) -> NSApplication.TerminateReply
```

#### Return Value

One of the values defined in [`NSApplication.TerminateReply`](nsapplication/terminatereply.md) constants indicating whether the application should terminate. For compatibility reasons, a return value of [`false`](https://developer.apple.com/documentation/swift/false) is equivalent to [`NSApplication.TerminateReply.terminateCancel`](nsapplication/terminatereply/terminatecancel.md), and a return value of [`true`](https://developer.apple.com/documentation/swift/true) is equivalent to [`NSApplication.TerminateReply.terminateNow`](nsapplication/terminatereply/terminatenow.md).

#### Discussion

This method is called after the application’s Quit menu item has been selected, or after the [`terminate(_:)`](nsapplication/terminate(_:).md) method has been called. Generally, you should return [`NSApplication.TerminateReply.terminateNow`](nsapplication/terminatereply/terminatenow.md) to allow the termination to complete, but you can cancel the termination process or delay it somewhat as needed. For example, you might delay termination to finish processing some critical data but then terminate the application as soon as you are done by calling the [`reply(toApplicationShouldTerminate:)`](nsapplication/reply(toapplicationshouldterminate:).md) method.

## Parameters

- `sender`: The application object that is about to be terminated.

## See Also

- [func terminate(Any?)](nsapplication/terminate(_:).md)
  Terminates the receiver.
- [NSApplication.TerminateReply](nsapplication/terminatereply.md)
  Constants that determine whether an app should terminate.
- [func applicationShouldTerminateAfterLastWindowClosed(NSApplication) -> Bool](nsapplicationdelegate/applicationshouldterminateafterlastwindowclosed(_:).md)
  Returns a Boolean value that indicates if the app terminates once the last window closes.
- [func applicationWillTerminate(Notification)](nsapplicationdelegate/applicationwillterminate(_:).md)
  Tells the delegate that the app is about to terminate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationshouldterminate(_:))*