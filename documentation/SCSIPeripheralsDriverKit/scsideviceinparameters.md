# SCSIDeviceInParameters

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: struct

A structure that contains properties from an inbound response from a SCSI device.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
typedef struct SCSIDeviceInParameters { ... } SCSIDeviceInParameters;
```

## Topics

### Accessing response properties
- [fCompletionStatus](scsideviceinparameters/fcompletionstatus.md)
  The status of the task at completion of the call, such as good, busy, or timeout.
- [fServiceResponse](scsideviceinparameters/fserviceresponse.md)
  The response from the service, such as complete, in process, or rejected.
- [fRealizedByteCountOfTransfer](scsideviceinparameters/frealizedbytecountoftransfer.md)
  The byte count of the tranferred data.
- [fSenseDataValid](scsideviceinparameters/fsensedatavalid.md)
  A Boolean value that indicates whether the sense data that the kernel provides is valid.
### Infrequently Used Functionality
- [reserved](scsideviceinparameters/reserved.md)
  An unused field reserved for future use.

## Relationships

### Inherited By
- [SCSIType00InParameters](scsitype00inparameters.md)
- [SCSIType05InParameters](scsitype05inparameters.md)
- [SCSIType07InParameters](scsitype07inparameters.md)

## See Also

- [SCSIDeviceOutParameters](scsideviceoutparameters.md)
  A structure that contains parameters for an outbound request to a SCSI device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsideviceinparameters)*