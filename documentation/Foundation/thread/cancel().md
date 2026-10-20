# cancel()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Changes the cancelled state of the receiver to indicate that it should exit.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func cancel()
```

```objc
- (void) cancel;
```

#### Discussion

The semantics of this method are the same as those used for [`Operation`](../operation.md). This method sets state information in the receiver that is then reflected by the [`isCancelled`](./iscancelled.md) property. Threads that support cancellation should periodically call the [`isCancelled`](./iscancelled.md) method to determine if the thread has in fact been cancelled, and exit if it has been.

For more information about cancellation and operation objects, see [`Operation`](../operation.md).

## See Also

### Related Documentation
- [var isCancelled: Bool](./iscancelled.md)
  A Boolean value that indicates whether the receiver is cancelled.
### Stopping a Thread
- [class func sleep(until: Date)](./sleep%28until%29.md)
  Blocks the current thread until the time specified.
- [class func sleep(forTimeInterval: TimeInterval)](./sleep%28fortimeinterval%29.md)
  Sleeps the thread for a given time interval.
- [class func exit()](./exit%28%29.md)
  Terminates the current thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/cancel())*