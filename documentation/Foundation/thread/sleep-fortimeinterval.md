# sleep(forTimeInterval:)

**Framework**: Foundation  
**Kind**: method

Sleeps the thread for a given time interval.

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
class func sleep(forTimeInterval ti: TimeInterval)
```

#### Discussion

No run loop processing occurs while the thread is blocked.

## Parameters

- `ti`: The duration of the sleep.

## See Also

- [class func sleep(until: Date)](thread/sleep(until:).md)
  Blocks the current thread until the time specified.
- [class func exit()](thread/exit.md)
  Terminates the current thread.
- [func cancel()](thread/cancel.md)
  Changes the cancelled state of the receiver to indicate that it should exit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/sleep(fortimeinterval:))*