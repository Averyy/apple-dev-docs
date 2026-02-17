# encode(toMTL4CommandEncoder:mtl4commandBuffer:sourceArrays:destinationArray:)

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func encode(toMTL4CommandEncoder encoder: (any MTL4ComputeCommandEncoder)?, mtl4commandBuffer commandBuffer: any MTL4CommandBuffer, sourceArrays: [MPSNDArray], destinationArray destination: MPSNDArray)
```

#### Discussion

Encode a simple inference NDArray kernel and return a NDArray to hold the result

## Parameters

- `encoder`: The MTLComputeCommandEncoder that the kernel will be encoded on
- `commandBuffer`: The command buffer into which to encode the kernel
- `sourceArrays`: The list of sources for the filter in a NSArray.   Ordering to be defined by subclass
- `destination`: A destination array to contain the result of the calculation   when the command buffer completes successfully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraymultiarykernel/encode(tomtl4commandencoder:mtl4commandbuffer:sourcearrays:destinationarray:))*