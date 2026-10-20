# sleep(until:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Blocks the current thread until the time specified.

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
class func sleep(until date: Date)
```

```objc
+ (void) sleepUntilDate:(NSDate *) date;
```

#### Discussion

No run loop processing occurs while the thread is blocked.

## Parameters

- `date`: The time at which to resume processing.

## See Also

### Related Documentation
- [class var current: Thread](./current.md)
  Returns the thread object representing the current thread of execution.
### Stopping a Thread
- [class func sleep(forTimeInterval: TimeInterval)](./sleep%28fortimeinterval%29.md)
  Sleeps the thread for a given time interval.
- [class func exit()](./exit%28%29.md)
  Terminates the current thread.
- [func cancel()](./cancel%28%29.md)
  Changes the cancelled state of the receiver to indicate that it should exit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/sleep(until:))*