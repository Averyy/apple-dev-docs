# fBufferDirection

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: property  
**Role**: Instance Property

The direction for the buffer to send or receive data.

**Availability**:
- DriverKit 22.0+

## Declaration

```c
uint8_t fBufferDirection;
```

#### Discussion

Use the following `DriverKit/IOMemoryDescriptor.h` direction values to populate this field:

- [`kIOMemoryDirectionNone`](../../kernel/api-3852596-anonymous/kiomemorydirectionnone.md)
- [`kIOMemoryDirectionIn`](../../kernel/api-3852596-anonymous/kiomemorydirectionin.md)
- [`kIOMemoryDirectionOut`](../../kernel/api-3852596-anonymous/kiomemorydirectionout.md)
- [`kIOMemoryDirectionOutIn`](../../kernel/api-3852596-anonymous/kiomemorydirectionoutin.md)
- [`kIOMemoryDirectionInOut`](../../kernel/api-3852596-anonymous/kiomemorydirectioninout.md)
- [`kIOMemoryDisableCopyOnWrite`](../../kernel/api-3852596-anonymous/kiomemorydisablecopyonwrite.md)

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
- [fDataTransferDirection](./fdatatransferdirection.md)
  The direction for the caller to send data to or receive data from the device.
- [fSenseLengthRequested](./fsenselengthrequested.md)
  The length of sense data to read, in bytes.
- [fDataBufferAddr](./fdatabufferaddr.md)
  The virtual address of the buffer the dext creates to transfer data.
- [fSenseBufferAddr](./fsensebufferaddr.md)
  The virtual address of the buffer that the dext creates to transfer sense data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsideviceoutparameters/fbufferdirection)*