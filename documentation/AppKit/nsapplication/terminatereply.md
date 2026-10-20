# NSApplication.TerminateReply

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that determine whether an app should terminate.

**Availability**:
- macOS

## Declaration

```swift
enum TerminateReply
```

```c
enum NSApplicationTerminateReply : NSUInteger;
```

## Topics

### Constants
- [NSApplication.TerminateReply.terminateNow](./terminatereply/terminatenow.md)
  It is OK to proceed with termination.
- [NSApplication.TerminateReply.terminateCancel](./terminatereply/terminatecancel.md)
  The app should not be terminated.
- [NSApplication.TerminateReply.terminateLater](./terminatereply/terminatelater.md)
### Initializers
- [init?(rawValue: UInt)](./terminatereply/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Terminating Applications
- [func applicationShouldTerminate(NSApplication) -> NSApplication.TerminateReply](../nsapplicationdelegate/applicationshouldterminate%28_%29.md)
  Returns a value that indicates if the app should terminate.
- [func applicationShouldTerminateAfterLastWindowClosed(NSApplication) -> Bool](../nsapplicationdelegate/applicationshouldterminateafterlastwindowclosed%28_%29.md)
  Returns a Boolean value that indicates if the app terminates once the last window closes.
- [func applicationWillTerminate(Notification)](../nsapplicationdelegate/applicationwillterminate%28_%29.md)
  Tells the delegate that the app is about to terminate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/terminatereply)*