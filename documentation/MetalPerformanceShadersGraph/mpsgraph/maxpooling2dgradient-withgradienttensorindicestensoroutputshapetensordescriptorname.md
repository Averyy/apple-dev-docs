# maxPooling2DGradient(withGradientTensor:indicesTensor:outputShapeTensor:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a max-pooling gradient operation and returns the result tensor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func maxPooling2DGradient(withGradientTensor gradient: MPSGraphTensor, indicesTensor indices: MPSGraphTensor, outputShapeTensor outputShape: MPSGraphTensor, descriptor: MPSGraphPooling2DOpDescriptor, name: String?) -> MPSGraphTensor
```

#### Return Value

Destination gradient tensor.

#### Discussion

With this API MPSGraph computes the max-pooling gradient efficiently by reusing the indices from the forward API instead of recomputing them. The descriptor must set `returnIndicesMode` and `returnIndicesDataType` to the same value as that set by the forward pass.

## Parameters

- `gradient`: A 2D input gradient tensor - must be of rank=4. The layout is defined by  .
- `indices`: The indices tensor returned from  .
- `outputShape`: A tensor containing the shape of the destination gradient.
- `descriptor`: A pooling operation descriptor that specifies pooling window sizes, strides, dilation rates, paddings and layouts.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/maxpooling2dgradient(withgradienttensor:indicestensor:outputshapetensor:descriptor:name:))*