# fServiceResponse

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: property  
**Role**: Instance Property

The response from the service, such as complete, in process, or rejected.

**Availability**:
- DriverKit 22.0+

## Declaration

```c
SCSIServiceResponse fServiceResponse;
```

#### Discussion

Use the values that [`SCSIServiceResponse`](../../iokit/scsiserviceresponse.md) defines to evaluate this field.

## See Also

### Accessing response properties
- [fCompletionStatus](./fcompletionstatus.md)
  The status of the task at completion of the call, such as good, busy, or timeout.
- [fRealizedByteCountOfTransfer](./frealizedbytecountoftransfer.md)
  The byte count of the tranferred data.
- [fSenseDataValid](./fsensedatavalid.md)
  A Boolean value that indicates whether the sense data that the kernel provides is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsideviceinparameters/fserviceresponse)*