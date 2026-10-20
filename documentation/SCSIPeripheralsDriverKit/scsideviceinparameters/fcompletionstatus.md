# fCompletionStatus

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: property  
**Role**: Instance Property

The status of the task at completion of the call, such as good, busy, or timeout.

**Availability**:
- DriverKit 22.0+

## Declaration

```c
SCSITaskStatus fCompletionStatus;
```

#### Discussion

Use the values that [`SCSITaskStatus`](../../iokit/scsitaskstatus.md) defines to evaluate this field.

## See Also

### Accessing response properties
- [fServiceResponse](./fserviceresponse.md)
  The response from the service, such as complete, in process, or rejected.
- [fRealizedByteCountOfTransfer](./frealizedbytecountoftransfer.md)
  The byte count of the tranferred data.
- [fSenseDataValid](./fsensedatavalid.md)
  A Boolean value that indicates whether the sense data that the kernel provides is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsideviceinparameters/fcompletionstatus)*