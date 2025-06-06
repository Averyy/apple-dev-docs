# startPeriodicEvents(afterDelay:withPeriod:)

**Framework**: AppKit  
**Kind**: method

Begins generating periodic events for the current thread.

**Availability**:
- macOS ?+

## Declaration

```swift
class func startPeriodicEvents(afterDelay delay: TimeInterval, withPeriod period: TimeInterval)
```

#### Discussion

Raises an `NSInternalInconsistencyException` if periodic events are already being generated for the current thread. This method is typically used in a modal loop while tracking mouse-dragged events.

## Parameters

- `delay`: The number of seconds that   should wait before beginning to generate periodic events.
- `period`: The period in seconds between the generated events.

## See Also

- [class func stopPeriodicEvents()](nsevent/stopperiodicevents.md)
  Stops generating periodic events for the current thread and discards any periodic events remaining in the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/startperiodicevents(afterdelay:withperiod:))*