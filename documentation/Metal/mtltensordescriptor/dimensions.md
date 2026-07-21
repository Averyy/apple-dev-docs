# dimensions

**Framework**: Metal  
**Kind**: property

An array of sizes, in elements, one for each dimension of the tensors you create with this descriptor.

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
var dimensions: MTLTensorExtents { get set }
```

#### Discussion

Every element of the array needs to be greater than `0`.

When [`dataType`](mtltensordescriptor/datatype.md) is [`MTLTensorDataType.int2`](mtltensordatatype/int2.md), [`MTLTensorDataType.uint2`](mtltensordatatype/uint2.md), [`MTLTensorDataType.int4`](mtltensordatatype/int4.md), [`MTLTensorDataType.uint4`](mtltensordatatype/uint4.md), [`MTLTensorDataType.metalFloat4e2m1`](mtltensordatatype/metalfloat4e2m1.md), [`MTLTensorDataType.metalFloat8e4m3`](mtltensordatatype/metalfloat8e4m3.md), [`MTLTensorDataType.metalFloat8e5m2`](mtltensordatatype/metalfloat8e5m2.md), or [`MTLTensorDataType.metalFloat8ue8m0`](mtltensordatatype/metalfloat8ue8m0.md):

- The dimension value of the array’s first element needs to be a multiple of 32 elements.
- The extents needs to have at least one dimension.

If the tensor has auxiliary planes, each dimension needs to be evenly divisible by its corresponding block factor.

The default value of this property is a rank one extents with size one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensordescriptor/dimensions)*