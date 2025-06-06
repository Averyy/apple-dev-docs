# READ_CAPACITY

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: func

Fills a Command Descriptor Block (CDB) to perform a SCSI read-capacity command.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
bool READ_CAPACITY(SCSIDeviceOutParameters * request, UInt64 bufAddr, SCSIDeviceInParameters * response, UInt64 senseBufAddr);
```

#### Return Value

`true` if the call successfully fills the CDB; `false`, otherwise.

#### Discussion

Use this method in your dext to prefill a 16-byte CDB for the standard `READ CAPACITY` SCSI command.

## Parameters

- `request`: An object that contains the request information.
- `bufAddr`: A buffer to receive the data.
- `response`: An empty   object. On return, the framework populates this object with the response information.
- `senseBufAddr`: The address of the sense buffer.

## See Also

- [TEST_UNIT_READY](test_unit_ready.md)
  Fills a Command Descriptor Block (CDB) to test whether the unit is ready.
- [INQUIRY](inquiry.md)
  Fills a Command Descriptor Block (CDB) to perform a SCSI inquiry.
- [REQUEST_SENSE](request_sense.md)
  Fills a Command Descriptor Block (CDB) to perform a SCSI sense-request command.
- [READ_10](read_10.md)
  Fills a Command Descriptor Block (CDB) to perform a SCSI read command.
- [WRITE_10](write_10.md)
  Fills a Command Descriptor Block (CDB) to perform a SCSI write command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/read_capacity)*