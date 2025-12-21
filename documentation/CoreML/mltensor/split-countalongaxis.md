# split(count:alongAxis:)

**Framework**: Core ML  
**Kind**: method

Splits a tensor into multiple tensors. The tensor is split along dimension `axis` into `count` smaller tensors.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func split(count: Int, alongAxis axis: Int = 0) -> [MLTensor]
```

#### Return Value

An array containing the tensor parts.

#### Discussion

For example:

```None
// 'value' is a tensor with shape [5, 30]
// Split 'value' into 3 tensors along dimension 1:
let parts = value.split(count: 3, alongAxis: 1)
parts[0] // has shape [5, 10]
parts[1] // has shape [5, 10]
parts[2] // has shape [5, 10]
```

## Parameters

- `count`: The number of splits to create, must divide the size of dimension   evenly.
- `axis`: The dimension along which to split this tensor. The   must be in the range  .

## See Also

- [func split(sizes: [Int], alongAxis: Int) -> [MLTensor]](mltensor/split(sizes:alongaxis:).md)
  Splits a tensor into multiple tensors. The tensor is split  into `sizes.shape[0]` parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/split(count:alongaxis:))*