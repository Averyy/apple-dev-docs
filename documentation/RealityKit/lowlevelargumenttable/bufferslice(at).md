# bufferSlice(at:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns the buffer slice bound at the given index, or `nil` if the slot is unset.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func bufferSlice(at index: Int) -> LowLevelBufferSlice?
```

#### Return Value

The buffer slice at `index`, or `nil` if the slot is unoccupied.

## Parameters

- `index`: The slot index within the argument table’s buffer array.

## See Also

### Accessing buffer slices
- [func setBufferSlice(LowLevelBufferSlice, at: Int) throws(LowLevelRenderContextError)](./setbufferslice%28_,at%29.md)
  Binds a buffer slice to the slot at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelargumenttable/bufferslice(at:))*