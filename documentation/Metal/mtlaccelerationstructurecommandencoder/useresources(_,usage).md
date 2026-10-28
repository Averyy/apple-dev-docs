# useResources(_:usage:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Makes multiple resources available to the acceleration structure pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS

## Declaration

```swift
func useResources(_ resources: [any MTLResource], usage: MTLResourceUsage)
```

## Discussion

This method makes the resources resident for the duration of a compute pass and ensures that they are in a format compatible with the compute function.

Call this method before issuing any dispatch calls that may access the resource. Calling this method again, or calling [`useHeap(_:)`](../mtlcomputecommandencoder/useheap%28_%29.md), overwrites any previously specified usage options for future dispatch calls within the same compute command encoder.

> **Note**:  You can track resource access and dependency hazards with [`MTLFence`](../mtlfence.md) instances.

## Parameters

- `resources`: An array of resources within an argument buffer.
- `usage`: Options that indicate how a GPU function accesses each resource in `resources`.

## See Also

### Making indirect resources resident
- [func useHeap(any MTLHeap)](./useheap%28_%29.md)
  Makes the resources contained in the specified heap available to the acceleration structure pass.
- [func useHeaps([any MTLHeap])](./useheaps%28_%29.md)
  Makes the resources contained in the specified heaps available to the acceleration structure pass.
- [func useResource(any MTLResource, usage: MTLResourceUsage)](./useresource%28_,usage%29.md)
  Makes a resource available to the acceleration structure pass.
- [struct MTLResourceUsage](../mtlresourceusage.md)
  Options that describe how a graphics or compute function uses an argument buffer’s resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/useresources(_:usage:))*