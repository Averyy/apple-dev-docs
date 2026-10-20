# CMBlockBufferIsRangeContiguous(_:atOffset:length:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether the specified range within a block buffer is contiguous.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMBlockBufferIsRangeContiguous(_ theBuffer: CMBlockBuffer, atOffset offset: Int, length: Int) -> Bool
```

```c
extern Boolean CMBlockBufferIsRangeContiguous(CMBlockBufferRef theBuffer, size_t offset, size_t length);
```

#### Return Value

Returns true if the specified range is contiguous within the `CMBlockBuffer`, false otherwise. Also returns false if the `CMBlockBuffer` is `NULL` or empty.

#### Discussion

Determines whether the specified range within the given `CMBlockBuffer` is contiguous. If `CMBlockBufferGetDataPointer`() were called with the same parameters, the returned pointer would address the desired number of bytes.

## Parameters

- `theBuffer`: `CMBlockBuffer` to examine. Must not be `NULL`.
- `offset`: Offset within the buffer’s offset range.
- `length`: Desired number of bytes to access at offset. If zero, the number of bytes available at offset (dataLength – offset), contiguous or not, is used.

## See Also

### Inspecting a Block Buffer
- [func CMBlockBufferGetDataPointer(CMBlockBuffer, atOffset: Int, lengthAtOffsetOut: UnsafeMutablePointer<Int>?, totalLengthOut: UnsafeMutablePointer<Int>?, dataPointerOut: UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>?) -> OSStatus](./cmblockbuffergetdatapointer%28_,atoffset,lengthatoffsetout,totallengthout,datapointerout%29.md)
  Gains access to the data represented by a block buffer.
- [func CMBlockBufferGetDataLength(CMBlockBuffer) -> Int](./cmblockbuffergetdatalength%28_%29.md)
  Returns the total length of data that’s accessible by a block buffer.
- [func CMBlockBufferIsEmpty(CMBlockBuffer) -> Bool](./cmblockbufferisempty%28_%29.md)
  Returns a Boolean value that indicates whether the buffer is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbufferisrangecontiguous(_:atoffset:length:))*