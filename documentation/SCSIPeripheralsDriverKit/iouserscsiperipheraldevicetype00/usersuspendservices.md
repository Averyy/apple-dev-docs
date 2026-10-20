# UserSuspendServices

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: method  
**Role**: Instance Method

Suspends services and allows the dext to communicate with the external drive.

**Availability**:
- DriverKit 22.0+

## Declaration

```cpp
virtual kern_return_t UserSuspendServices();
```

#### Return Value

A value that indicates the result of the suspend request. [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) indicates success. For error definitions, see [IOKit Constants](../../iokit/iokit_constants.md).

#### Discussion

This method allows the dext to try to obtain a clear window to communicate with the external drive. Calling this method attempts to close any open references to the media. This informs file systems that someone is accessing the media. You can use this cleared window of communication for things like firmware updates without risking harm to the user’s data.

This call expects you to unmount existing volumes upstream of this drive before invoking this API. You can use the [Disk Arbitration](../../DiskArbitration/DiskArbitration.md) APIs to programmatically unmount any such volumes.

To prevent power state transitions during this window, you can optionally acquire a power assertion before invoking this API.

> **Note**: Make sure your dext obtains exclusive access to the drive using this API before sending any vendor-specific commands using [`UserSendCDB`](./usersendcdb.md).

## See Also

### Suspending and resuming services
- [UserResumeServices](./userresumeservices.md)
  Resumes normal services after a suspension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype00/usersuspendservices)*