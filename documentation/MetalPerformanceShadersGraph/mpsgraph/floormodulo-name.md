# floorModulo(_:_:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Returns the remainder of floor divison between the primary and secondary tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func floorModulo(_ primaryTensor: MPSGraphTensor, _ secondaryTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid `MPSGraphTensor` object containing the elementwise result of the applied operation.

#### Discussion

Creates a floorModulo operation and returns the result tensor, it supports broadcasting as well, returns 0 if divisor is 0.

```md
resultTensor = primaryTensor - (floor(primaryTensor / secondaryTensor) * secondaryTensor)
```

## Parameters

- `primaryTensor`: The LHS tensor of the binary Op.
- `secondaryTensor`: The RHS tensor of the binary Op.
- `name`: An optional string which serves as an identifier for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/floormodulo(_:_:name:))*