# setBufferSlice(_:at:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Binds a buffer slice to the slot at the given index.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func setBufferSlice(_ bufferSlice: LowLevelBufferSlice, at index: Int) throws(LowLevelRenderContextError)
```

#### Discussion

> **Throws**: [`LowLevelRenderContextError`](../lowlevelrendercontexterror.md) if `index` is out of range or `bufferSlice` is incompatible with the slot.

## Parameters

- `bufferSlice`: The buffer slice to bind to the slot. Its size must be no smaller than the slot’s [`size`](./descriptor-swift.struct/buffer/size.md).
- `index`: The slot index within the argument table’s buffer array.

## See Also

### Accessing buffer slices
- [func bufferSlice(at: Int) -> LowLevelBufferSlice?](./bufferslice%28at%29.md)
  Returns the buffer slice bound at the given index, or `nil` if the slot is unset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelargumenttable/setbufferslice(_:at:))*