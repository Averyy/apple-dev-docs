# applicationWillTerminate(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the app is about to terminate.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationWillTerminate(_ notification: Notification)
```

```objc
- (void) applicationWillTerminate:(NSNotification *) notification;
```

## Discussion

Your delegate can use this method to perform any final cleanup before the app terminates.  The app will terminate after this method returns.

> **Note**: This method isn’t called during sudden termination of an app. For more information about sudden termination, see the section  [`ProcessInfo`](../../Foundation/processinfo.md) of [`ProcessInfo`](../../Foundation/processinfo.md).

## Parameters

- `notification`: A notification named [`willTerminateNotification`](../nsapplication/willterminatenotification.md). Calling the [`object`](../../Foundation/nsnotification/object.md) method of this notification returns the `NSApplication` object itself.

## See Also

### Related Documentation
- [func terminate(Any?)](../nsapplication/terminate%28_%29.md)
  Terminates the receiver.
### Terminating Applications
- [func applicationShouldTerminate(NSApplication) -> NSApplication.TerminateReply](./applicationshouldterminate%28_%29.md)
  Returns a value that indicates if the app should terminate.
- [NSApplication.TerminateReply](../nsapplication/terminatereply.md)
  Constants that determine whether an app should terminate.
- [func applicationShouldTerminateAfterLastWindowClosed(NSApplication) -> Bool](./applicationshouldterminateafterlastwindowclosed%28_%29.md)
  Returns a Boolean value that indicates if the app terminates once the last window closes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationwillterminate(_:))*