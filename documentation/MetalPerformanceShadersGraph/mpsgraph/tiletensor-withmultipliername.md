# tileTensor(_:withMultiplier:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a tile operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func tileTensor(_ tensor: MPSGraphTensor, withMultiplier multiplier: [NSNumber], name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Creates a tensor which contains multiple copies of the input tensor along each dimension of the tensor.

## Parameters

- `tensor`: The input tensor
- `multiplier`: An array of numbers that specifies how many copies per dimension MPSGraph produces.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/tiletensor(_:withmultiplier:name:))*