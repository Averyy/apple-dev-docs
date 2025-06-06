# isFinite(with:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Checks if the input tensor elements are finite or not.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func isFinite(with tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid `MPSGraphTensor` object containing the elementwise result of the applied operation.

#### Discussion

If the input tensor element is finite, the operation returns `true`, else it returns `false`.

## Parameters

- `tensor`: The input tensor.
- `name`: An optional string which serves as an identifier for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/isfinite(with:name:))*