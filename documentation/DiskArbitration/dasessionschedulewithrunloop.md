# DASessionScheduleWithRunLoop(_:_:_:)

**Framework**: Disk Arbitration  
**Kind**: func

Schedules the session on a run loop.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DASessionScheduleWithRunLoop(_ session: DASession, _ runLoop: CFRunLoop, _ runLoopMode: CFString)
```

## Parameters

- `session`: The session which is being scheduled.
- `runLoop`: The run loop on which the session should be scheduled.
- `runLoopMode`: The run loop mode in which the session should be scheduled.

## See Also

- [func DASessionCreate(CFAllocator?) -> DASession?](dasessioncreate(_:).md)
  Creates a new session.
- [func DASessionGetTypeID() -> CFTypeID](dasessiongettypeid().md)
  Returns the type identifier of all DASession instances.
- [func DASessionSetDispatchQueue(DASession, dispatch_queue_t?)](dasessionsetdispatchqueue(_:_:).md)
  Schedules the session on a dispatch queue.
- [func DASessionUnscheduleFromRunLoop(DASession, CFRunLoop, CFString)](dasessionunschedulefromrunloop(_:_:_:).md)
  Unschedules the session from a run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dasessionschedulewithrunloop(_:_:_:))*