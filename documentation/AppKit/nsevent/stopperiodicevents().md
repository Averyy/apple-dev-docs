# stopPeriodicEvents()

**Framework**: AppKit  
**Kind**: method

Stops generating periodic events for the current thread and discards any periodic events remaining in the queue.

**Availability**:
- macOS ?+

## Declaration

```swift
class func stopPeriodicEvents()
```

#### Discussion

This message is ignored if periodic events aren’t currently being generated.

## See Also

- [class func startPeriodicEvents(afterDelay: TimeInterval, withPeriod: TimeInterval)](nsevent/startperiodicevents(afterdelay:withperiod:).md)
  Begins generating periodic events for the current thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/stopperiodicevents())*