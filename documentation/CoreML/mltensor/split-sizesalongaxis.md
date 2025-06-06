# split(sizes:alongAxis:)

**Framework**: Core ML  
**Kind**: method

Splits a tensor into multiple tensors. The tensor is split  into `sizes.shape[0]` parts.

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
func split(sizes: [Int], alongAxis axis: Int = 0) -> [MLTensor]
```

#### Return Value

Array containing the tensors parts.

#### Discussion

For example:

```None
// 'value' is a tensor with shape [5, 30]
// Split 'value' into 3 tensors with sizes [4, 15, 11] along dimension 1:
let parts = value.split(sizes: [4, 15, 11], alongAxis: 1)
parts[0] // has shape [5, 4]
parts[1] // has shape [5, 15]
parts[2] // has shape [5, 11]
```

## Parameters

- `sizes`: A one-dimensional tensor containing the size of each split, must add up to the size of dimension  .
- `axis`: The dimension along which to split this tensor. Must be in the range  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/split(sizes:alongaxis:))*