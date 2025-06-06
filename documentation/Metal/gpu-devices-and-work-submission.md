# GPU Devices and Work Submission

**Framework**: Metal

Find any available GPU, submit work to it with command buffers, suspend work, and coordinate between multiple GPUs.

#### Overview

You can use any available GPU’s [`MTLDevice`](mtldevice.md) instance in addition to the default instance that [`MTLCreateSystemDefaultDevice()`](mtlcreatesystemdefaultdevice().md) returns. For each device instance, get its [`MTLCommandQueue`](mtlcommandqueue.md) instance, and create one or more [`MTLCommandBuffer`](mtlcommandbuffer.md) instances to send work to the GPU.

When the system suspends your app, use the command queue to finish command buffers already in progress. See [`Preparing Your Metal App to Run in the Background`](preparing-your-metal-app-to-run-in-the-background.md) for more information.

## Topics

### Locating and Inspecting a GPU Device
- [Getting the Default GPU](getting-the-default-gpu.md)
  Select the system’s default GPU device on which to run your Metal code.
- [Detecting GPU Features and Metal Software Versions](detecting-gpu-features-and-metal-software-versions.md)
  Use the device object’s properties to determine how you perform tasks in Metal.
- [func MTLCreateSystemDefaultDevice() -> (any MTLDevice)?](mtlcreatesystemdefaultdevice().md)
  Returns the device instance Metal selects as the default.
- [protocol MTLDevice](mtldevice.md)
  The main Metal interface to a GPU that apps use to draw graphics and run computations in parallel.
- [Multi-GPU Systems](multi-gpu-systems.md)
  Locate and work with internal and external GPUs and their displays, video memory, and performance tradeoffs.
### Submitting Work to a GPU
- [Setting Up a Command Structure](setting-up-a-command-structure.md)
  Discover how Metal executes commands on a GPU.
- [protocol MTLCommandQueue](mtlcommandqueue.md)
  An instance you use to create, submit, and schedule command buffers to a specific GPU device to run the commands within those buffers.
- [class MTLCommandQueueDescriptor](mtlcommandqueuedescriptor.md)
  A configuration that customizes the behavior for a new command queue.
- [protocol MTLCommandBuffer](mtlcommandbuffer.md)
  A container that stores a sequence of GPU commands that you encode into it.
- [class MTLCommandBufferDescriptor](mtlcommandbufferdescriptor.md)
  A configuration that customizes the behavior for a new command buffer.
- [struct MTLCommandBufferError](mtlcommandbuffererror-swift.struct.md)
  The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.
- [protocol MTLCommandEncoder](mtlcommandencoder.md)
  An encoder that writes GPU commands into a command buffer.
### Suspending Work on a GPU
- [Preparing Your Metal App to Run in the Background](preparing-your-metal-app-to-run-in-the-background.md)
  Prepare your app to move into the background by pausing future GPU use and ensuring previous work is scheduled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/gpu-devices-and-work-submission)*