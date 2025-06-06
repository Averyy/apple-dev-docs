# CMBlockBufferGetDataPointer(_:atOffset:lengthAtOffsetOut:totalLengthOut:dataPointerOut:)

**Framework**: Core Media  
**Kind**: func

Gains access to the data represented by a block buffer.

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
func CMBlockBufferGetDataPointer(_ theBuffer: CMBlockBuffer, atOffset offset: Int, lengthAtOffsetOut: UnsafeMutablePointer<Int>?, totalLengthOut: UnsafeMutablePointer<Int>?, dataPointerOut: UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>?) -> OSStatus
```

#### Return Value

Returns `kCMBlockBufferNoErr` if data was accessible at the specified offset within the given `CMBlockBuffer`. Returns an error otherwise.

#### Discussion

Gains access to the data represented by a [`CMBlockBuffer`](cmblockbuffer.md). A pointer into a memory block is returned which corresponds to the offset within the `CMBlockBuffer`.  If `lengthAtOffset` is non `NULL`, the number of bytes addressable at the pointer is returned. This length-at-offset may be smaller than the number of bytes actually available starting at the offset if the `dataLength` of the `CMBlockBuffer` is covered by multiple memory blocks (a noncontiguous `CMBlockBuffer`). The caller can compare (`offset`+`lengthAtOffset`) with `totalLength` to determine whether the entire `CMBlockBuffer` has been referenced and whether it is possible to access the `CMBlockBuffer`’s data with a contiguous reference. The data pointer returned will remain valid as long as the original `CMBlockBuffer` is referenced - once the `CMBlockBuffer` is released for the last time, any pointers                into it will be invalid.

## Parameters

- `theBuffer`:   to operate on. Must not be 
- `offset`: Offset within the buffer’s offset range.
- `lengthAtOffsetOut`: On return, contains the amount of data available at the specified offset. May be  .
- `totalLengthOut`: On return, contains the block buffer’s total data length (from offset 0). May be  .
- `dataPointerOut`: On return, contains a pointer to the data byte at the specified offset;   bytes are available at this address. May be  .

## See Also

- [func CMBlockBufferGetDataLength(CMBlockBuffer) -> Int](cmblockbuffergetdatalength(_:).md)
  Returns the total length of data that’s accessible by a block buffer.
- [func CMBlockBufferIsRangeContiguous(CMBlockBuffer, atOffset: Int, length: Int) -> Bool](cmblockbufferisrangecontiguous(_:atoffset:length:).md)
  Returns a Boolean value that indicates whether the specified range within a block buffer is contiguous.
- [func CMBlockBufferIsEmpty(CMBlockBuffer) -> Bool](cmblockbufferisempty(_:).md)
  Returns a Boolean value that indicates whether the buffer is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbuffergetdatapointer(_:atoffset:lengthatoffsetout:totallengthout:datapointerout:))*