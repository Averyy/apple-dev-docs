# realPartOfTensor(tensor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Returns the real part of a tensor.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func realPartOfTensor(tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid `MPSGraphTensor` object containing the elementwise result of the applied operation.

## Parameters

- `tensor`: The input tensor.
- `name`: An optional string which serves as an identifier for the operation..


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/realpartoftensor(tensor:name:))*