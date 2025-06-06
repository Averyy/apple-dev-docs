# maximumWithNaNPropagation(_:_:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Returns the elementwise maximum of the input tensors, while propagating `NaN` values.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func maximumWithNaNPropagation(_ primaryTensor: MPSGraphTensor, _ secondaryTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid `MPSGraphTensor` object containing the elementwise result of the applied operation.

#### Discussion

This operation creates a maximum with `NaN` propagation operation and returns the result tensor. This means that if any of the elementwise operands is `NaN`, the result is `NaN`. It supports broadcasting as well.

```md
resultTensor = isNaN(primaryTensor) || isNan(secondaryTensor) ? NaN : max(primaryTensor, secondaryTensor) 
```

## Parameters

- `primaryTensor`: The LHS tensor of the binary Op.
- `secondaryTensor`: The RHS tensor of the binary Op.
- `name`: An optional string which serves as an identifier for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/maximumwithnanpropagation(_:_:name:))*