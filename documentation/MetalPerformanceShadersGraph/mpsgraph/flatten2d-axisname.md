# flatten2D(_:axis:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a flatten2D operation and returns the result tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func flatten2D(_ tensor: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Flattens dimensions before `axis` to `result[0]` and dimensions starting from `axis` to `result[1]` and returns a rank-2 tensor as result.

## Parameters

- `tensor`: The tensor to be flattened.
- `axis`: The axis around which to flatten.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/flatten2d(_:axis:name:))*