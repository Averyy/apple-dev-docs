# Tracking the Resource Residency of Argument Buffers

**Framework**: Metal

Optimize resource performance within an argument buffer.

#### Overview

The Metal driver can’t automatically track the residency of argument buffer resources, but you can track it manually.

##### Track Argument Buffer Resource Residency Manually

Call an [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) or [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) method:

- For individual resources, call [`useResource(_:usage:stages:)`](mtlrendercommandencoder/useresource(_:usage:stages:).md) or [`useResource(_:usage:)`](mtlcomputecommandencoder/useresource(_:usage:).md).
- For all resources in a heap, call [`useHeap(_:stages:)`](mtlrendercommandencoder/useheap(_:stages:).md) or [`useHeap(_:)`](mtlcomputecommandencoder/useheap(_:).md).

These methods perform two important functions:

- They add argument buffer resources to the set of resources that the render or compute pass needs resident.
- They ensure that argument buffer resources are in a format that’s compatible with the required function operation, as an [`MTLResourceUsage`](mtlresourceusage.md) value specifies.

The methods with a `stages` parameter also insert dependency hazards, similar to [`MTLFence`](mtlfence.md) instances for that stage.

Call these methods before issuing any draw or dispatch calls that may access the specified resources.

> **Note**:  To track resource access and dependency hazards, use [`MTLFence`](mtlfence.md) instances. If all the required resources aren’t resident when executing a render or compute pass, the associated [`MTLCommandBuffer`](mtlcommandbuffer.md) instance fails.

 To track resource access and dependency hazards, use [`MTLFence`](mtlfence.md) instances.

If all the required resources aren’t resident when executing a render or compute pass, the associated [`MTLCommandBuffer`](mtlcommandbuffer.md) instance fails.

## See Also

- [Improving CPU Performance by Using Argument Buffers](improving-cpu-performance-by-using-argument-buffers.md)
  Optimize your app’s performance by grouping your resources into argument buffers.
- [Managing groups of resources with argument buffers](managing-groups-of-resources-with-argument-buffers.md)
  Create argument buffers to organize related resources.
- [Indexing Argument Buffers](indexing-argument-buffers.md)
  Assign resource indices within an argument buffer.
- [Rendering Terrain Dynamically with Argument Buffers](rendering-terrain-dynamically-with-argument-buffers.md)
  Use argument buffers to render terrain in real time with a GPU-driven pipeline.
- [Encoding Argument Buffers on the GPU](encoding-argument-buffers-on-the-gpu.md)
  Use a compute pass to encode an argument buffer and access its arguments in a subsequent render pass.
- [Using Argument Buffers with Resource Heaps](using-argument-buffers-with-resource-heaps.md)
  Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [class MTLArgumentDescriptor](mtlargumentdescriptor.md)
  A representation of an argument within an argument buffer.
- [protocol MTLArgumentEncoder](mtlargumentencoder.md)
  An object used to encode data into an argument buffer.
- [let MTLAttributeStrideStatic: Int](mtlattributestridestatic.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/tracking-the-resource-residency-of-argument-buffers)*