# UserDetermineDeviceCharacteristics

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: method  
**Role**: Instance Method

Performs enumeration-time initializations in response to a call from the framework.

**Availability**:
- DriverKit 22.0+

## Declaration

```cpp
virtual kern_return_t UserDetermineDeviceCharacteristics(bool *result);
```

## Discussion

The kernel calls this user space method at enumeration time. Use this callback to perform any initializations your DriverKit extension (dext) needs to perform.

## Parameters

- `result`: On return, this value is `true` if initialization succeeds; otherwise, `false`.

## See Also

### Managing the device
- [UserResetDevice](./userresetdevice.md)
  Performs a bus reset of the external drive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype00/userdeterminedevicecharacteristics)*