# applicationShouldTerminate(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a value that indicates if the app should terminate.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func applicationShouldTerminate(_ sender: NSApplication) -> NSApplication.TerminateReply
```

```objc
- (NSApplicationTerminateReply) applicationShouldTerminate:(NSApplication *) sender;
```

## Return Value

One of the values defined in [`NSApplication.TerminateReply`](../nsapplication/terminatereply.md) constants indicating whether the application should terminate. For compatibility reasons, a return value of [`false`](../../Swift/false.md) is equivalent to [`NSApplication.TerminateReply.terminateCancel`](../nsapplication/terminatereply/terminatecancel.md), and a return value of [`true`](../../Swift/true.md) is equivalent to [`NSApplication.TerminateReply.terminateNow`](../nsapplication/terminatereply/terminatenow.md).

## Discussion

This method is called after the application’s Quit menu item has been selected, or after the [`terminate(_:)`](../nsapplication/terminate%28_%29.md) method has been called. Generally, you should return [`NSApplication.TerminateReply.terminateNow`](../nsapplication/terminatereply/terminatenow.md) to allow the termination to complete, but you can cancel the termination process or delay it somewhat as needed. For example, you might delay termination to finish processing some critical data but then terminate the application as soon as you are done by calling the [`reply(toApplicationShouldTerminate:)`](../nsapplication/reply%28toapplicationshouldterminate%29.md) method.

## Parameters

- `sender`: The application object that is about to be terminated.

## See Also

### Related Documentation
- [func terminate(Any?)](../nsapplication/terminate%28_%29.md)
  Terminates the receiver.
### Terminating Applications
- [NSApplication.TerminateReply](../nsapplication/terminatereply.md)
  Constants that determine whether an app should terminate.
- [func applicationShouldTerminateAfterLastWindowClosed(NSApplication) -> Bool](./applicationshouldterminateafterlastwindowclosed%28_%29.md)
  Returns a Boolean value that indicates if the app terminates once the last window closes.
- [func applicationWillTerminate(Notification)](./applicationwillterminate%28_%29.md)
  Tells the delegate that the app is about to terminate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationshouldterminate(_:))*