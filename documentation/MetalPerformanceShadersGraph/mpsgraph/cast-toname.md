# cast(_:to:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a cast operation and returns the result tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func cast(_ tensor: MPSGraphTensor, to type: MPSDataType, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Returns the input tensor casted to the specied data type.

## Parameters

- `tensor`: The input tensor.
- `type`: The datatype to which MPSGraph casts the input.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/cast(_:to:name:))*