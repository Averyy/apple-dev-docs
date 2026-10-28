# buffer

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A Metal buffer that contains a list of vectors.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+

## Declaration

```swift
var buffer: any MTLBuffer { get }
```

```objc
@property (nonatomic, strong, readonly) id<MTLBuffer> buffer;
```

## Discussion

Each vector in the buffer is of the type defined by [`format`](./format.md). Every vector may itself contain multiple scalars, defined by [`componentsPerVector`](./componentspervector.md).

The buffer’s [`storageMode`](../../Metal/mtlresource/storagemode.md) is [`MTLStorageMode.shared`](../../Metal/mtlstoragemode/shared.md) which allows it to be accessed on both, the CPU, and GPU.

## See Also

### Accessing Geometry
- [subscript(Int32) -> (Float, Float, Float)](./subscript%28_%29-3v98f.md)
  Provides the source float triplet at the subscripted index.
- [subscript(Int32) -> CUnsignedChar](./subscript%28_%29-7jf4y.md)
  Provides the number at the subscripted index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeometrysource/buffer)*