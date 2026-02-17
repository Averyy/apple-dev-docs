# encode(to:sourceArray:destinationArray:)

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
func encode(to cmdBuf: any MTL4CommandBuffer, sourceArray: MPSNDArray, destinationArray destination: MPSNDArray)
```

#### Discussion

Encode a simple inference NDArray kernel and return a NDArray to hold the result

## Parameters

- `cmdBuf`: The MTL4command buffer into which to encode the kernel
- `sourceArray`: The source for the filter in an NSArray.
- `destination`: The NDArray to receive the result


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayunarykernel/encode(to:sourcearray:destinationarray:)-9cvxn)*