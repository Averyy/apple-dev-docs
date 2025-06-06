# fBufferDirection

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: property

The direction for the buffer to send or receive data.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
uint8_t fBufferDirection;
```

#### Discussion

Use the following `DriverKit/IOMemoryDescriptor.h` direction values to populate this field:

- [`kIOMemoryDirectionNone`](https://developer.apple.com/documentation/kernel/3852596-anonymous/kiomemorydirectionnone)
- [`kIOMemoryDirectionIn`](https://developer.apple.com/documentation/kernel/3852596-anonymous/kiomemorydirectionin)
- [`kIOMemoryDirectionOut`](https://developer.apple.com/documentation/kernel/3852596-anonymous/kiomemorydirectionout)
- [`kIOMemoryDirectionOutIn`](https://developer.apple.com/documentation/kernel/3852596-anonymous/kiomemorydirectionoutin)
- [`kIOMemoryDirectionInOut`](https://developer.apple.com/documentation/kernel/3852596-anonymous/kiomemorydirectioninout)
- [`kIOMemoryDisableCopyOnWrite`](https://developer.apple.com/documentation/kernel/3852596-anonymous/kiomemorydisablecopyonwrite)

## See Also

- [fLogicalUnitNumber](scsideviceoutparameters/flogicalunitnumber.md)
  The SCSI logical unit number of the device that receives the command.
- [fTimeoutDuration](scsideviceoutparameters/ftimeoutduration.md)
  A timeout for the command, in milliseconds.
- [fCommandDescriptorBlock](scsideviceoutparameters/fcommanddescriptorblock.md)
  A 16-byte opcode to fill out the Command Descriptor Block (CDB).
- [fRequestedByteCountOfTransfer](scsideviceoutparameters/frequestedbytecountoftransfer.md)
  The size of the data to transfer.
- [fDataTransferDirection](scsideviceoutparameters/fdatatransferdirection.md)
  The direction for the caller to send data to or receive data from the device.
- [fSenseLengthRequested](scsideviceoutparameters/fsenselengthrequested.md)
  The length of sense data to read, in bytes.
- [fDataBufferAddr](scsideviceoutparameters/fdatabufferaddr.md)
  The virtual address of the buffer the dext creates to transfer data.
- [fSenseBufferAddr](scsideviceoutparameters/fsensebufferaddr.md)
  The virtual address of the buffer that the dext creates to transfer sense data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsideviceoutparameters/fbufferdirection)*