# DASessionUnscheduleFromRunLoop(_:_:_:)

**Framework**: Disk Arbitration  
**Kind**: func  
**Role**: Function

Unschedules the session from a run loop.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DASessionUnscheduleFromRunLoop(_ session: DASession, _ runLoop: CFRunLoop, _ runLoopMode: CFString)
```

```c
extern void DASessionUnscheduleFromRunLoop(DASessionRef session, CFRunLoopRef runLoop, CFStringRef runLoopMode);
```

## Parameters

- `session`: The session which is being unscheduled.
- `runLoop`: The run loop on which the session is scheduled.
- `runLoopMode`: The run loop mode in which the session is scheduled.

## See Also

### Miscellaneous
- [func DASessionCreate(CFAllocator?) -> DASession?](./dasessioncreate%28_%29.md)
  Creates a new session.
- [func DASessionGetTypeID() -> CFTypeID](./dasessiongettypeid%28%29.md)
  Returns the type identifier of all DASession instances.
- [func DASessionScheduleWithRunLoop(DASession, CFRunLoop, CFString)](./dasessionschedulewithrunloop%28_,_,_%29.md)
  Schedules the session on a run loop.
- [func DASessionSetDispatchQueue(DASession, dispatch_queue_t?)](./dasessionsetdispatchqueue%28_,_%29.md)
  Schedules the session on a dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dasessionunschedulefromrunloop(_:_:_:))*