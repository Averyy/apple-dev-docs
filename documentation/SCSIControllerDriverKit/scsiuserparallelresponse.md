# SCSIUserParallelResponse

**Framework**: SCSIControllerDriverKit  
**Kind**: struct

The properties of a completed request.

**Availability**:
- DriverKit ?+

## Declaration

```swift
typedef struct SCSIUserParallelResponse { ... } SCSIUserParallelResponse;
```

## Topics

### Response Properties
- [version](scsiuserparallelresponse/version.md)
  The version of the parallel response structure currently in use.
- [SCSIUserParallelResponseVersion](scsiuserparallelresponseversion.md)
  Constants that represent versions of the user parallel task structure.
- [fTargetID](scsiuserparallelresponse/ftargetid.md)
  An identifier that represents a SCSI target device.
- [fSCSIParallelFeatureResult](scsiuserparallelresponse/fscsiparallelfeatureresult.md)
  An array of features the system successfully negotiated with the SCSI parallel interface.
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

## See Also

- [UserProcessParallelTask](iouserscsiparallelinterfacecontroller/userprocessparalleltask.md)
  Processes a parallel task in response to a call from the framework.
- [SCSIUserParallelTask](scsiuserparalleltask.md)
  The properties of a parallel task to perform.
- [ParallelTaskCompletion](iouserscsiparallelinterfacecontroller/paralleltaskcompletion.md)
  Indicates to the system that the extension has completed an asynchronous request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/scsiuserparallelresponse)*