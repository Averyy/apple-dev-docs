# UserProcessBundledParallelTasks

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Processes one or more parallel tasks in response to a call from the framework.

**Availability**:
- DriverKit ?+

## Declaration

```swift
void UserProcessBundledParallelTasks(const uint16_t parallelRequestSlotIndices[32], uint16_t parallelRequestSlotIndicesCount, OSAction * completion);
```

#### Discussion

The system calls this method to put one or more commands on the bus. The framework populates a [`SCSIUserParallelTask`](scsiuserparalleltask.md) for each task and makes it available in the command buffers. Access these command buffers with the indices passed in the `parallelRequestSlotIndices` parameter.

If the dext can’t process any commands, invoke [`BundledParallelTaskCompletion`](iouserscsiparallelinterfacecontroller/bundledparalleltaskcompletion.md) for those commands. The framework completes those commands with the response provided by the dext.

The framework only calls this method when the dext has successfully mapped command and response buffers in the dext address space in [`UserMapBundledParallelTaskCommandAndResponseBuffers`](iouserscsiparallelinterfacecontroller/usermapbundledparalleltaskcommandandresponsebuffers.md).

## Parameters

- `parallelRequestSlotIndices`: Indices of shared command buffer slots for   the tasks to process. Entries from zero to    have valid indices.
- `parallelRequestSlotIndicesCount`: The number of tasks to process.
- `completion`: An   object that the dext class uses to complete the request.

## See Also

- [UserMapBundledParallelTaskCommandAndResponseBuffers](iouserscsiparallelinterfacecontroller/usermapbundledparalleltaskcommandandresponsebuffers.md)
  Maps the shared command and response buffers in the dext address space in response to a call from the framework.
- [BundledParallelTaskCompletion](iouserscsiparallelinterfacecontroller/bundledparalleltaskcompletion.md)
  Indicates to the system that the extension completed a bundled asynchronous request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/userprocessbundledparalleltasks)*