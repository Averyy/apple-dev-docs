# split(_:splitSizesTensor:axis:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a split operation and returns the result tensor.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
func split(_ tensor: MPSGraphTensor, splitSizesTensor: MPSGraphTensor, axis: Int, name: String?) -> [MPSGraphTensor]
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

Splits the input tensor along `axis` into multiple result tensors of size determined by `splitSizesTensor`. Requires that the sum of the elements of `splitSizesTensor` is equal to the lenth of the input along `axis`.

## Parameters

- `tensor`: The input tensor
- `splitSizesTensor`: The lengths of the result tensors along the split axis.
- `axis`: The dimension along which MPSGraph splits the input tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/split(_:splitsizestensor:axis:name:))*