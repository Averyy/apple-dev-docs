# setBufferSlice(_:at:)

**Framework**: RealityKit  
**Kind**: method

Binds a buffer slice to the slot at the given index.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func setBufferSlice(_ bufferSlice: LowLevelBufferSlice, at index: Int) throws(LowLevelRenderContextError)
```

#### Discussion

> **Note**: [`LowLevelRenderContextError`](lowlevelrendercontexterror.md) if `index` is out of range or `bufferSlice` is incompatible with the slot.

## Parameters

- `bufferSlice`: The buffer slice to bind to the slot.
- `index`: The slot index within the argument table’s buffer array.

## See Also

- [func bufferSlice(at: Int) -> LowLevelBufferSlice?](lowlevelargumenttable/bufferslice(at:).md)
  Returns the buffer slice bound at the given index, or `nil` if the slot is unset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelargumenttable/setbufferslice(_:at:))*