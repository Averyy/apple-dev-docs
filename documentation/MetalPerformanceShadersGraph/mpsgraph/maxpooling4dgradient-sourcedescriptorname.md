# maxPooling4DGradient(_:source:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a max-pooling gradient operation and returns the result tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func maxPooling4DGradient(_ gradient: MPSGraphTensor, source: MPSGraphTensor, descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

## Parameters

- `gradient`: An input gradient tensor.
- `source`: The input tensor for the forward pass.
- `descriptor`: A pooling operation descriptor that specifies pooling window sizes, strides, dilation rates and paddings.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/maxpooling4dgradient(_:source:descriptor:name:))*