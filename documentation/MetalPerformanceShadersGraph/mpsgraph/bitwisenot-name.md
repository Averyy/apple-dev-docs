# bitwiseNOT(_:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Applies the bitwise NOT operation to the input tensor element.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+

## Declaration

```swift
func bitwiseNOT(_ tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid `MPSGraphTensor` object containing the elementwise result of the applied operation.

#### Discussion

This operation only accepts integer tensors.

## Parameters

- `tensor`: The input tensor, which must be of integer type.
- `name`: An optional string which serves as an identifier for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/bitwisenot(_:name:))*