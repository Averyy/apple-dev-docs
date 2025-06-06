# broadcast(_:shapeTensor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a broadcast operation and returns the result tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func broadcast(_ tensor: MPSGraphTensor, shapeTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Broadcasts values inside the tensor, starting from the trailing dimensions, to give it the correct shape. This is equivalent to the broadcasting for arithmetic operations when operands have different shapes.

## Parameters

- `tensor`: The Tensor to be broadcasted.
- `shapeTensor`: A rank-1 tensor of type   or   that defines the shape of the result tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/broadcast(_:shapetensor:name:))*