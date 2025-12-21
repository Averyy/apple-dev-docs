# dispatchThreads(_:threadsPerThreadgroup:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a compute command using an arbitrarily sized grid.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
func dispatchThreads(_ threadsPerGrid: MTLSize, threadsPerThreadgroup: MTLSize)
```

## Mentions

- [Calculating threadgroup and grid sizes](calculating-threadgroup-and-grid-sizes.md)

#### Discussion

> ⚠️ **Warning**:  Use this method only if the device your app is running on supports nonuniform threadgroup sizes. Check for device capabilities with [`supportsFamily(_:)`](mtldevice/supportsfamily(_:).md) on the device providing your compute command encoder. See [`Metal Feature Set Tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for device support information.

This method encodes a call that uses an arbitrary number of threads in its execution grid. Metal calculates the number of threadgroups needed, providing partial threadgroups if necessary. Prefer this method to [`dispatchThreadgroups(_:threadsPerThreadgroup:)`](mtlcomputecommandencoder/dispatchthreadgroups(_:threadsperthreadgroup:).md) if your app requires bounds checking or you need extra data allocations to saturate a uniform grid.

## Parameters

- `threadsPerGrid`: The number of threads in the grid, in each dimension.
- `threadsPerThreadgroup`: The number of threads in one threadgroup, in each dimension.

## See Also

- [func dispatchThreadgroups(MTLSize, threadsPerThreadgroup: MTLSize)](mtlcomputecommandencoder/dispatchthreadgroups(_:threadsperthreadgroup:).md)
  Encodes a compute dispatch command using a grid aligned to threadgroup boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/dispatchthreads(_:threadsperthreadgroup:))*