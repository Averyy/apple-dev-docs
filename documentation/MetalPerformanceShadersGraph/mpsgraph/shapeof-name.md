# shapeOf(_:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a shape-of operation and returns the result tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func shapeOf(_ tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Returns a rank-1 tensor of type `MPSDataTypeInt32` with the values of the static shape of the input tensor.

## Parameters

- `tensor`: The input tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/shapeof(_:name:))*