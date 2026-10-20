# DASessionCreate(_:)

**Framework**: Disk Arbitration  
**Kind**: func  
**Role**: Function

Creates a new session.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DASessionCreate(_ allocator: CFAllocator?) -> DASession?
```

```c
extern DASessionRefDASessionCreate(CFAllocatorRef allocator);
```

#### Return Value

A reference to a new DASession.

#### Discussion

The caller of this function receives a reference to the returned object. The caller also implicitly retains the object and is responsible for releasing it.

## See Also

### Miscellaneous
- [func DASessionGetTypeID() -> CFTypeID](./dasessiongettypeid%28%29.md)
  Returns the type identifier of all DASession instances.
- [func DASessionScheduleWithRunLoop(DASession, CFRunLoop, CFString)](./dasessionschedulewithrunloop%28_,_,_%29.md)
  Schedules the session on a run loop.
- [func DASessionSetDispatchQueue(DASession, dispatch_queue_t?)](./dasessionsetdispatchqueue%28_,_%29.md)
  Schedules the session on a dispatch queue.
- [func DASessionUnscheduleFromRunLoop(DASession, CFRunLoop, CFString)](./dasessionunschedulefromrunloop%28_,_,_%29.md)
  Unschedules the session from a run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dasessioncreate(_:))*