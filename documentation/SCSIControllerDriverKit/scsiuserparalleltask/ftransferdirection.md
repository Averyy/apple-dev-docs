# fTransferDirection

**Framework**: SCSIControllerDriverKit  
**Kind**: property  
**Role**: Instance Property

The direction of data transfer for this task.

**Availability**:
- DriverKit

## Declaration

```c
uint8_t fTransferDirection;
```

#### Discussion

Use the constants in [`Data Transfer Direction`](../../iokit/api-1534749-data_transfer_direction.md) for this value.

## See Also

### Task properties
- [version](./version.md)
  The version of the parallel task structure currently in use.
- [SCSIUserParallelTaskVersion](../scsiuserparalleltaskversion.md)
  Constants that represent versions of the user parallel task structure.
- [fTargetID](./ftargetid.md)
  An identifier that represents a SCSI target device.
- [fSCSIParallelFeatureRequest](./fscsiparallelfeaturerequest.md)
  An array of features of the SCSI parallel interface to negotiate.
- [SCSIParallelFeatureRequest](../scsiparallelfeaturerequest.md)
  An enumeration of feature negotiation behaviors.
- [fSCSIParallelFeatureRequestCount](./fscsiparallelfeaturerequestcount.md)
  The number of features to negotiate.
- [fControllerTaskIdentifier](./fcontrollertaskidentifier.md)
  A unique identifier for a task.
- [fRequestedTransferCount](./frequestedtransfercount.md)
  The requested data transfer count for the request’s data.
- [fBufferIOVMAddr](./fbufferiovmaddr.md)
  The start address of the generated physical segment of the data buffer.
- [fTaskAttribute](./ftaskattribute.md)
  The SCSI task attribute of the task.
- [fTaskTagIdentifier](./ftasktagidentifier.md)
  A 64-bit number that represents a unique task identifier.
- [fLogicalUnitBytes](./flogicalunitbytes.md)
  The request’s logical unit bytes.
- [fCommandDescriptorBlock](./fcommanddescriptorblock.md)
  The task’s SCSI command descriptor block.
- [fCommandSize](./fcommandsize.md)
  The size of the SCSI command descriptor block in bytes.
- [reserved](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/scsiuserparalleltask/ftransferdirection)*