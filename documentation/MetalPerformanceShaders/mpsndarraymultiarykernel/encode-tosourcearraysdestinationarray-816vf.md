# encode(to:sourceArrays:destinationArray:)

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
func encode(to cmdBuf: any MTLCommandBuffer, sourceArrays: [MPSNDArray], destinationArray destination: MPSNDArray)
```

#### Discussion

Encode a simple inference NDArray kernel and return a NDArray to hold the result

## Parameters

- `cmdBuf`: The command buffer into which to encode the kernel
- `sourceArrays`: The list of sources for the filter in a NSArray.   Ordering to be defined by subclass
- `destination`: The NDArray to receive the result


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraymultiarykernel/encode(to:sourcearrays:destinationarray:)-816vf)*