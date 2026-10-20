# applicationShouldTerminateAfterLastWindowClosed(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates if the app terminates once the last window closes.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func applicationShouldTerminateAfterLastWindowClosed(_ sender: NSApplication) -> Bool
```

```objc
- (BOOL) applicationShouldTerminateAfterLastWindowClosed:(NSApplication *) sender;
```

#### Return Value

[`false`](../../Swift/false.md) if the application should not be terminated when its last window is closed; otherwise, [`true`](../../Swift/true.md) to terminate the application.

#### Discussion

The application sends this message to your delegate when the application’s last window is closed. It sends this message regardless of whether there are still panels open. (A panel in this case is defined as being an instance of `NSPanel` or one of its subclasses.)

If your implementation returns [`false`](../../Swift/false.md), control returns to the main event loop and the application is not terminated. If you return [`true`](../../Swift/true.md), your delegate’s [`applicationShouldTerminate(_:)`](./applicationshouldterminate%28_%29.md) method is subsequently invoked to confirm that the application should be terminated.

## Parameters

- `sender`: The application object whose last window was closed.

## See Also

### Related Documentation
- [func terminate(Any?)](../nsapplication/terminate%28_%29.md)
  Terminates the receiver.
### Terminating Applications
- [func applicationShouldTerminate(NSApplication) -> NSApplication.TerminateReply](./applicationshouldterminate%28_%29.md)
  Returns a value that indicates if the app should terminate.
- [NSApplication.TerminateReply](../nsapplication/terminatereply.md)
  Constants that determine whether an app should terminate.
- [func applicationWillTerminate(Notification)](./applicationwillterminate%28_%29.md)
  Tells the delegate that the app is about to terminate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationshouldterminateafterlastwindowclosed(_:))*