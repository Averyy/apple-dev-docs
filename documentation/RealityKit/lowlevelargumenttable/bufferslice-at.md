# bufferSlice(at:)

**Framework**: RealityKit  
**Kind**: method

Returns the buffer slice bound at the given index, or `nil` if the slot is unset.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func bufferSlice(at index: Int) -> LowLevelBufferSlice?
```

#### Return Value

The buffer slice at `index`, or `nil` if the slot is unoccupied.

## Parameters

- `index`: The slot index within the argument table’s buffer array.

## See Also

- [func setBufferSlice(LowLevelBufferSlice, at: Int) throws(LowLevelRenderContextError)](lowlevelargumenttable/setbufferslice(_:at:).md)
  Binds a buffer slice to the slot at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelargumenttable/bufferslice(at:))*