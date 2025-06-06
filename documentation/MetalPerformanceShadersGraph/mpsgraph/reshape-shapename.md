# reshape(_:shape:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a reshape operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func reshape(_ tensor: MPSGraphTensor, shape: [NSNumber], name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

This operation reshapes the input tensor to the target shape. The shape must be compatible with the input tensor shape, specifically the volume of the input tensor has to match the volume defined by the shape. The shape is allowed to contain dynamic dimensions (-1) when the result type can be inferred unambiguously.

## Parameters

- `tensor`: The tensor to be reshaped.
- `shape`: The result tensor shape.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/reshape(_:shape:name:))*