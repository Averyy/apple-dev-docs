# DASessionSetDispatchQueue(_:_:)

**Framework**: Disk Arbitration  
**Kind**: func

Schedules the session on a dispatch queue.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func DASessionSetDispatchQueue(_ session: DASession, _ queue: dispatch_queue_t?)
```

## Parameters

- `session`: The session which is being scheduled.
- `queue`: The dispatch queue on which the session should be scheduled. Pass NULL to unschedule.

## See Also

- [func DASessionCreate(CFAllocator?) -> DASession?](dasessioncreate(_:).md)
  Creates a new session.
- [func DASessionGetTypeID() -> CFTypeID](dasessiongettypeid().md)
  Returns the type identifier of all DASession instances.
- [func DASessionScheduleWithRunLoop(DASession, CFRunLoop, CFString)](dasessionschedulewithrunloop(_:_:_:).md)
  Schedules the session on a run loop.
- [func DASessionUnscheduleFromRunLoop(DASession, CFRunLoop, CFString)](dasessionunschedulefromrunloop(_:_:_:).md)
  Unschedules the session from a run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dasessionsetdispatchqueue(_:_:))*