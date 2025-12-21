# makeTensor(descriptor:offset:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a tensor that shares storage with this buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeTensor(descriptor: MTLTensorDescriptor, offset: Int) throws -> any MTLTensor
```

#### Discussion

If the descriptor specifies `MTLTensorUsageMachineLearning` usage, you need to observe the following restrictions:

- pass in `0` for the `offset` parameter
- set the element stride the descriptor to `1`
- ensure that number of bytes per row is a multiple of `64`
- for dimensions greater than `2`, make sure `strides[dim] = strides[dim -1] * dimensions[dim - 1]`

## Parameters

- `descriptor`: A description of the properties for the new tensor.
- `offset`: Offset into the buffer at which the data of the tensor begins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbuffer/maketensor(descriptor:offset:))*