# applicationWillTerminate(_:)

**Framework**: Appkit  
**Kind**: method

Tells the delegate that the app is about to terminate.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationWillTerminate(_ notification: Notification)
```

#### Discussion

Your delegate can use this method to perform any final cleanup before the app terminates.  The app will terminate after this method returns.

> **Note**: This method isn’t called during sudden termination of an app. For more information about sudden termination, see the section  [`ProcessInfo`](https://developer.apple.com/documentation/Foundation/ProcessInfo) of [`ProcessInfo`](https://developer.apple.com/documentation/Foundation/ProcessInfo).

## Parameters

- `notification`: A notification named  . Calling the   method of this notification returns the   object itself.

## See Also

- [func terminate(Any?)](nsapplication/terminate(_:).md)
  Terminates the receiver.
- [func applicationShouldTerminate(NSApplication) -> NSApplication.TerminateReply](nsapplicationdelegate/applicationshouldterminate(_:).md)
  Returns a value that indicates if the app should terminate.
- [NSApplication.TerminateReply](nsapplication/terminatereply.md)
  Constants that determine whether an app should terminate.
- [func applicationShouldTerminateAfterLastWindowClosed(NSApplication) -> Bool](nsapplicationdelegate/applicationshouldterminateafterlastwindowclosed(_:).md)
  Returns a Boolean value that indicates if the app terminates once the last window closes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationwillterminate(_:))*