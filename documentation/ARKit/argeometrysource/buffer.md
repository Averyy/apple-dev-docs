# buffer

**Framework**: ARKit  
**Kind**: property

A Metal buffer that contains a list of vectors.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
var buffer: any MTLBuffer { get }
```

#### Discussion

Each vector in the buffer is of the type defined by [`format`](argeometrysource/format.md). Every vector may itself contain multiple scalars, defined by [`componentsPerVector`](argeometrysource/componentspervector.md).

The buffer’s [`storageMode`](https://developer.apple.com/documentation/Metal/MTLResource/storageMode) is [`MTLStorageMode.shared`](https://developer.apple.com/documentation/Metal/MTLStorageMode/shared) which allows it to be accessed on both, the CPU, and GPU.

## See Also

- [subscript(Int32) -> (Float, Float, Float)](argeometrysource/subscript(_:)-3v98f.md)
  Provides the source float triplet at the subscripted index.
- [subscript(Int32) -> CUnsignedChar](argeometrysource/subscript(_:)-7jf4y.md)
  Provides the number at the subscripted index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeometrysource/buffer)*