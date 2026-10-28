# UserMapBundledParallelTaskCommandAndResponseBuffers

**Framework**: SCSIControllerDriverKit  
**Kind**: method  
**Role**: Instance Method

Maps the shared command and response buffers in the dext address space in response to a call from the framework.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t UserMapBundledParallelTaskCommandAndResponseBuffers(IOBufferMemoryDescriptor *parallelCommandIOMemoryDescriptor, IOBufferMemoryDescriptor *parallelResponseIOMemoryDescriptor);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success and [`kIOReturnError`](../../DriverKit/kioreturnerror.md) on failure.

## Discussion

To optimize the interaction with the DriverKit Extension (dext) class, SCSIControllerDriverKit allocates contiguous command and response buffers to hold the maximum number of tasks reported by [`UserReportMaximumTaskCount`](./userreportmaximumtaskcount.md). The framework calls this method before [`UserStartController`](./userstartcontroller.md), so the dext class can map these buffers in the dext address space. The framework uses the shared buffers to pass command and response payloads. The command and response buffers use a one-to-one mapping; use the same slot number for related command and response payloads. For example, if the framework assigns buffer slot number 12 to a command, use slot number 12 in the mapped response buffers during I/O completion.

The framework owns the shared buffer slots for both command and responses until it passes ownership to the dext in the [`UserProcessBundledParallelTasks`](./userprocessbundledparalleltasks.md) call. From that point, the dext has ownership of these buffer slots until it returns ownership back to the framework in [`BundledParallelTaskCompletion`](./bundledparalleltaskcompletion.md). Don’t access a command or response buffer slot until the framework passes ownership to your dext.

If you don’t want to use the shared buffers, your dext can return [`kIOReturnError`](../../DriverKit/kioreturnerror.md) and continue to use [`UserProcessParallelTask`](./userprocessparalleltask.md) and `UserCompleteParallelTask` to process the I/O. If you return [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) from this method, the framework expects your dext to use [`UserProcessBundledParallelTasks`](./userprocessbundledparalleltasks.md) and `UserCompleteBundledParallelTask`.

## Parameters

- `parallelCommandIOMemoryDescriptor`: The memory descriptor corresponding to the command buffers.
- `parallelResponseIOMemoryDescriptor`: The memory descriptor corresponding to the response buffers.

## See Also

### Managing bundled parallel tasks
- [UserProcessBundledParallelTasks](./userprocessbundledparalleltasks.md)
  Processes one or more parallel tasks in response to a call from the framework.
- [BundledParallelTaskCompletion](./bundledparalleltaskcompletion.md)
  Indicates to the system that the extension completed a bundled asynchronous request.
- [kMaxBundledParallelTasks](../kmaxbundledparalleltasks.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/usermapbundledparalleltaskcommandandresponsebuffers)*