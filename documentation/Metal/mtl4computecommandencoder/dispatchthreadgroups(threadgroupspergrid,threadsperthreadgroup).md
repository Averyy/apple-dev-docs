# dispatchThreadgroups(threadgroupsPerGrid:threadsPerThreadgroup:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func dispatchThreadgroups(threadgroupsPerGrid: MTLSize, threadsPerThreadgroup: MTLSize)
```

```objc
- (void) dispatchThreadgroups:(MTLSize) threadgroupsPerGrid threadsPerThreadgroup:(MTLSize) threadsPerThreadgroup;
```

## Parameters

- `threadgroupsPerGrid`: An [`MTLSize`](../mtlsize.md) instance that represents the number of threadgroups in the grid, in each dimension.
- `threadsPerThreadgroup`: An [`MTLSize`](../mtlsize.md) instance that represents the number of threads in one threadgroup, in each dimension.

## See Also

### Running dispatch commands
- [func dispatchThreads(threadsPerGrid: MTLSize, threadsPerThreadgroup: MTLSize)](./dispatchthreads%28threadspergrid,threadsperthreadgroup%29.md)
  Encodes a compute dispatch command using an arbitrarily-sized grid.
- [func dispatchThreads(indirectBuffer: MTLGPUAddress)](./dispatchthreads%28indirectbuffer%29.md)
  Encodes a compute dispatch command with an arbitrarily sized grid, using an indirect buffer for arguments.
- [func dispatchThreadgroups(indirectBuffer: MTLGPUAddress, threadsPerThreadgroup: MTLSize)](./dispatchthreadgroups%28indirectbuffer,threadsperthreadgroup%29.md)
  Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries, using an indirect buffer for arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/dispatchthreadgroups(threadgroupspergrid:threadsperthreadgroup:))*