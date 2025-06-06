# resize(_:sizeTensor:scaleTensor:offsetTenor:mode:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a Resize operation and returns the result tensor.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func resize(_ imagesTensor: MPSGraphTensor, sizeTensor size: MPSGraphTensor, scaleTensor scale: MPSGraphTensor, offsetTenor offset: MPSGraphTensor, mode: MPSGraphResizeMode, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

Resamples input images to given size using the provided scale and offset. Destination indices are computed using

```md
dst_indices = (src_indices * scale) + offset
```

For most use cases passing the scale and offset directly is unnecessary, and it is preferable to use the API specifying centerResult and alignCorners.

## Parameters

- `imagesTensor`: Tensor containing input images.
- `size`: The target size of the result tensor.  1D Int32 or Int64 tensor of size equal to rank of input.
- `scale`: 1D float tensor of size equal to rank of input.
- `offset`: 1D float tensor of size equal to rank of input.
- `mode`: The resampling mode to use. If nearest sampling is specifed, RoundPreferCeil mode will be used.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/resize(_:sizetensor:scaletensor:offsettenor:mode:name:))*