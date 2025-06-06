# UserSuspendServices

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: method

Suspends services and allows the dext to communicate with the external drive.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
kern_return_t UserSuspendServices();
```

#### Return Value

A value that indicates the result of the suspend request. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

This method allows the dext to try to obtain a clear window to communicate with the external drive. Calling this method attempts to close any open references to the media. This informs file systems that someone is accessing the media. You can use this cleared window of communication for things like firmware updates without risking harm to the user’s data.

This call expects you to unmount existing volumes upstream of this drive before invoking this API. You can use the [`Disk Arbitration`](https://developer.apple.com/documentation/DiskArbitration) APIs to programmatically unmount any such volumes.

To prevent power state transitions during this window, you can optionally acquire a power assertion before invoking this API.

## See Also

- [UserResumeServices](iouserscsiperipheraldevicetype05/userresumeservices.md)
  Resumes normal services after a suspension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype05/usersuspendservices)*