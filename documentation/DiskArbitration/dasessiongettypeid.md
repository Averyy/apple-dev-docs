# DASessionGetTypeID()

**Framework**: Disk Arbitration  
**Kind**: func

Returns the type identifier of all DASession instances.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DASessionGetTypeID() -> CFTypeID
```

## See Also

- [func DASessionCreate(CFAllocator?) -> DASession?](dasessioncreate(_:).md)
  Creates a new session.
- [func DASessionScheduleWithRunLoop(DASession, CFRunLoop, CFString)](dasessionschedulewithrunloop(_:_:_:).md)
  Schedules the session on a run loop.
- [func DASessionSetDispatchQueue(DASession, dispatch_queue_t?)](dasessionsetdispatchqueue(_:_:).md)
  Schedules the session on a dispatch queue.
- [func DASessionUnscheduleFromRunLoop(DASession, CFRunLoop, CFString)](dasessionunschedulefromrunloop(_:_:_:).md)
  Unschedules the session from a run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dasessiongettypeid())*