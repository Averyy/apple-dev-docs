# select(predicate:trueTensor:falseTensor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Selects values from either the true or false predicate tensor, depending on the values in the first input.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func select(predicate predicateTensor: MPSGraphTensor, trueTensor truePredicateTensor: MPSGraphTensor, falseTensor falseSelectTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid `MPSGraphTensor` object containing the elementwise result of the applied operation.

#### Discussion

This operation creates a select operation and returns the result tensor. It supports broadcasting as well.

```md
resultTensor = select(predicateTensor, truePredicateTensor, falseSelectTensor)
```

## Parameters

- `predicateTensor`: The predicate tensor.
- `truePredicateTensor`: The tensor to select values from if predicate is true.
- `falseSelectTensor`: The tensor to select values from if predicate is false.
- `name`: An optional string which serves as an identifier for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/select(predicate:truetensor:falsetensor:name:))*