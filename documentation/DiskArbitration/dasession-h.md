# DASession.h

**Framework**: Disk Arbitration  
**Role**: API Collection

## Overview

See the Overview section above for header-level documentation.

## Overview

### Included Headers

- <CoreFoundation/CoreFoundation.h>

## Topics

### Miscellaneous
- [func DASessionCreate(CFAllocator?) -> DASession?](./dasessioncreate%28_%29.md)
  Creates a new session.
- [func DASessionGetTypeID() -> CFTypeID](./dasessiongettypeid%28%29.md)
  Returns the type identifier of all DASession instances.
- [func DASessionScheduleWithRunLoop(DASession, CFRunLoop, CFString)](./dasessionschedulewithrunloop%28_,_,_%29.md)
  Schedules the session on a run loop.
- [func DASessionSetDispatchQueue(DASession, dispatch_queue_t?)](./dasessionsetdispatchqueue%28_,_%29.md)
  Schedules the session on a dispatch queue.
- [func DASessionUnscheduleFromRunLoop(DASession, CFRunLoop, CFString)](./dasessionunschedulefromrunloop%28_,_,_%29.md)
  Unschedules the session from a run loop.
### Data Types
- [class DASession](./dasession.md)
  Type of a reference to DASession instances.

## See Also

### Reference
- [DADisk.h](./dadisk-h.md)
- [DADissenter.h](./dadissenter-h.md)
- [DiskArbitration.h](./diskarbitration-h.md)
  Register for mount/unmount notifications, and block mount/unmount events.
- [DiskArbitration Enumerations](./diskarbitration-enumerations.md)
- [DiskArbitration Constants](./diskarbitration-constants.md)
- [DiskArbitration Data Types](./diskarbitration-data-types.md)
- [DiskArbitration Functions](./diskarbitration-functions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dasession-h)*