# dimensions

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

An array of sizes, in elements, one for each dimension of this tensor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var dimensions: MTLTensorExtents { get }
```

#### Discussion

You are responsible for ensuring `dimensions` meets the following requirements:

- `dimensions[i]` must be greater than 0.
- If [`dataType`](mtltensor/datatype.md) is a format [`MTLTensorDataType`](mtltensordatatype.md), `dimensions[0]` must be a multiple of 32 elements.
- If the tensor has auxiliary planes, each dimension must be evenly divisible by its corresponding block factor.
- If [`dataType`](mtltensor/datatype.md) is a format [`MTLTensorDataType`](mtltensordatatype.md), or the tensor has auxiliary planes, the tensor must have rank 1 or higher.

The default value of this property is a rank one extents with size one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensor/dimensions)*