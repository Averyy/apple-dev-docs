# fDataTransferDirection

**Framework**: SCSIPeripheralsDriverKit  
**Kind**: property

The direction for the caller to send data to or receive data from the device.

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
uint8_t fDataTransferDirection;
```

#### Discussion

Use the following `DriverKit/storage/SCSITask.h` direction values to populate this field:

- [`kSCSIDataTransfer_NoDataTransfer`](https://developer.apple.com/documentation/driverkit/3583340-anonymous/kscsidatatransfer_nodatatransfer)
- [`kSCSIDataTransfer_FromInitiatorToTarget`](https://developer.apple.com/documentation/driverkit/3583340-anonymous/kscsidatatransfer_frominitiatortotarget)
- [`kSCSIDataTransfer_FromTargetToInitiator`](https://developer.apple.com/documentation/driverkit/3583340-anonymous/kscsidatatransfer_fromtargettoinitiator)

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
- [fSenseLengthRequested](scsideviceoutparameters/fsenselengthrequested.md)
  The length of sense data to read, in bytes.
- [fDataBufferAddr](scsideviceoutparameters/fdatabufferaddr.md)
  The virtual address of the buffer the dext creates to transfer data.
- [fSenseBufferAddr](scsideviceoutparameters/fsensebufferaddr.md)
  The virtual address of the buffer that the dext creates to transfer sense data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsideviceoutparameters/fdatatransferdirection)*