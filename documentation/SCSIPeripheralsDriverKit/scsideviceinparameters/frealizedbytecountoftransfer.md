# fRealizedByteCountOfTransfer

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: property  
**Role**: Instance Property

The byte count of the tranferred data.

**Availability**:
- DriverKit 22.0+

## Declaration

```c
uint64_t fRealizedByteCountOfTransfer;
```

## See Also

### Accessing response properties
- [fCompletionStatus](./fcompletionstatus.md)
  The status of the task at completion of the call, such as good, busy, or timeout.
- [fServiceResponse](./fserviceresponse.md)
  The response from the service, such as complete, in process, or rejected.
- [fSenseDataValid](./fsensedatavalid.md)
  A Boolean value that indicates whether the sense data that the kernel provides is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsideviceinparameters/frealizedbytecountoftransfer)*