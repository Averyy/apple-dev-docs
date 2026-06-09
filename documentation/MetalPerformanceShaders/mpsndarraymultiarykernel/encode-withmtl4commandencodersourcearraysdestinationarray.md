# encode(withMTL4CommandEncoder:sourceArrays:destinationArray:)

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func encode(withMTL4CommandEncoder encoder: any MTL4ComputeCommandEncoder, sourceArrays: [MPSNDArray], destinationArray destination: MPSNDArray)
```

#### Discussion

Encode a simple inference NDArray kernel. The encoder associates the commands with MTLStageDispatch. Synchronize your workloads against this stage when using this function to prevent race conditions.

## Parameters

- `encoder`: The MTL4ComputeCommandEncoder to encode the kernel with.
- `sourceArrays`: The source NDArray instances in a NSArray. Make sure the instances are arranged in the order required by the MPSNDArrayMultiaryKernel subclass.
- `destination`: The destination NDArray.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraymultiarykernel/encode(withmtl4commandencoder:sourcearrays:destinationarray:))*