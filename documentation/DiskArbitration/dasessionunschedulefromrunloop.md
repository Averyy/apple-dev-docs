# DASessionUnscheduleFromRunLoop(_:_:_:)

**Framework**: Disk Arbitration  
**Kind**: func

Unschedules the session from a run loop.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DASessionUnscheduleFromRunLoop(_ session: DASession, _ runLoop: CFRunLoop, _ runLoopMode: CFString)
```

## Parameters

- `session`: The session which is being unscheduled.
- `runLoop`: The run loop on which the session is scheduled.
- `runLoopMode`: The run loop mode in which the session is scheduled.

## See Also

- [func DASessionCreate(CFAllocator?) -> DASession?](dasessioncreate(_:).md)
  Creates a new session.
- [func DASessionGetTypeID() -> CFTypeID](dasessiongettypeid().md)
  Returns the type identifier of all DASession instances.
- [func DASessionScheduleWithRunLoop(DASession, CFRunLoop, CFString)](dasessionschedulewithrunloop(_:_:_:).md)
  Schedules the session on a run loop.
- [func DASessionSetDispatchQueue(DASession, dispatch_queue_t?)](dasessionsetdispatchqueue(_:_:).md)
  Schedules the session on a dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dasessionunschedulefromrunloop(_:_:_:))*