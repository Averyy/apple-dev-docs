# UserProcessParallelTask

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Processes a parallel task in response to a call from the framework.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t UserProcessParallelTask(SCSIUserParallelTask parallelRequest, uint32_t * response, OSAction * completion);
```

#### Discussion

The system calls this method to put a command on the bus, sending all information necessary to process the request in the `parallelRequest` parameter. Your HBA-specific subclass must implement this method.

The following example shows a minimal implementation of [`UserProcessParallelTask`](iouserscsiparallelinterfacecontroller/userprocessparalleltask.md):

1. The example starts by using the `parallelRequest` parameter’s [`fControllerTaskIdentifier`](scsiuserparalleltask/fcontrollertaskidentifier.md) to look up task data, which it stores in a hypothetical convenience type called `TaskData`.
2. Next, it sets the metadata for this I/O operation. The kernel generates one long phsyical segment with [`fBufferIOVMAddr`](scsiuserparalleltask/fbufferiovmaddr.md) as its start address, as seen here in the call to a hypothetical `PrepareScatterGatherList()` function. You may need to prepare a custom scatter gather list if your hardware specification requires you to split this up into multiple segments.
3. After that, the example retains and stashes  the `completion` callback for later.
4. Finally, the code posts the request to the hardware by calling `PostSCSIRequest()`, another hypothetical convenience function. Assuming this call returns [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess), the example sets the `response` in-out parameter to [`kSCSIServiceResponse_Request_In_Process`](https://developer.apple.com/documentation/DriverKit/SCSIServiceResponse/kSCSIServiceResponse_Request_In_Process), to indicate to the kernel that the request is underway.

```objc
kern_return_t
IMPL ( ExampleSCSIDext, UserProcessParallelTask )
{
    kern_return_t     ret          = kIOReturnError;
    TaskData *        taskData     = NULL;

    taskData = ivars->fTaskArray[parallelRequest.fControllerTaskIdentifier];

    // Set all the metadata for this IO.
    taskData->fRequestedTransferCount = parallelRequest.fRequestedTransferCount;
    taskData->fTransferDirection = parallelRequest.fTransferDirection;
    PrepareScatterGatherList ( taskData, parallelRequest.fBufferIOVMAddr );
    …

    // Retain and stash the completion callback.
    completion->retain ( );
    taskData->fAction = completion;
    
    // Submit the request to the hardware.
    ret = PostSCSIRequest ( taskData );
    __Require ( ( kIOReturnSuccess == ret ), Exit );

    // Set the response and return.
    *response = kSCSIServiceResponse_Request_In_Process;

    return ret;
}
```

## Parameters

- `parallelRequest`: A   object that contains all necessary request information.
- `response`: A service response for the request.
- `completion`: An   object that the dext class uses to complete the request.

## See Also

- [SCSIUserParallelTask](scsiuserparalleltask.md)
  The properties of a parallel task to perform.
- [ParallelTaskCompletion](iouserscsiparallelinterfacecontroller/paralleltaskcompletion.md)
  Indicates to the system that the extension has completed an asynchronous request.
- [SCSIUserParallelResponse](scsiuserparallelresponse.md)
  The properties of a completed request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/userprocessparalleltask)*