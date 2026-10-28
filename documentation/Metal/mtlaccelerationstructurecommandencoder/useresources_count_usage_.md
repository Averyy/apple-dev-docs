# useResources:count:usage:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Specifies that an array of resources in an argument buffer can be safely used by the acceleration structure pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) useResources:(id<MTLResource> const[]) resources count:(NSUInteger) count usage:(MTLResourceUsage) usage;
```

## Discussion

This method makes the array of resources resident for the duration of a compute pass and ensures that it’s in a format compatible with the compute function.

Call this method before issuing any dispatch calls that may access the array of resources. Calling this method again, or calling [`useHeap(_:)`](../mtlcomputecommandencoder/useheap%28_%29.md), overwrites any previously specified usage options for future dispatch calls within the same compute command encoder.

> **Note**:  You can track resource access and dependency hazards with [`MTLFence`](../mtlfence.md) instances.

## Parameters

- `resources`: An array of resources within an argument buffer.
- `count`: The number of resource elements in `resources`.
- `usage`: Options that indicate how a GPU function accesses each resource in `resources`.

## See Also

### Making indirect resources resident
- [func useHeap(any MTLHeap)](./useheap%28_%29.md)
  Makes the resources contained in the specified heap available to the acceleration structure pass.
- [- useHeaps:count:](./useheaps_count_.md)
  Specifies that an array of heaps containing resources in an argument buffer can be safely used by the acceleration structure pass.
- [func useResource(any MTLResource, usage: MTLResourceUsage)](./useresource%28_,usage%29.md)
  Makes a resource available to the acceleration structure pass.
- [struct MTLResourceUsage](../mtlresourceusage.md)
  Options that describe how a graphics or compute function uses an argument buffer’s resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/useresources:count:usage:)*