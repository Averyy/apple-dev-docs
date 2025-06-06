# ParallelTaskCompletion

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Indicates to the system that the extension has completed an asynchronous request.

**Availability**:
- DriverKit ?+

## Declaration

```swift
void ParallelTaskCompletion(OSAction * action, SCSIUserParallelResponse response);
```

#### Discussion

Your driver extension class invokes this method to complete an asynchronous request.

## Parameters

- `action`: A pointer to the   object of the asynchronous request that the system specifies in a  .
- `response`: The result of the asychronous request.

## See Also

- [UserProcessParallelTask](iouserscsiparallelinterfacecontroller/userprocessparalleltask.md)
  Processes a parallel task in response to a call from the framework.
- [SCSIUserParallelTask](scsiuserparalleltask.md)
  The properties of a parallel task to perform.
- [SCSIUserParallelResponse](scsiuserparallelresponse.md)
  The properties of a completed request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/paralleltaskcompletion)*