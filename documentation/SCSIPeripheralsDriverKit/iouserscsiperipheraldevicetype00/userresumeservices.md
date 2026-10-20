# UserResumeServices

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: method  
**Role**: Instance Method

Resumes normal services after a suspension.

**Availability**:
- DriverKit 22.0+

## Declaration

```cpp
virtual kern_return_t UserResumeServices();
```

#### Return Value

A value that indicates the result of the resume request. [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) indicates success. For error definitions, see [IOKit Constants](../../iokit/iokit_constants.md).

#### Discussion

Call this method when the dext finishes using its window of exclusivity from a previous [`UserSuspendServices`](./usersuspendservices.md) call so file systems can continue communicating with the drive.

## See Also

### Suspending and resuming services
- [UserSuspendServices](./usersuspendservices.md)
  Suspends services and allows the dext to communicate with the external drive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype00/userresumeservices)*