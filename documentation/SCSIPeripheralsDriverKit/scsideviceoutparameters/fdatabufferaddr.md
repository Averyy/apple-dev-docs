# fDataBufferAddr

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: property  
**Role**: Instance Property

The virtual address of the buffer the dext creates to transfer data.

**Availability**:
- DriverKit 22.0+

## Declaration

```c
uint64_t fDataBufferAddr;
```

## Discussion

The framework uses this address to create an [`IOMemoryDescriptor`](../../DriverKit/iomemorydescriptor.md) in the kernel that [`fRequestedByteCountOfTransfer`](./frequestedbytecountoftransfer.md) specifies and maps to the dext process.

## See Also

### Setting command parameters
- [fLogicalUnitNumber](./flogicalunitnumber.md)
  The SCSI logical unit number of the device that receives the command.
- [fTimeoutDuration](./ftimeoutduration.md)
  A timeout for the command, in milliseconds.
- [fCommandDescriptorBlock](./fcommanddescriptorblock.md)
  A 16-byte opcode to fill out the Command Descriptor Block (CDB).
- [fRequestedByteCountOfTransfer](./frequestedbytecountoftransfer.md)
  The size of the data to transfer.
- [fBufferDirection](./fbufferdirection.md)
  The direction for the buffer to send or receive data.
- [fDataTransferDirection](./fdatatransferdirection.md)
  The direction for the caller to send data to or receive data from the device.
- [fSenseLengthRequested](./fsenselengthrequested.md)
  The length of sense data to read, in bytes.
- [fSenseBufferAddr](./fsensebufferaddr.md)
  The virtual address of the buffer that the dext creates to transfer sense data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsideviceoutparameters/fdatabufferaddr)*