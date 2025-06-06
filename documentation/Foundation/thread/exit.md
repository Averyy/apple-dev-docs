# exit()

**Framework**: Foundation  
**Kind**: method

Terminates the current thread.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func exit()
```

#### Discussion

This method uses the [`current`](thread/current.md) class method to access the current thread. Before exiting the thread, this method posts the [`NSThreadWillExit`](nsnotification/name-swift.struct/nsthreadwillexit.md) with the thread being exited to the default notification center. Because notifications are delivered synchronously, all observers of [`NSThreadWillExit`](nsnotification/name-swift.struct/nsthreadwillexit.md) are guaranteed to receive the notification before the thread exits.

Invoking this method should be avoided as it does not give your thread a chance to clean up any resources it allocated during its execution.

## See Also

- [class var current: Thread](thread/current.md)
  Returns the thread object representing the current thread of execution.
- [class func sleep(until: Date)](thread/sleep(until:).md)
  Blocks the current thread until the time specified.
- [class func sleep(forTimeInterval: TimeInterval)](thread/sleep(fortimeinterval:).md)
  Sleeps the thread for a given time interval.
- [func cancel()](thread/cancel.md)
  Changes the cancelled state of the receiver to indicate that it should exit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/exit())*