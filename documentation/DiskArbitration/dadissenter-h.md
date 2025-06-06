# DADissenter.h

**Framework**: Disk Arbitration

#### Overview

See the Overview section above for header-level documentation.

#### Overview

##### Included Headers

- <mach/error.h>
- <CoreFoundation/CoreFoundation.h>

## Topics

### Miscellaneous
- [func DADissenterCreate(CFAllocator?, DAReturn, CFString?) -> DADissenter](dadissentercreate(_:_:_:).md)
  Creates a new dissenter object.
- [func DADissenterGetStatus(DADissenter) -> DAReturn](dadissentergetstatus(_:).md)
  Obtains the return code.
- [func DADissenterGetStatusString(DADissenter) -> CFString?](dadissentergetstatusstring(_:).md)
  Obtains the return code string.
### Data Types
- [class DADissenter](dadissenter.md)
  Type of a reference to DADissenter instances.

## See Also

- [DADisk.h](dadisk-h.md)
- [DASession.h](dasession-h.md)
- [DiskArbitration.h](diskarbitration-h.md)
  Register for mount/unmount notifications, and block mount/unmount events.
- [DiskArbitration Enumerations](diskarbitration-enumerations.md)
- [DiskArbitration Constants](diskarbitration-constants.md)
- [DiskArbitration Data Types](diskarbitration-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dadissenter-h)*