# Command Buffer Debugging

**Framework**: Metal

Properties and methods for programmatically debugging runtime issues with a command buffer.

## Topics

### Identifying the Command Buffer
- [var label: String?](mtlcommandbuffer/label.md)
  An optional name that can help you identify the command buffer.
- [var commandQueue: any MTLCommandQueue](mtlcommandbuffer/commandqueue.md)
  The command queue that creates the command buffer.
- [var device: any MTLDevice](mtlcommandbuffer/device.md)
  The GPU device that indirectly owns the command buffer because you create it from a command queue the device also owns.
### Grouping Commands within a GPU Frame Capture
- [func pushDebugGroup(String)](mtlcommandbuffer/pushdebuggroup(_:).md)
  Marks the beginning of a debug group and gives it an identifying label, which temporarily replaces the previous group, if applicable.
- [func popDebugGroup()](mtlcommandbuffer/popdebuggroup.md)
  Marks the end of a debug group and, if applicable, restores the previous group from a stack.
### Getting Error Details
- [var error: (any Error)?](mtlcommandbuffer/error.md)
  A description of an error when the GPU encounters an issue as it runs the command buffer.
- [var errorOptions: MTLCommandBufferErrorOption](mtlcommandbuffer/erroroptions.md)
  Settings that determine which information the command buffer records about execution errors, and how it does it.
- [protocol MTLCommandBufferEncoderInfo](mtlcommandbufferencoderinfo.md)
  A container that provides additional information about a runtime failure a GPU encounters as it runs the commands in a command buffer.
- [let MTLCommandBufferEncoderInfoErrorKey: String](mtlcommandbufferencoderinfoerrorkey.md)
  A key to a command buffer error’s user information dictionary that retrieves additional information about a GPU’s runtime error.
### Reading the Runtime Message Logs
- [var logs: MTLLogContainer](mtlcommandbuffer/logs-518l2.md)
  The messages the command buffer records as the GPU runs its commands.
### Checking Scheduling Times on the CPU
- [var kernelStartTime: CFTimeInterval](mtlcommandbuffer/kernelstarttime.md)
  The host time, in seconds, when the CPU begins to schedule the command buffer.
- [var kernelEndTime: CFTimeInterval](mtlcommandbuffer/kernelendtime.md)
  The host time, in seconds, when the CPU finishes scheduling the command buffer.
### Checking Execution Times on the GPU
- [var gpuStartTime: CFTimeInterval](mtlcommandbuffer/gpustarttime.md)
  The host time, in seconds, when the GPU starts command buffer execution.
- [var gpuEndTime: CFTimeInterval](mtlcommandbuffer/gpuendtime.md)
  The host time, in seconds, when the GPU finishes execution of the command buffer.
### Determining Whether to Maintain Strong References
- [var retainedReferences: Bool](mtlcommandbuffer/retainedreferences.md)
  A Boolean value that indicates whether the command buffer maintains strong references to the resources it uses.

## See Also

- [var status: MTLCommandBufferStatus](mtlcommandbuffer/status.md)
  The command buffer’s current state.
- [enum MTLCommandBufferStatus](mtlcommandbufferstatus.md)
  The discrete states for a command buffer that represent its life cycle stages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/command-buffer-debugging)*