# convolutionTranspose2D(_:weights:outputShapeTensor:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a convolution transpose operation and returns the result tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func convolutionTranspose2D(_ source: MPSGraphTensor, weights: MPSGraphTensor, outputShapeTensor outputShape: MPSGraphTensor, descriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

## Parameters

- `source`: Input tensor
- `weights`: Weights tensor
- `outputShape`: 1D Int32 or Int64 tensor. shape of the result tensor.
- `descriptor`: Descriptor for the corresponding forward Conv2D operation
- `name`: Name for the operation


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/convolutiontranspose2d(_:weights:outputshapetensor:descriptor:name:))*