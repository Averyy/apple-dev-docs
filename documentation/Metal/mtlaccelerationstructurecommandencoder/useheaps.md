# useHeaps(_:)

**Framework**: Metal  
**Kind**: method

Makes the resources contained in the specified heaps available to the acceleration structure pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
func useHeaps(_ heaps: [any MTLHeap])
```

#### Discussion

This method makes all the resources in multiple heaps resident for the duration of a compute pass and ensures that they’re in a format compatible with the compute function.

Call this method before issuing any dispatch calls that may access the resources in the heap.

You can only read or sample resources in the specified heap. This method ignores render targets (textures that specify a [`renderTarget`](mtltextureusage/rendertarget.md) usage option) and writable textures (textures that specify a [`shaderWrite`](mtltextureusage/shaderwrite.md) usage option) within the heap. To use these resources, you must call the [`useResource(_:usage:)`](mtlcomputecommandencoder/useresource(_:usage:).md) method instead.

> **Note**:  To track resource access and dependency hazards, you must use [`MTLFence`](mtlfence.md) objects.

## Parameters

- `heaps`: The sets of heap that contain resources to mark as used.

## See Also

- [func useHeap(any MTLHeap)](mtlaccelerationstructurecommandencoder/useheap(_:).md)
  Makes the resources contained in the specified heap available to the acceleration structure pass.
- [func useResource(any MTLResource, usage: MTLResourceUsage)](mtlaccelerationstructurecommandencoder/useresource(_:usage:).md)
  Makes a resource available to the acceleration structure pass.
- [func useResources([any MTLResource], usage: MTLResourceUsage)](mtlaccelerationstructurecommandencoder/useresources(_:usage:).md)
  Makes multiple resources available to the acceleration structure pass.
- [struct MTLResourceUsage](mtlresourceusage.md)
  Options that describe how a graphics or compute function uses an argument buffer’s resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/useheaps(_:))*