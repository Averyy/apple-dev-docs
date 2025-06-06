# fDataBufferAddr

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: property

The virtual address of the buffer the dext creates to transfer data.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
uint64_t fDataBufferAddr;
```

#### Discussion

The framework uses this address to create an [`IOMemoryDescriptor`](https://developer.apple.com/documentation/DriverKit/IOMemoryDescriptor) in the kernel that [`fRequestedByteCountOfTransfer`](scsideviceoutparameters/frequestedbytecountoftransfer.md) specifies and maps to the dext process.

## See Also

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
- [fSenseBufferAddr](scsideviceoutparameters/fsensebufferaddr.md)
  The virtual address of the buffer that the dext creates to transfer sense data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsideviceoutparameters/fdatabufferaddr)*