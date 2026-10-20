# exit()

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (void) exit;
```

#### Discussion

This method uses the [`current`](./current.md) class method to access the current thread. Before exiting the thread, this method posts the [`NSThreadWillExit`](../nsnotification/name-swift.struct/nsthreadwillexit.md) with the thread being exited to the default notification center. Because notifications are delivered synchronously, all observers of [`NSThreadWillExit`](../nsnotification/name-swift.struct/nsthreadwillexit.md) are guaranteed to receive the notification before the thread exits.

Invoking this method should be avoided as it does not give your thread a chance to clean up any resources it allocated during its execution.

## See Also

### Related Documentation
- [class var current: Thread](./current.md)
  Returns the thread object representing the current thread of execution.
### Stopping a Thread
- [class func sleep(until: Date)](./sleep%28until%29.md)
  Blocks the current thread until the time specified.
- [class func sleep(forTimeInterval: TimeInterval)](./sleep%28fortimeinterval%29.md)
  Sleeps the thread for a given time interval.
- [func cancel()](./cancel%28%29.md)
  Changes the cancelled state of the receiver to indicate that it should exit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/exit())*