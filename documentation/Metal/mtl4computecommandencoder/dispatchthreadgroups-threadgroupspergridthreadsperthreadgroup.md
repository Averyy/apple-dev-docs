# dispatchThreadgroups(threadgroupsPerGrid:threadsPerThreadgroup:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a compute dispatch command with a grid that aligns to threadgroup boundaries.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func dispatchThreadgroups(threadgroupsPerGrid: MTLSize, threadsPerThreadgroup: MTLSize)
```

## Parameters

- `threadgroupsPerGrid`: An   instance that represents the number of threadgroups in the grid,   in each dimension.
- `threadsPerThreadgroup`: An   instance that represents the number of threads in one   threadgroup, in each dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/dispatchthreadgroups(threadgroupspergrid:threadsperthreadgroup:))*