# stopPeriodicEvents()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Stops generating periodic events for the current thread and discards any periodic events remaining in the queue.

**Availability**:
- macOS

## Declaration

```swift
class func stopPeriodicEvents()
```

```objc
+ (void) stopPeriodicEvents;
```

## Discussion

This message is ignored if periodic events aren’t currently being generated.

## See Also

### Requesting and stopping periodic events
- [class func startPeriodicEvents(afterDelay: TimeInterval, withPeriod: TimeInterval)](./startperiodicevents%28afterdelay,withperiod%29.md)
  Begins generating periodic events for the current thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/stopperiodicevents())*