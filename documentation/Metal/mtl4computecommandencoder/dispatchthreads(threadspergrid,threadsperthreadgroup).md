# dispatchThreads(threadsPerGrid:threadsPerThreadgroup:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a compute dispatch command using an arbitrarily-sized grid.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func dispatchThreads(threadsPerGrid: MTLSize, threadsPerThreadgroup: MTLSize)
```

```objc
- (void) dispatchThreads:(MTLSize) threadsPerGrid threadsPerThreadgroup:(MTLSize) threadsPerThreadgroup;
```

## Parameters

- `threadsPerGrid`: An [`MTLSize`](../mtlsize.md) instance that represents the number of threads in the grid, in each dimension.
- `threadsPerThreadgroup`: An [`MTLSize`](../mtlsize.md) instance that represents the number of threads in one threadgroup, in each dimension.

## See Also

### Running dispatch commands
- [func dispatchThreads(indirectBuffer: MTLGPUAddress)](./dispatchthreads%28indirectbuffer%29.md)
  Encodes a compute dispatch command with an arbitrarily sized grid, using an indirect buffer for arguments.
- [func dispatchThreadgroups(threadgroupsPerGrid: MTLSize, threadsPerThreadgroup: MTLSize)](./dispatchthreadgroups%28threadgroupspergrid,threadsperthreadgroup%29.md)
  Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries.
- [func dispatchThreadgroups(indirectBuffer: MTLGPUAddress, threadsPerThreadgroup: MTLSize)](./dispatchthreadgroups%28indirectbuffer,threadsperthreadgroup%29.md)
  Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries, using an indirect buffer for arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/dispatchthreads(threadspergrid:threadsperthreadgroup:))*