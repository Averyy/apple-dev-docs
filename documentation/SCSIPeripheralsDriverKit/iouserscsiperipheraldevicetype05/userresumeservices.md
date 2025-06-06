# UserResumeServices

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: method

Resumes normal services after a suspension.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
kern_return_t UserResumeServices();
```

#### Return Value

A value that indicates the result of the resume request. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

Call this method when the dext finishes using its window of exclusivity from a previous [`UserSuspendServices`](iouserscsiperipheraldevicetype05/usersuspendservices.md) call so file systems can continue communicating with the drive.

## See Also

- [UserSuspendServices](iouserscsiperipheraldevicetype05/usersuspendservices.md)
  Suspends services and allows the dext to communicate with the external drive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype05/userresumeservices)*