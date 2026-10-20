# fTargetID

**Framework**: SCSIControllerDriverKit  
**Kind**: property  
**Role**: Instance Property

An identifier that represents a SCSI target device.

**Availability**:
- DriverKit

## Declaration

```c
SCSITargetIdentifier fTargetID;
```

## See Also

### Response properties
- [version](./version.md)
  The version of the parallel response structure currently in use.
- [SCSIUserParallelResponseVersion](../scsiuserparallelresponseversion.md)
  Constants that represent versions of the user parallel task structure.
- [fSCSIParallelFeatureResult](./fscsiparallelfeatureresult.md)
  An array of features the system successfully negotiated with the SCSI parallel interface.
- [SCSIParallelFeatureResult](../scsiparallelfeatureresult.md)
  An enumeration of feature negotiation results.
- [fSCSIParallelFeatureRequestResultCount](./fscsiparallelfeaturerequestresultcount.md)
  The number of negotiated features.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/scsiuserparallelresponse/ftargetid)*