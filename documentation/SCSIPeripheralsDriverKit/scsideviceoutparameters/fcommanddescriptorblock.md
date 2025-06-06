# fCommandDescriptorBlock

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: property

A 16-byte opcode to fill out the Command Descriptor Block (CDB).

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
SCSICommandDescriptorBlock fCommandDescriptorBlock;
```

#### Discussion

Populate this member of the parameters structure with the functions listed in the following sections:

- Creating common SCSI commands
- Creating Self-Monitoring, Analysis and Reporting Technology (SMART) Commands
- Creating arbitrary SCSI commands

## See Also

- [fLogicalUnitNumber](scsideviceoutparameters/flogicalunitnumber.md)
  The SCSI logical unit number of the device that receives the command.
- [fTimeoutDuration](scsideviceoutparameters/ftimeoutduration.md)
  A timeout for the command, in milliseconds.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsideviceoutparameters/fcommanddescriptorblock)*