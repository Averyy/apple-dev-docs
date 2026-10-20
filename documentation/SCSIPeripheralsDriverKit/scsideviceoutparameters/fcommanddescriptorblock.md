# fCommandDescriptorBlock

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: property  
**Role**: Instance Property

A 16-byte opcode to fill out the Command Descriptor Block (CDB).

**Availability**:
- DriverKit 22.0+

## Declaration

```c
SCSICommandDescriptorBlock fCommandDescriptorBlock;
```

#### Discussion

Populate this member of the parameters structure with the functions listed in the following sections:

- Creating common SCSI commands
- Creating Self-Monitoring, Analysis and Reporting Technology (SMART) Commands
- Creating arbitrary SCSI commands

## See Also

### Setting command parameters
- [fLogicalUnitNumber](./flogicalunitnumber.md)
  The SCSI logical unit number of the device that receives the command.
- [fTimeoutDuration](./ftimeoutduration.md)
  A timeout for the command, in milliseconds.
- [fRequestedByteCountOfTransfer](./frequestedbytecountoftransfer.md)
  The size of the data to transfer.
- [fBufferDirection](./fbufferdirection.md)
  The direction for the buffer to send or receive data.
- [fDataTransferDirection](./fdatatransferdirection.md)
  The direction for the caller to send data to or receive data from the device.
- [fSenseLengthRequested](./fsenselengthrequested.md)
  The length of sense data to read, in bytes.
- [fDataBufferAddr](./fdatabufferaddr.md)
  The virtual address of the buffer the dext creates to transfer data.
- [fSenseBufferAddr](./fsensebufferaddr.md)
  The virtual address of the buffer that the dext creates to transfer sense data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsideviceoutparameters/fcommanddescriptorblock)*