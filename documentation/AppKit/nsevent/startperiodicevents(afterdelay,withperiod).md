# startPeriodicEvents(afterDelay:withPeriod:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Begins generating periodic events for the current thread.

**Availability**:
- macOS

## Declaration

```swift
class func startPeriodicEvents(afterDelay delay: TimeInterval, withPeriod period: TimeInterval)
```

```objc
+ (void) startPeriodicEventsAfterDelay:(NSTimeInterval) delay withPeriod:(NSTimeInterval) period;
```

## Discussion

Raises an `NSInternalInconsistencyException` if periodic events are already being generated for the current thread. This method is typically used in a modal loop while tracking mouse-dragged events.

## Parameters

- `delay`: The number of seconds that `NSEvent` should wait before beginning to generate periodic events.
- `period`: The period in seconds between the generated events.

## See Also

### Requesting and stopping periodic events
- [class func stopPeriodicEvents()](./stopperiodicevents%28%29.md)
  Stops generating periodic events for the current thread and discards any periodic events remaining in the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/startperiodicevents(afterdelay:withperiod:))*