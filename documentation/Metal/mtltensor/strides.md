# strides

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

An array of strides, in elements, one for each dimension of this tensor, if applicable.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var strides: MTLTensorExtents? { get }
```

#### Discussion

You are responsible for ensuring `strides` meets the following requirements:

- The first element of `strides` must be 1.
- If [`usage`](mtltensor/usage.md) contains [`machineLearning`](mtltensorusage/machinelearning.md), the second element of `strides` must be aligned to 64 bytes, and for any `i` larger than 1, `strides[i]` must equal `strides[i-1] * dimensions[i-1]`.
- If [`dataType`](mtltensor/datatype.md) is a format [`MTLTensorDataType`](mtltensordatatype.md), for any `i` greater than or equal to 1, `strides[i]` must be aligned to 128 bytes. This is not a requirement for non-format data types, but following this convention improves performance.

This property is non-nil only for tensors created from a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensor/strides)*