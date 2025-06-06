# unstacked(alongAxis:)

**Framework**: Core ML  
**Kind**: method

Unpacks the given dimension of a rank-`R` tensor into multiple rank-`(R-1)` tensors.

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
func unstacked(alongAxis axis: Int = 0) -> [MLTensor]
```

#### Return Value

An array containing the unstacked tensors.

#### Discussion

Unpacks `N` tensors from this tensor by chipping it along the `axis` dimension, where `N` is inferred from this tensor’s shape. For example, given a tensor with shape `[A, B, C, D]`:

- If `axis == 0` then the `i`-th tensor in the returned array is the slice `self[i, nil, nil, nil]` and each tensor in that array will have shape `[B, C, D]`.
- If `axis == 1` then the `i`-th tensor in the returned array is the slice `value[:, i, :, :]` and each tensor in that array will have shape `[A, C, D]`.
- Etc.

This is the opposite of `MLTensor.init(stacking:alongAxis:)`.

## Parameters

- `axis`: The dimension along which to unstack. The   must be in the range  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/unstacked(alongaxis:))*