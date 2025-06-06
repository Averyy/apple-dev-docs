# bitwiseAND(_:_:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Returns the elementwise bitwise AND of binary representations of two integer tensors.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+

## Declaration

```swift
func bitwiseAND(_ primaryTensor: MPSGraphTensor, _ secondaryTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid `MPSGraphTensor` object containing the elementwise result of the applied operation.

## Parameters

- `primaryTensor`: The primary input tensor, must be of integer type.
- `secondaryTensor`: The secondary input tensor, must be of integer type.
- `name`: An optional string which serves as an identifier for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/bitwiseand(_:_:name:))*