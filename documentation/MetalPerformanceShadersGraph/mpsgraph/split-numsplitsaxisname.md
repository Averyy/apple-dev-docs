# split(_:numSplits:axis:name:)

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
func split(_ tensor: MPSGraphTensor, numSplits: Int, axis: Int, name: String?) -> [MPSGraphTensor]
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Splits the input tensor along `axis` into `numsplits` result tensors of equal size. Requires that the lenth of the input along `axis` is divisible by `numSplits`.

## Parameters

- `tensor`: The input tensor.
- `numSplits`: The number of result tensors to split to.
- `axis`: The dimension along which MPSGraph splits the input tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/split(_:numsplits:axis:name:))*