# stack(_:axis:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a stack operation and returns the result tensor.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
func stack(_ inputTensors: [MPSGraphTensor], axis: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Stacks all input tensors along `axis` into a result tensor of `rank + 1`. Tensors must be broadcast compatible along all dimensions except `axis`, and have the same type.

## Parameters

- `inputTensors`: The input tensors.
- `axis`: The dimension to stack tensors into result. Must be in range:  .
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/stack(_:axis:name:))*