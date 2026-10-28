# useHeaps:count:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Specifies that an array of heaps containing resources in an argument buffer can be safely used by the acceleration structure pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) useHeaps:(id<MTLHeap> const[]) heaps count:(NSUInteger) count;
```

## Discussion

This method makes all the resources in the array of heaps resident for the duration of a compute pass and ensures that they’re in a format compatible with the compute function.

Call this method before issuing any dispatch calls that may access the resources in the array of heaps.

Resources within the specified array of heaps can only be read or sampled from. This method ignores render targets (textures that specify a [`renderTarget`](../mtltextureusage/rendertarget.md) usage option) and writable textures (textures that specify a [`shaderWrite`](../mtltextureusage/shaderwrite.md) usage option) within the array of heaps. To use these resources, you need to call the [`useResource(_:usage:)`](../mtlcomputecommandencoder/useresource%28_,usage%29.md) method instead.

> **Note**:  You can synchronize memory operations to address dependency hazards with [`MTLFence`](../mtlfence.md) instances.

## Parameters

- `heaps`: An array of heaps that contains resources within an argument buffer.
- `count`: The number of heaps in the array.

## See Also

### Making indirect resources resident
- [func useHeap(any MTLHeap)](./useheap%28_%29.md)
  Makes the resources contained in the specified heap available to the acceleration structure pass.
- [func useResource(any MTLResource, usage: MTLResourceUsage)](./useresource%28_,usage%29.md)
  Makes a resource available to the acceleration structure pass.
- [- useResources:count:usage:](./useresources_count_usage_.md)
  Specifies that an array of resources in an argument buffer can be safely used by the acceleration structure pass.
- [struct MTLResourceUsage](../mtlresourceusage.md)
  Options that describe how a graphics or compute function uses an argument buffer’s resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/useheaps:count:)*