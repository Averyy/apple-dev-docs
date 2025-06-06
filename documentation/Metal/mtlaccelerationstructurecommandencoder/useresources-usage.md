# useResources(_:usage:)

**Framework**: Metal  
**Kind**: method

Makes multiple resources available to the acceleration structure pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
func useResources(_ resources: [any MTLResource], usage: MTLResourceUsage)
```

#### Discussion

This method makes the resources resident for the duration of a compute pass and ensures that they are in a format compatible with the compute function.

Call this method before issuing any dispatch calls that may access the resource. Calling this method again, or calling [`useHeap(_:)`](mtlcomputecommandencoder/useheap(_:).md), overwrites any previously specified usage options for future dispatch calls within the same compute command encoder.

> **Note**:  To track resource access and dependency hazards, you must use [`MTLFence`](mtlfence.md) separately.

## Parameters

- `resources`: An array of resources within an argument buffer.
- `usage`: Options that indicate how a GPU function accesses each resource in  .

## See Also

- [func useHeap(any MTLHeap)](mtlaccelerationstructurecommandencoder/useheap(_:).md)
  Makes the resources contained in the specified heap available to the acceleration structure pass.
- [func useHeaps([any MTLHeap])](mtlaccelerationstructurecommandencoder/useheaps(_:).md)
  Makes the resources contained in the specified heaps available to the acceleration structure pass.
- [func useResource(any MTLResource, usage: MTLResourceUsage)](mtlaccelerationstructurecommandencoder/useresource(_:usage:).md)
  Makes a resource available to the acceleration structure pass.
- [struct MTLResourceUsage](mtlresourceusage.md)
  Options that describe how a graphics or compute function uses an argument buffer’s resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/useresources(_:usage:))*