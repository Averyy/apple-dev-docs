# BundledParallelTaskCompletion

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Indicates to the system that the extension completed a bundled asynchronous request.

**Availability**:
- DriverKit ?+

## Declaration

```swift
void BundledParallelTaskCompletion(OSAction * action, const uint16_t parallelResponseSlotIndices[32], uint16_t parallelResponseSlotIndicesCount);
```

#### Discussion

Use this method to complete one or more requests previously received by the [`UserProcessBundledParallelTasks`](iouserscsiparallelinterfacecontroller/userprocessbundledparalleltasks.md) method. For each request to complete:

1. Populate a [`SCSIUserParallelResponse`](scsiuserparallelresponse.md).
2. Make the response available in the shared response buffers.
3. Pass the response buffer slot in `parallelResponseSlotIndices`.

The command and response buffers have a one-to-one mapping; use the same slot number for related command and response payloads.

## Parameters

- `action`: A pointer to the   object of the asynchronous request that the system specifies in a   call.
- `parallelResponseSlotIndices`: The indices of the shared response buffer slots containing a   for each task to complete.
- `parallelResponseSlotIndicesCount`: The number of tasks to complete. Ensure that entries from zero to   have valid indicies.

## See Also

- [UserProcessBundledParallelTasks](iouserscsiparallelinterfacecontroller/userprocessbundledparalleltasks.md)
  Processes one or more parallel tasks in response to a call from the framework.
- [UserMapBundledParallelTaskCommandAndResponseBuffers](iouserscsiparallelinterfacecontroller/usermapbundledparalleltaskcommandandresponsebuffers.md)
  Maps the shared command and response buffers in the dext address space in response to a call from the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/bundledparalleltaskcompletion)*