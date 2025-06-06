# sleep(until:)

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

No run loop processing occurs while the thread is blocked.

## Parameters

- `date`: The time at which to resume processing.

## See Also

- [class var current: Thread](thread/current.md)
  Returns the thread object representing the current thread of execution.
- [class func sleep(forTimeInterval: TimeInterval)](thread/sleep(fortimeinterval:).md)
  Sleeps the thread for a given time interval.
- [class func exit()](thread/exit.md)
  Terminates the current thread.
- [func cancel()](thread/cancel.md)
  Changes the cancelled state of the receiver to indicate that it should exit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/sleep(until:))*