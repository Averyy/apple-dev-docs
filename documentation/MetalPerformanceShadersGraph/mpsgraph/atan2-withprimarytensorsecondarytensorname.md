# atan2(withPrimaryTensor:secondaryTensor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Returns the elementwise two-argument arctangent of the input tensors.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func atan2(withPrimaryTensor primaryTensor: MPSGraphTensor, secondaryTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid `MPSGraphTensor` object containing the elementwise result of the applied operation.

#### Discussion

This operation creates a `atan2` operation and returns the result tensor. It supports broadcasting as well. Graph computes arc tangent of primaryTensor over secondaryTensor.

```md
resultTensor = atan2(primaryTensor, secondaryTensor)
```

## Parameters

- `primaryTensor`: The LHS tensor of the binary Op.
- `secondaryTensor`: The RHS tensor of the binary Op.
- `name`: An optional string which serves as an identifier for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/atan2(withprimarytensor:secondarytensor:name:))*