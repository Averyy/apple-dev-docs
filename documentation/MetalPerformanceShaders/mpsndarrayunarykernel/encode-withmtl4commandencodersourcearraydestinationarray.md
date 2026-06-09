# encode(withMTL4CommandEncoder:sourceArray:destinationArray:)

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
func encode(withMTL4CommandEncoder encoder: any MTL4ComputeCommandEncoder, sourceArray: MPSNDArray, destinationArray destination: MPSNDArray)
```

#### Discussion

Encode a simple inference NDArray kernel. The encoder associates the commands with MTLStageDispatch. Synchronize your workloads against this stage when using this function to prevent race conditions.

## Parameters

- `encoder`: The MTL4ComputeCommandEncoder to encode the kernel with.
- `sourceArray`: The source NDArray.
- `destination`: The destination NDArray.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayunarykernel/encode(withmtl4commandencoder:sourcearray:destinationarray:))*