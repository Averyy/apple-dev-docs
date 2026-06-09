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

You are responsible for ensuring `dimensions` meets the following requirements:

- `dimensions[i]` must be greater than 0.
- If [`dataType`](mtltensordescriptor/datatype.md) is a format [`MTLTensorDataType`](mtltensordatatype.md), `dimensions[0]` must be a multiple of 32 elements.

The default value of this property is a rank one extents with size one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensordescriptor/dimensions)*