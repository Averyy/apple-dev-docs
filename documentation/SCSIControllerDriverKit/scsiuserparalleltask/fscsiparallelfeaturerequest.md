# fSCSIParallelFeatureRequest

**Framework**: SCSIControllerDriverKit  
**Kind**: property

An array of features of the SCSI parallel interface to negotiate.

**Availability**:
- DriverKit ?+

## Declaration

```swift
uint32_t fSCSIParallelFeatureRequest[5];
```

## See Also

- [version](scsiuserparalleltask/version.md)
  The version of the parallel task structure currently in use.
- [SCSIUserParallelTaskVersion](scsiuserparalleltaskversion.md)
  Constants that represent versions of the user parallel task structure.
- [fTargetID](scsiuserparalleltask/ftargetid.md)
  An identifier that represents a SCSI target device.
- [SCSIParallelFeatureRequest](scsiparallelfeaturerequest.md)
  An enumeration of feature negotiation behaviors.
- [fSCSIParallelFeatureRequestCount](scsiuserparalleltask/fscsiparallelfeaturerequestcount.md)
  The number of features to negotiate.
- [fControllerTaskIdentifier](scsiuserparalleltask/fcontrollertaskidentifier.md)
  A unique identifier for a task.
- [fRequestedTransferCount](scsiuserparalleltask/frequestedtransfercount.md)
  The requested data transfer count for the request’s data.
- [fBufferIOVMAddr](scsiuserparalleltask/fbufferiovmaddr.md)
  The start address of the generated physical segment of the data buffer.
- [fTaskAttribute](scsiuserparalleltask/ftaskattribute.md)
  The SCSI task attribute of the task.
- [fTaskTagIdentifier](scsiuserparalleltask/ftasktagidentifier.md)
  A 64-bit number that represents a unique task identifier.
- [fLogicalUnitBytes](scsiuserparalleltask/flogicalunitbytes.md)
  The request’s logical unit bytes.
- [fCommandDescriptorBlock](scsiuserparalleltask/fcommanddescriptorblock.md)
  The task’s SCSI command descriptor block.
- [fCommandSize](scsiuserparalleltask/fcommandsize.md)
  The size of the SCSI command descriptor block in bytes.
- [fTransferDirection](scsiuserparalleltask/ftransferdirection.md)
  The direction of data transfer for this task.
- [reserved](scsiuserparalleltask/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/scsiuserparalleltask/fscsiparallelfeaturerequest)*