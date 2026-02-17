# encode(to:sourceArray:resultState:destinationArray:)

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func encode(to cmdBuf: any MTLCommandBuffer, sourceArray: MPSNDArray, resultState outGradientState: MPSState?, destinationArray destination: MPSNDArray)
```

#### Discussion

Encode a simple inference NDArray kernel and return a NDArray to hold the result

## Parameters

- `cmdBuf`: The command buffer into which to encode the kernel
- `sourceArray`: The source for the filter in an NSArray.
- `outGradientState`: The output gradient state to record the operation for later use by gradient
- `destination`: A destination array to contain the result of the calculation   when the command buffer completes successfully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayunarykernel/encode(to:sourcearray:resultstate:destinationarray:)-7lmzc)*