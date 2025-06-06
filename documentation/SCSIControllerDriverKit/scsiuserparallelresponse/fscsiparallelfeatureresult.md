# fSCSIParallelFeatureResult

**Framework**: SCSIControllerDriverKit  
**Kind**: property

An array of features the system successfully negotiated with the SCSI parallel interface.

**Availability**:
- DriverKit ?+

## Declaration

```swift
uint32_t fSCSIParallelFeatureResult[5];
```

## See Also

- [version](scsiuserparallelresponse/version.md)
  The version of the parallel response structure currently in use.
- [SCSIUserParallelResponseVersion](scsiuserparallelresponseversion.md)
  Constants that represent versions of the user parallel task structure.
- [fTargetID](scsiuserparallelresponse/ftargetid.md)
  An identifier that represents a SCSI target device.
- [SCSIParallelFeatureResult](scsiparallelfeatureresult.md)
  An enumeration of feature negotiation results.
- [fSCSIParallelFeatureRequestResultCount](scsiuserparallelresponse/fscsiparallelfeaturerequestresultcount.md)
  The number of negotiated features.
- [fControllerTaskIdentifier](scsiuserparallelresponse/fcontrollertaskidentifier.md)
  A unique identifier for a task.
- [fCompletionStatus](scsiuserparallelresponse/fcompletionstatus.md)
  The status of the task after the host bus adapter (HBA) completes processing.
- [fServiceResponse](scsiuserparallelresponse/fserviceresponse.md)
  Attributes of the task service response.
- [fBytesTransferred](scsiuserparallelresponse/fbytestransferred.md)
  The total number of bytes the system transferred as part of the I/O with the interface.
- [fSenseBuffer](scsiuserparallelresponse/fsensebuffer.md)
  The SCSI sense data buffer.
- [fSenseLength](scsiuserparallelresponse/fsenselength.md)
  The length of the sense buffer, if any.
- [kMaxSenseBufferSize](kmaxsensebuffersize.md)
  The maximum size of the SCSI sense data buffer in a response.
- [reserved](scsiuserparallelresponse/reserved.md)
  An unused field reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/scsiuserparallelresponse/fscsiparallelfeatureresult)*