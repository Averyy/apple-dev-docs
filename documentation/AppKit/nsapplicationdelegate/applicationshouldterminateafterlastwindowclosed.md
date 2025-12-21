# applicationShouldTerminateAfterLastWindowClosed(_:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates if the app terminates once the last window closes.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func applicationShouldTerminateAfterLastWindowClosed(_ sender: NSApplication) -> Bool
```

#### Return Value

[`false`](https://developer.apple.com/documentation/Swift/false) if the application should not be terminated when its last window is closed; otherwise, [`true`](https://developer.apple.com/documentation/Swift/true) to terminate the application.

#### Discussion

The application sends this message to your delegate when the application’s last window is closed. It sends this message regardless of whether there are still panels open. (A panel in this case is defined as being an instance of `NSPanel` or one of its subclasses.)

If your implementation returns [`false`](https://developer.apple.com/documentation/Swift/false), control returns to the main event loop and the application is not terminated. If you return [`true`](https://developer.apple.com/documentation/Swift/true), your delegate’s [`applicationShouldTerminate(_:)`](nsapplicationdelegate/applicationshouldterminate(_:).md) method is subsequently invoked to confirm that the application should be terminated.

## Parameters

- `sender`: The application object whose last window was closed.

## See Also

- [func terminate(Any?)](nsapplication/terminate(_:).md)
  Terminates the receiver.
- [func applicationShouldTerminate(NSApplication) -> NSApplication.TerminateReply](nsapplicationdelegate/applicationshouldterminate(_:).md)
  Returns a value that indicates if the app should terminate.
- [NSApplication.TerminateReply](nsapplication/terminatereply.md)
  Constants that determine whether an app should terminate.
- [func applicationWillTerminate(Notification)](nsapplicationdelegate/applicationwillterminate(_:).md)
  Tells the delegate that the app is about to terminate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationshouldterminateafterlastwindowclosed(_:))*