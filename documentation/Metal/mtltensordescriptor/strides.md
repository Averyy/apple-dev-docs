# strides

**Framework**: Metal  
**Kind**: property

An array of strides, in elements, one for each dimension in the tensors you create with this descriptor, if applicable.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@NSCopying
var strides: MTLTensorExtents { get set }
```

#### Discussion

This property only applies to tensors you create from a buffer, otherwise it is nil. You are responsible for ensuring `strides` meets the following requirements:

- Elements of `strides`are in monotonically non-decreasing order.
- The first element of `strides` is one.
- For any `i` larger than zero, `strides[i]` is greater than or equal to `strides[i-1] * dimensions[i-1]`.
- If `usage` contains [`machineLearning`](mtltensorusage/machinelearning.md), the second element of `strides` is aligned to 64 bytes, and for any `i` larger than one, `strides[i]` is equal to `strides[i-1] * dimensions[i-1]`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensordescriptor/strides)*