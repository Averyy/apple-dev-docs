# UserDetermineDeviceCharacteristics

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: method

Performs enumeration-time initializations in response to a call from the framework.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
kern_return_t UserDetermineDeviceCharacteristics(bool * result);
```

#### Discussion

The kernel calls this user space method at enumeration time. Use this callback to perform any initializations your DriverKit extension (dext) needs to perform.

## Parameters

- `result`: On return, this value is   if initialization succeeds; otherwise,  .

## See Also

- [UserResetDevice](iouserscsiperipheraldevicetype00/userresetdevice.md)
  Performs a bus reset of the external drive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype00/userdeterminedevicecharacteristics)*