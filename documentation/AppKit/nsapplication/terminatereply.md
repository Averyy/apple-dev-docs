# NSApplication.TerminateReply

**Framework**: AppKit  
**Kind**: enum

Constants that determine whether an app should terminate.

**Availability**:
- macOS ?+

## Declaration

```swift
enum TerminateReply
```

## Topics

### Constants
- [NSApplication.TerminateReply.terminateNow](nsapplication/terminatereply/terminatenow.md)
  It is OK to proceed with termination.
- [NSApplication.TerminateReply.terminateCancel](nsapplication/terminatereply/terminatecancel.md)
  The app should not be terminated.
- [NSApplication.TerminateReply.terminateLater](nsapplication/terminatereply/terminatelater.md)
### Initializers
- [init?(rawValue: UInt)](nsapplication/terminatereply/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func applicationShouldTerminate(NSApplication) -> NSApplication.TerminateReply](nsapplicationdelegate/applicationshouldterminate(_:).md)
  Returns a value that indicates if the app should terminate.
- [func applicationShouldTerminateAfterLastWindowClosed(NSApplication) -> Bool](nsapplicationdelegate/applicationshouldterminateafterlastwindowclosed(_:).md)
  Returns a Boolean value that indicates if the app terminates once the last window closes.
- [func applicationWillTerminate(Notification)](nsapplicationdelegate/applicationwillterminate(_:).md)
  Tells the delegate that the app is about to terminate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/terminatereply)*