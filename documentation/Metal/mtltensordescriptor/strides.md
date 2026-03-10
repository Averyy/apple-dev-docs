# strides

**Framework**: Metal  
**Kind**: property

An array of strides, in elements, one for each dimension in the tensors you create with this descriptor, if applicable.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@NSCopying
var strides: MTLTensorExtents? { get set }
```

#### Discussion

You are responsible for ensuring `strides` meets the following requirements:

- The first element of `strides` is one.
- If [`usage`](mtltensordescriptor/usage.md) contains [`machineLearning`](mtltensorusage/machinelearning.md), the second element of `strides` is aligned to 64 bytes, and for any `i` larger than one, `strides[i]` is equal to `strides[i-1] * dimensions[i-1]`.
- If [`dataType`](mtltensordescriptor/datatype.md) is a sub-byte [`MTLTensorDataType`](mtltensordatatype.md), for any `i` greater than or equal to 1, `strides[i]` is aligned to 128 bytes. This is not a requirement for non-sub-byte data types, but following this convention improves performance.

Only set this property when creating tensors from a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensordescriptor/strides)*