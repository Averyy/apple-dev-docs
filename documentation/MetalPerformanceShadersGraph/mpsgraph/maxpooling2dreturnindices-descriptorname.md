# maxPooling2DReturnIndices(_:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a 2D max-pooling operation and returns the result tensor and the corresponding indices tensor.

**Availability**:
- iOS 15.3+
- iPadOS 15.3+
- Mac Catalyst 15.3+
- macOS 12.2+
- tvOS 15.3+
- visionOS 1.0+

## Declaration

```swift
func maxPooling2DReturnIndices(_ source: MPSGraphTensor, descriptor: MPSGraphPooling2DOpDescriptor, name: String?) -> [MPSGraphTensor]
```

#### Return Value

An array of two MPSGraphTensors. The first tensor holds the result of max pool and the second tensor holds the corresponding indices

#### Discussion

In order to Computes the indices, `returnIndicesMode` of the descriptor must be set. The datatype of indices tensor can be set using `returnIndicesDataType`. If `returnIndicesMode = MPSGraphPoolingReturnIndicesNone` then only the first result MPSGraph returns will be valid and using the second result will assert.

## Parameters

- `source`: A 2D Image source as tensor - must be of rank=4. The layout is defined by  .
- `descriptor`: A pooling operation descriptor that specifies pooling window sizes, strides, dilation rates, paddings and layouts.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/maxpooling2dreturnindices(_:descriptor:name:))*