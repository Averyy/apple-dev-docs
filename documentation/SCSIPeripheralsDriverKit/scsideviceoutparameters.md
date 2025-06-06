# SCSIDeviceOutParameters

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: struct

A structure that contains parameters for an outbound request to a SCSI device.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
typedef struct SCSIDeviceOutParameters { ... } SCSIDeviceOutParameters;
```

## Topics

### Setting command parameters
- [fLogicalUnitNumber](scsideviceoutparameters/flogicalunitnumber.md)
  The SCSI logical unit number of the device that receives the command.
- [fTimeoutDuration](scsideviceoutparameters/ftimeoutduration.md)
  A timeout for the command, in milliseconds.
- [fCommandDescriptorBlock](scsideviceoutparameters/fcommanddescriptorblock.md)
  A 16-byte opcode to fill out the Command Descriptor Block (CDB).
- [fRequestedByteCountOfTransfer](scsideviceoutparameters/frequestedbytecountoftransfer.md)
  The size of the data to transfer.
- [fBufferDirection](scsideviceoutparameters/fbufferdirection.md)
  The direction for the buffer to send or receive data.
- [fDataTransferDirection](scsideviceoutparameters/fdatatransferdirection.md)
  The direction for the caller to send data to or receive data from the device.
- [fSenseLengthRequested](scsideviceoutparameters/fsenselengthrequested.md)
  The length of sense data to read, in bytes.
- [fDataBufferAddr](scsideviceoutparameters/fdatabufferaddr.md)
  The virtual address of the buffer the dext creates to transfer data.
- [fSenseBufferAddr](scsideviceoutparameters/fsensebufferaddr.md)
  The virtual address of the buffer that the dext creates to transfer sense data.
### Infrequently Used Functionality
- [reserved](scsideviceoutparameters/reserved.md)
  An unused field reserved for future use.

## Relationships

### Inherited By
- [SCSIType00OutParameters](scsitype00outparameters.md)
- [SCSIType05OutParameters](scsitype05outparameters.md)
- [SCSIType07OutParameters](scsitype07outparameters.md)

## See Also

- [SCSIDeviceInParameters](scsideviceinparameters.md)
  A structure that contains properties from an inbound response from a SCSI device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsideviceoutparameters)*