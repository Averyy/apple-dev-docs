# divisionNoNaN(_:_:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Divides the first input tensor by the second, with the result being 0 if the denominator is 0.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func divisionNoNaN(_ primaryTensor: MPSGraphTensor, _ secondaryTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid `MPSGraphTensor` object containing the elementwise result of the applied operation.

#### Discussion

```md
resultTensor = select(secondaryTensor, primaryTensor / secondaryTensor, 0)
```

## Parameters

- `primaryTensor`: The LHS tensor of the binary Op.
- `secondaryTensor`: The RHS tensor of the binary Op.
- `name`: An optional string which serves as an identifier for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/divisionnonan(_:_:name:))*