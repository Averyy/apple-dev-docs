# gradients(of:with:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Calculates a partial derivative of primaryTensor with respect to the tensors.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func gradients(of primaryTensor: MPSGraphTensor, with tensors: [MPSGraphTensor], name: String?) -> [MPSGraphTensor : MPSGraphTensor]
```

#### Return Value

A valid MPSGraphTensor dictionary object containing partial derivative d(primaryTensor)/d(secondaryTensor) for each tensor as key.

## Parameters

- `primaryTensor`: Tensor to be differentiated (numerator).
- `tensors`: Tensors to do the differentiation with (denominator).
- `name`: Name for the gradient operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/gradients(of:with:name:))*