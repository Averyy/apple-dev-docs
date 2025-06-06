# UserMapBundledParallelTaskCommandAndResponseBuffers

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Maps the shared command and response buffers in the dext address space in response to a call from the framework.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t UserMapBundledParallelTaskCommandAndResponseBuffers(IOBufferMemoryDescriptor * parallelCommandIOMemoryDescriptor, IOBufferMemoryDescriptor * parallelResponseIOMemoryDescriptor);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success and [`kIOReturnError`](https://developer.apple.com/documentation/DriverKit/kIOReturnError) on failure.

#### Discussion

To optimize the interaction with the DriverKit Extension (dext) class, SCSIControllerDriverKit allocates contiguous command and response buffers to hold the maximum number of tasks reported by [`UserReportMaximumTaskCount`](iouserscsiparallelinterfacecontroller/userreportmaximumtaskcount.md). The framework calls this method before [`UserStartController`](iouserscsiparallelinterfacecontroller/userstartcontroller.md), so the dext class can map these buffers in the dext address space. The framework uses the shared buffers to pass command and response payloads. The command and response buffers use a one-to-one mapping; use the same slot number for related command and response payloads. For example, if the framework assigns buffer slot number 12 to a command, use slot number 12 in the mapped response buffers during I/O completion.

The framework owns the shared buffer slots for both command and responses until it passes ownership to the dext in the [`UserProcessBundledParallelTasks`](iouserscsiparallelinterfacecontroller/userprocessbundledparalleltasks.md) call. From that point, the dext has ownership of these buffer slots until it returns ownership back to the framework in [`BundledParallelTaskCompletion`](iouserscsiparallelinterfacecontroller/bundledparalleltaskcompletion.md). Don’t access a command or response buffer slot until the framework passes ownership to your dext.

If you don’t want to use the shared buffers, your dext can return [`kIOReturnError`](https://developer.apple.com/documentation/DriverKit/kIOReturnError) and continue to use [`UserProcessParallelTask`](iouserscsiparallelinterfacecontroller/userprocessparalleltask.md) and `UserCompleteParallelTask` to process the I/O. If you return [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) from this method, the framework expects your dext to use [`UserProcessBundledParallelTasks`](iouserscsiparallelinterfacecontroller/userprocessbundledparalleltasks.md) and `UserCompleteBundledParallelTask`.

## Parameters

- `parallelCommandIOMemoryDescriptor`: The memory descriptor corresponding   to the command buffers.
- `parallelResponseIOMemoryDescriptor`: The memory descriptor corresponding   to the response buffers.

## See Also

- [UserProcessBundledParallelTasks](iouserscsiparallelinterfacecontroller/userprocessbundledparalleltasks.md)
  Processes one or more parallel tasks in response to a call from the framework.
- [BundledParallelTaskCompletion](iouserscsiparallelinterfacecontroller/bundledparalleltaskcompletion.md)
  Indicates to the system that the extension completed a bundled asynchronous request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/usermapbundledparalleltaskcommandandresponsebuffers)*