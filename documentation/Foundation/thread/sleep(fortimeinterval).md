# sleep(forTimeInterval:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (void) sleepForTimeInterval:(NSTimeInterval) ti;
```

## Discussion

No run loop processing occurs while the thread is blocked.

## Parameters

- `ti`: The duration of the sleep.

## See Also

### Stopping a Thread
- [class func sleep(until: Date)](./sleep%28until%29.md)
  Blocks the current thread until the time specified.
- [class func exit()](./exit%28%29.md)
  Terminates the current thread.
- [func cancel()](./cancel%28%29.md)
  Changes the cancelled state of the receiver to indicate that it should exit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/sleep(fortimeinterval:))*