# DASessionSetDispatchQueue(_:_:)

**Framework**: Disk Arbitration  
**Kind**: func  
**Role**: Function

Schedules the session on a dispatch queue.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func DASessionSetDispatchQueue(_ session: DASession, _ queue: dispatch_queue_t?)
```

```c
extern void DASessionSetDispatchQueue(DASessionRef session, dispatch_queue_t queue);
```

## Parameters

- `session`: The session which is being scheduled.
- `queue`: The dispatch queue on which the session should be scheduled. Pass NULL to unschedule.

## See Also

### Miscellaneous
- [func DASessionCreate(CFAllocator?) -> DASession?](./dasessioncreate%28_%29.md)
  Creates a new session.
- [func DASessionGetTypeID() -> CFTypeID](./dasessiongettypeid%28%29.md)
  Returns the type identifier of all DASession instances.
- [func DASessionScheduleWithRunLoop(DASession, CFRunLoop, CFString)](./dasessionschedulewithrunloop%28_,_,_%29.md)
  Schedules the session on a run loop.
- [func DASessionUnscheduleFromRunLoop(DASession, CFRunLoop, CFString)](./dasessionunschedulefromrunloop%28_,_,_%29.md)
  Unschedules the session from a run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dasessionsetdispatchqueue(_:_:))*