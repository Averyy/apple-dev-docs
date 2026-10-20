# fSCSIParallelFeatureRequestResultCount

**Framework**: SCSIControllerDriverKit  
**Kind**: property  
**Role**: Instance Property

The number of negotiated features.

**Availability**:
- DriverKit

## Declaration

```c
uint64_t fSCSIParallelFeatureRequestResultCount;
```

#### Discussion

This value represents the number of items in the [`fSCSIParallelFeatureResult`](./fscsiparallelfeatureresult.md) array.

## See Also

### Response properties
- [version](./version.md)
  The version of the parallel response structure currently in use.
- [SCSIUserParallelResponseVersion](../scsiuserparallelresponseversion.md)
  Constants that represent versions of the user parallel task structure.
- [fTargetID](./ftargetid.md)
  An identifier that represents a SCSI target device.
- [fSCSIParallelFeatureResult](./fscsiparallelfeatureresult.md)
  An array of features the system successfully negotiated with the SCSI parallel interface.
- [SCSIParallelFeatureResult](../scsiparallelfeatureresult.md)
  An enumeration of feature negotiation results.
- [fControllerTaskIdentifier](./fcontrollertaskidentifier.md)
  A unique identifier for a task.
- [fCompletionStatus](./fcompletionstatus.md)
  The status of the task after the host bus adapter (HBA) completes processing.
- [fServiceResponse](./fserviceresponse.md)
  Attributes of the task service response.
- [fBytesTransferred](./fbytestransferred.md)
  The total number of bytes the system transferred as part of the I/O with the interface.
- [fSenseBuffer](./fsensebuffer.md)
  The SCSI sense data buffer.
- [fSenseLength](./fsenselength.md)
  The length of the sense buffer, if any.
- [kMaxSenseBufferSize](../kmaxsensebuffersize.md)
  The maximum size of the SCSI sense data buffer in a response.
- [reserved](./reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/scsiuserparallelresponse/fscsiparallelfeaturerequestresultcount)*