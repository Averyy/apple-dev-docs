# NSWillBecomeMultiThreaded

**Framework**: Foundation  
**Kind**: property

Posted when the first thread is detached from the current thread. The `NSThread` class posts this notification at most once—the first time a thread is detached using [`detachNewThreadSelector(_:toTarget:with:)`](thread/detachnewthreadselector(_:totarget:with:).md) or the [`start()`](thread/start().md) method. Subsequent invocations of those methods do not post this notification. Observers of this notification have their notification method invoked in the main thread, not the new thread. The observer notification methods always execute before the new thread begins executing.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let NSWillBecomeMultiThreaded: NSNotification.Name
```

#### Discussion

This notification does not contain a notification object or a `userInfo` dictionary.

## See Also

- [static let NSDidBecomeSingleThreaded: NSNotification.Name](nsnotification/name-swift.struct/nsdidbecomesinglethreaded.md)
  Not implemented.
- [static let NSThreadWillExit: NSNotification.Name](nsnotification/name-swift.struct/nsthreadwillexit.md)
  An `NSThread` object posts this notification when it receives the [`exit()`](thread/exit().md) message, before the thread exits. Observer methods invoked to receive this notification execute in the exiting thread, before it exits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nswillbecomemultithreaded)*