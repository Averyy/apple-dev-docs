# Reducing the memory footprint of Metal apps

**Framework**: Metal

Learn best practices for using memory efficiently in iOS and tvOS.

#### Overview

Efficient memory usage is a critical consideration for resource-intensive Metal apps in iOS and tvOS. Create apps so they use as little memory as possible, making more memory available for other apps and system services.

iOS and tvOS monitor your app’s total memory usage at runtime, and if the amount exceeds a predetermined limit, the system terminates your app. This limit varies by device model, so test your app on all supported devices.

##### Optimize Memory Usage in Your Metal App

Here are some tips to understand how your Metal app is using memory, and best practices to reduce memory usage.

 Build your app with the iOS or tvOS SDK, then use Xcode Memory Report to observe your app’s total memory footprint during execution. For more information about Xcode Memory Report, see [`Gathering information about memory use`](https://developer.apple.com/documentation/Xcode/gathering-information-about-memory-use).

- Take an [`Instruments`](https://developer.apple.comhttps://help.apple.com/instruments/mac/current/#//apple_ref/doc/uid/TP40004652-CH19-SW13) trace and look at the Metal Resource Allocations Instrument, which is part of the Metal System Trace template. For more information on working with the Metal Resource Allocations Instrument, see [`Delivering Optimized Metal Apps and Games`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2019/606/?time=1726).
- Capture a GPU trace with [`Metal debugger`](https://developer.apple.com/documentation/Xcode/Metal-debugger) and see a visual representation of all of a frame’s GPU resources and a table of properties for each resource with the Memory view. For detailed information about the Memory view, see [`Delivering Optimized Metal Apps and Games`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2019/606/?time=1665).
- Observe and take action on suggestions highlighted in the Memory insights section of the GPU trace summary. For more information on Memory insights, see [`Gain insights into your Metal app with Xcode 12`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020-10605/?time=620).
- Use the memory graph tool to help identify leaks and abandoned memory. For more information, see [`Memory Graph Debugging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/debugging_with_xcode/chapters/special_debugging_workflows.html#//apple_ref/doc/uid/TP40015022-CH9-DontLinkElementID_1).
- Query the amount of memory available to your app at runtime using the [`os_proc_available_memory`](https://developer.apple.com/documentation/os/os_proc_available_memory) API to help you identify memory spikes.

 Avoid loading a large resource when a smaller one works. Use compressed texture formats. Load lower-resolution textures when running on memory-constrained devices. Consider reducing the fidelity of 3D models and compressing per-vertex data.

 Some effects, like shadows or motion blur, require large offscreen buffers for temporary image data. Consider lowering the resolution of these image buffers or applying fewer effects when running on memory-constrained devices.

 Xcode can help you identify Metal objects that aren’t in use. Use Metal Debugger to get a GPU trace. Then navigate to the Memory view, and select the Unused filter.

 Use [`MTLPurgeableState.volatile`](mtlpurgeablestate/volatile.md) and [`setPurgeableState(_:)`](mtlresource/setpurgeablestate(_:).md) for textures and buffers the operating system can safely discard under low-memory conditions, and be subsequently recreated or reloaded by your app as needed. This design means your app keeps a cache of idle resources in memory but doesn’t count them toward the memory limit.

 [`MTLStorageMode.memoryless`](mtlstoragemode/memoryless.md) avoids allocating regular system memory, allowing apps to store the contents of temporary render targets directly in tile memory on the GPU.

 Using [`MTLHeap`](mtlheap.md), your app can have Multiple Metal resources backed by the same memory allocation. For example, use resource heaps when transient resources are produced and consumed for each frame but aren’t all used together. Those not used together share the same memory, backed by a heap.

##### Additional Resources

The WWDC video [`Gain insights into your Metal app with Xcode 12`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020/10605/) provides additional information about the latest memory-debugging tools and best practices to help you optimize the memory footprint of your Metal apps and games.

## See Also

- [Setting resource storage modes](setting-resource-storage-modes.md)
  Set a storage mode that defines the memory location and access permissions of a resource.
- [Choosing a resource storage mode for Apple GPUs](choosing-a-resource-storage-mode-for-apple-gpus.md)
  Select an appropriate storage mode for your textures and buffers on Apple GPUs.
- [Choosing a resource storage mode for Intel and AMD GPUs](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md)
  Select an appropriate storage mode for your textures and buffers on AMD and Intel GPUs.
- [Copying data to a private resource](copying-data-to-a-private-resource.md)
  Use a blit command encoder to copy buffer or texture data to a private resource.
- [Synchronizing a managed resource in macOS](synchronizing-a-managed-resource-in-macos.md)
  Manually synchronize memory for a Metal resource in apps.
- [Transferring data between connected GPUs](transferring-data-between-connected-gpus.md)
  Use high-speed connections between GPUs to transfer data quickly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/reducing-the-memory-footprint-of-metal-apps)*