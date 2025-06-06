# reciprocalSquareRoot(_:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Applies the reciprocal square root operation to the input tensor elements.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func reciprocalSquareRoot(_ tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid `MPSGraphTensor` object containing the elementwise result of the applied operation.

## Parameters

- `tensor`: The input tensor.
- `name`: An optional string which serves as an identifier for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/reciprocalsquareroot(_:name:))*