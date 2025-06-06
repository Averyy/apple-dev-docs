# Getting the Default GPU

**Framework**: Metal

Select the system’s default GPU device on which to run your Metal code.

#### Overview

To use the Metal framework, start by getting a GPU device. All of the objects your app needs to interact with Metal come from a [`MTLDevice`](mtldevice.md) that you acquire at runtime. Some devices, such as those with iOS and tvOS have a single GPU that you can access by calling [`MTLCreateSystemDefaultDevice()`](mtlcreatesystemdefaultdevice().md).

```swift
if(!(device = MTLCreateSystemDefaultDevice()))
{
    NSLog(@"Failed to get the system's default Metal device.");
}
```

On macOS devices that have multiple GPUs, such as a MacBook Pro, the system default is the discrete GPU.

## See Also

- [Detecting GPU Features and Metal Software Versions](detecting-gpu-features-and-metal-software-versions.md)
  Use the device object’s properties to determine how you perform tasks in Metal.
- [func MTLCreateSystemDefaultDevice() -> (any MTLDevice)?](mtlcreatesystemdefaultdevice().md)
  Returns the device instance Metal selects as the default.
- [protocol MTLDevice](mtldevice.md)
  The main Metal interface to a GPU that apps use to draw graphics and run computations in parallel.
- [Multi-GPU Systems](multi-gpu-systems.md)
  Locate and work with internal and external GPUs and their displays, video memory, and performance tradeoffs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/getting-the-default-gpu)*