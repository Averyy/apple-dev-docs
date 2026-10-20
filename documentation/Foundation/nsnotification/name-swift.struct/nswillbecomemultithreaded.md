# NSWillBecomeMultiThreaded

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Posted when the first thread is detached from the current thread. The `NSThread` class posts this notification at most once—the first time a thread is detached using [`detachNewThreadSelector(_:toTarget:with:)`](../../thread/detachnewthreadselector%28_,totarget,with%29.md) or the [`start()`](../../thread/start%28%29.md) method. Subsequent invocations of those methods do not post this notification. Observers of this notification have their notification method invoked in the main thread, not the new thread. The observer notification methods always execute before the new thread begins executing.

**Availability**:
- iOS 2.0+ - Deprecated in 26.0
- iPadOS 2.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.0+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 2.0+ - Deprecated in 26.0

> **Deprecated**: This notification does not protect against data races

## Declaration

```swift
static let NSWillBecomeMultiThreaded: NSNotification.Name
```

```c
extern NSNotificationName const NSWillBecomeMultiThreadedNotification;
```

#### Discussion

This notification does not contain a notification object or a `userInfo` dictionary.

## See Also

### Notifications
- [static let NSDidBecomeSingleThreaded: NSNotification.Name](./nsdidbecomesinglethreaded.md)
  Not implemented.
- [static let NSThreadWillExit: NSNotification.Name](./nsthreadwillexit.md)
  An `NSThread` object posts this notification when it receives the [`exit()`](../../thread/exit%28%29.md) message, before the thread exits. Observer methods invoked to receive this notification execute in the exiting thread, before it exits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nswillbecomemultithreaded)*