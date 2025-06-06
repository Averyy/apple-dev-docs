# fSenseDataValid

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: property

A Boolean value that indicates whether the sense data that the kernel provides is valid.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
bool fSenseDataValid;
```

#### Discussion

The default value of this property is `false`.

## See Also

- [fCompletionStatus](scsideviceinparameters/fcompletionstatus.md)
  The status of the task at completion of the call, such as good, busy, or timeout.
- [fServiceResponse](scsideviceinparameters/fserviceresponse.md)
  The response from the service, such as complete, in process, or rejected.
- [fRealizedByteCountOfTransfer](scsideviceinparameters/frealizedbytecountoftransfer.md)
  The byte count of the tranferred data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsideviceinparameters/fsensedatavalid)*