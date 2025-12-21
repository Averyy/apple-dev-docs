# useResource(_:usage:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Makes a resource available to the acceleration structure pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func useResource(_ resource: any MTLResource, usage: MTLResourceUsage)
```

#### Discussion

This method makes the resource resident for the duration of a compute pass and ensures that it’s in a format compatible with the compute function.

Call this method before issuing any dispatch calls that may access the resource. Calling this method again, or calling [`useHeap(_:)`](mtlcomputecommandencoder/useheap(_:).md), overwrites any previously specified usage options for future dispatch calls within the same compute command encoder.

> **Note**:  You can track resource access and dependency hazards with [`MTLFence`](mtlfence.md) instances.

## Parameters

- `resource`: A specific resource within an argument buffer.
- `usage`: The options that describe how the compute function uses the resource.

## See Also

- [func useHeap(any MTLHeap)](mtlaccelerationstructurecommandencoder/useheap(_:).md)
  Makes the resources contained in the specified heap available to the acceleration structure pass.
- [func useHeaps([any MTLHeap])](mtlaccelerationstructurecommandencoder/useheaps(_:).md)
  Makes the resources contained in the specified heaps available to the acceleration structure pass.
- [func useResources([any MTLResource], usage: MTLResourceUsage)](mtlaccelerationstructurecommandencoder/useresources(_:usage:).md)
  Makes multiple resources available to the acceleration structure pass.
- [struct MTLResourceUsage](mtlresourceusage.md)
  Options that describe how a graphics or compute function uses an argument buffer’s resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/useresource(_:usage:))*