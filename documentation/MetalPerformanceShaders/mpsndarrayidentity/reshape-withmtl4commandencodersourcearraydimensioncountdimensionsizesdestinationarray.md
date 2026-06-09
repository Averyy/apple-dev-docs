# reshape(withMTL4CommandEncoder:sourceArray:dimensionCount:dimensionSizes:destinationArray:)

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
func reshape(withMTL4CommandEncoder encoder: any MTL4ComputeCommandEncoder, sourceArray: MPSNDArray, dimensionCount numberOfDimensions: Int, dimensionSizes: UnsafeMutablePointer<Int>, destinationArray: MPSNDArray)
```

#### Discussion

Encode a reshape operation. The encoder associates the commands with MTLStageDispatch. Synchronize your workloads against this stage when using this function to prevent race conditions.

## Parameters

- `encoder`: The MTL4ComputeCommandEncoder to encode the kernel with.
- `sourceArray`: The source NDArray.
- `numberOfDimensions`: The NDArray’s dimension count.
- `dimensionSizes`: The extents of each dimension of the NDArray.
- `destinationArray`: The destination NDArray. The shape of `destinationArray` must match `numberOfDimensions` and `dimensionSizes`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayidentity/reshape(withmtl4commandencoder:sourcearray:dimensioncount:dimensionsizes:destinationarray:))*