# NSApplication.TerminateReply.terminateLater

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

**Availability**:
- macOS

## Declaration

```swift
case terminateLater
```

```c
NSTerminateLater
```

#### Discussion

It may be OK to proceed with termination later. Returning this value causes Cocoa to run the run loop in the [`NSModalPanelRunLoopMode`](../../nsmodalpanelrunloopmode.md) until your app subsequently calls [`reply(toApplicationShouldTerminate:)`](../reply%28toapplicationshouldterminate%29.md) with the value [`true`](../../../Swift/true.md) or [`false`](../../../Swift/false.md). This return value is for delegates that need to provide document modal alerts (sheets) in order to decide whether to quit.

## See Also

### Constants
- [NSApplication.TerminateReply.terminateNow](./terminatenow.md)
  It is OK to proceed with termination.
- [NSApplication.TerminateReply.terminateCancel](./terminatecancel.md)
  The app should not be terminated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/terminatereply/terminatelater)*