# dispatchThreadgroups(_:threadsPerThreadgroup:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a compute dispatch command using a grid aligned to threadgroup boundaries.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func dispatchThreadgroups(_ threadgroupsPerGrid: MTLSize, threadsPerThreadgroup: MTLSize)
```

## Mentions

- [Calculating Threadgroup and Grid Sizes](calculating-threadgroup-and-grid-sizes.md)

#### Discussion

> 💡 **Tip**:  Prefer using dispatchThreads for your kernel calls on `Apple4` and later Apple GPUs. See [`Metal Feature Set Tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for information on hardware support.

Metal calculates the number of threads in a grid by multiplying `threadsPerThreadgroup` by `threadgroupsPerGrid`.

If the size of your data doesn’t match the size of the grid, perform boundary checks in your compute function to avoid accessing data out of bounds. See [`Calculating Threadgroup and Grid Sizes`](calculating-threadgroup-and-grid-sizes.md) for an example.

## Parameters

- `threadgroupsPerGrid`: An   instance that represents the number of threads for each grid dimension.
- `threadsPerThreadgroup`: An   instance that represents the number of threads in a threadgroup.

## See Also

- [func dispatchThreads(MTLSize, threadsPerThreadgroup: MTLSize)](mtlcomputecommandencoder/dispatchthreads(_:threadsperthreadgroup:).md)
  Encodes a compute command using an arbitrarily sized grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/dispatchthreadgroups(_:threadsperthreadgroup:))*