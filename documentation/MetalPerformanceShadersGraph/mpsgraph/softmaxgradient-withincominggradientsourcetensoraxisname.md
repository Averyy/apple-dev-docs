# softMaxGradient(withIncomingGradient:sourceTensor:axis:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Computes the gradient of the softmax function along the specified axis using the incoming gradient tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func softMaxGradient(withIncomingGradient gradient: MPSGraphTensor, sourceTensor source: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid [`MPSGraphTensor`](mpsgraphtensor.md) object

## Parameters

- `gradient`: The incoming gradient tensor.
- `source`: The input tensor.
- `axis`: The axis along which softmax is computed.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/softmaxgradient(withincominggradient:sourcetensor:axis:name:))*