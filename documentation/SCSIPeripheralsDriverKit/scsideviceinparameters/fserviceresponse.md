# fServiceResponse

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: property

The response from the service, such as complete, in process, or rejected.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
SCSIServiceResponse fServiceResponse;
```

#### Discussion

Use the values that [`SCSIServiceResponse`](https://developer.apple.com/documentation/iokit/scsiserviceresponse) defines to evaluate this field.

## See Also

- [fCompletionStatus](scsideviceinparameters/fcompletionstatus.md)
  The status of the task at completion of the call, such as good, busy, or timeout.
- [fRealizedByteCountOfTransfer](scsideviceinparameters/frealizedbytecountoftransfer.md)
  The byte count of the tranferred data.
- [fSenseDataValid](scsideviceinparameters/fsensedatavalid.md)
  A Boolean value that indicates whether the sense data that the kernel provides is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsideviceinparameters/fserviceresponse)*