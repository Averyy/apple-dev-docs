# avgPooling2DGradient(withGradientTensor:sourceTensor:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a 2D average pooling gradient operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func avgPooling2DGradient(withGradientTensor gradient: MPSGraphTensor, sourceTensor source: MPSGraphTensor, descriptor: MPSGraphPooling2DOpDescriptor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

## Parameters

- `gradient`: A 2D input gradient tensor - must be of rank=4. The layout is defined by  .
- `source`: The input tensor for the forward pass.
- `descriptor`: A pooling operation descriptor that specifies pooling window sizes, strides, dilation rates, paddings and layouts.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/avgpooling2dgradient(withgradienttensor:sourcetensor:descriptor:name:))*