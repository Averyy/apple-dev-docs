# TEST_UNIT_READY

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: func

Fills a Command Descriptor Block (CDB) to test whether the unit is ready.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
bool TEST_UNIT_READY(SCSIDeviceOutParameters * request, SCSIDeviceInParameters * response, UInt64 senseBufAddr);
```

#### Return Value

`true` if the call successfully fills the CDB; `false`, otherwise.

#### Discussion

Use this method in your dext to prefill a 16-byte CDB for the standard `TEST UNIT READY` SCSI command.

## Parameters

- `request`: An object that contains the request information.
- `response`: An empty   object. On return, the framework populates this object with the response information.
- `senseBufAddr`: The address of the sense buffer.

## See Also

- [INQUIRY](inquiry.md)
  Fills a Command Descriptor Block (CDB) to perform a SCSI inquiry.
- [REQUEST_SENSE](request_sense.md)
  Fills a Command Descriptor Block (CDB) to perform a SCSI sense-request command.
- [READ_10](read_10.md)
  Fills a Command Descriptor Block (CDB) to perform a SCSI read command.
- [WRITE_10](write_10.md)
  Fills a Command Descriptor Block (CDB) to perform a SCSI write command.
- [READ_CAPACITY](read_capacity.md)
  Fills a Command Descriptor Block (CDB) to perform a SCSI read-capacity command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/test_unit_ready)*