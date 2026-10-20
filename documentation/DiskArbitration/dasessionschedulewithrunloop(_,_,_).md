# DASessionScheduleWithRunLoop(_:_:_:)

**Framework**: Disk Arbitration  
**Kind**: func  
**Role**: Function

Schedules the session on a run loop.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DASessionScheduleWithRunLoop(_ session: DASession, _ runLoop: CFRunLoop, _ runLoopMode: CFString)
```

```c
extern void DASessionScheduleWithRunLoop(DASessionRef session, CFRunLoopRef runLoop, CFStringRef runLoopMode);
```

## Parameters

- `session`: The session which is being scheduled.
- `runLoop`: The run loop on which the session should be scheduled.
- `runLoopMode`: The run loop mode in which the session should be scheduled.

## See Also

### Miscellaneous
- [func DASessionCreate(CFAllocator?) -> DASession?](./dasessioncreate%28_%29.md)
  Creates a new session.
- [func DASessionGetTypeID() -> CFTypeID](./dasessiongettypeid%28%29.md)
  Returns the type identifier of all DASession instances.
- [func DASessionSetDispatchQueue(DASession, dispatch_queue_t?)](./dasessionsetdispatchqueue%28_,_%29.md)
  Schedules the session on a dispatch queue.
- [func DASessionUnscheduleFromRunLoop(DASession, CFRunLoop, CFString)](./dasessionunschedulefromrunloop%28_,_,_%29.md)
  Unschedules the session from a run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dasessionschedulewithrunloop(_:_:_:))*