# complexTensor(realTensor:imaginaryTensor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Returns a complex tensor from the two input tensors.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func complexTensor(realTensor: MPSGraphTensor, imaginaryTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid `MPSGraphTensor` object containing the elementwise result of the applied operation.

## Parameters

- `realTensor`: The real part of the complex tensor.
- `imaginaryTensor`: The imaginary part of the complex tensor.
- `name`: An optional string which serves as an identifier for the operation..


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/complextensor(realtensor:imaginarytensor:name:))*