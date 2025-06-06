# fCompletionStatus

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: property

The status of the task at completion of the call, such as good, busy, or timeout.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
SCSITaskStatus fCompletionStatus;
```

#### Discussion

Use the values that [`SCSITaskStatus`](https://developer.apple.com/documentation/iokit/scsitaskstatus) defines to evaluate this field.

## See Also

- [fServiceResponse](scsideviceinparameters/fserviceresponse.md)
  The response from the service, such as complete, in process, or rejected.
- [fRealizedByteCountOfTransfer](scsideviceinparameters/frealizedbytecountoftransfer.md)
  The byte count of the tranferred data.
- [fSenseDataValid](scsideviceinparameters/fsensedatavalid.md)
  A Boolean value that indicates whether the sense data that the kernel provides is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsideviceinparameters/fcompletionstatus)*