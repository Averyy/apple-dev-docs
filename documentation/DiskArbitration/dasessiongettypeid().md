# DASessionGetTypeID()

**Framework**: Disk Arbitration  
**Kind**: func  
**Role**: Function

Returns the type identifier of all DASession instances.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DASessionGetTypeID() -> CFTypeID
```

```c
extern CFTypeID DASessionGetTypeID();
```

## See Also

### Miscellaneous
- [func DASessionCreate(CFAllocator?) -> DASession?](./dasessioncreate%28_%29.md)
  Creates a new session.
- [func DASessionScheduleWithRunLoop(DASession, CFRunLoop, CFString)](./dasessionschedulewithrunloop%28_,_,_%29.md)
  Schedules the session on a run loop.
- [func DASessionSetDispatchQueue(DASession, dispatch_queue_t?)](./dasessionsetdispatchqueue%28_,_%29.md)
  Schedules the session on a dispatch queue.
- [func DASessionUnscheduleFromRunLoop(DASession, CFRunLoop, CFString)](./dasessionunschedulefromrunloop%28_,_,_%29.md)
  Unschedules the session from a run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dasessiongettypeid())*