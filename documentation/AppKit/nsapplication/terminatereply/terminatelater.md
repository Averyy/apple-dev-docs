# NSApplication.TerminateReply.terminateLater

**Framework**: AppKit  
**Kind**: case

**Availability**:
- macOS ?+

## Declaration

```swift
case terminateLater
```

#### Discussion

It may be OK to proceed with termination later. Returning this value causes Cocoa to run the run loop in the [`NSModalPanelRunLoopMode`](nsmodalpanelrunloopmode.md) until your app subsequently calls [`reply(toApplicationShouldTerminate:)`](nsapplication/reply(toapplicationshouldterminate:).md) with the value [`true`](https://developer.apple.com/documentation/swift/true) or [`false`](https://developer.apple.com/documentation/swift/false). This return value is for delegates that need to provide document modal alerts (sheets) in order to decide whether to quit.

## See Also

- [NSApplication.TerminateReply.terminateNow](nsapplication/terminatereply/terminatenow.md)
  It is OK to proceed with termination.
- [NSApplication.TerminateReply.terminateCancel](nsapplication/terminatereply/terminatecancel.md)
  The app should not be terminated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/terminatereply/terminatelater)*