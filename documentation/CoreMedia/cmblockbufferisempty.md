# CMBlockBufferIsEmpty(_:)

**Framework**: Core Media  
**Kind**: func

Returns a Boolean value that indicates whether the buffer is empty.

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
func CMBlockBufferIsEmpty(_ theBuffer: CMBlockBuffer) -> Bool
```

#### Return Value

False if the `CMBlockBuffer` is `NULL`.

#### Discussion

Determines whether the given `CMBlockBuffer` is empty, i.e., devoid of any `memoryBlocks` or `CMBlockBuffer` references. Note that a `CMBlockBuffer` containing a not-yet allocated `memoryBlock` is not considered empty.

## Parameters

- `theBuffer`:   to examine. Must not be  .

## See Also

- [func CMBlockBufferGetDataPointer(CMBlockBuffer, atOffset: Int, lengthAtOffsetOut: UnsafeMutablePointer<Int>?, totalLengthOut: UnsafeMutablePointer<Int>?, dataPointerOut: UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>?) -> OSStatus](cmblockbuffergetdatapointer(_:atoffset:lengthatoffsetout:totallengthout:datapointerout:).md)
  Gains access to the data represented by a block buffer.
- [func CMBlockBufferGetDataLength(CMBlockBuffer) -> Int](cmblockbuffergetdatalength(_:).md)
  Returns the total length of data that’s accessible by a block buffer.
- [func CMBlockBufferIsRangeContiguous(CMBlockBuffer, atOffset: Int, length: Int) -> Bool](cmblockbufferisrangecontiguous(_:atoffset:length:).md)
  Returns a Boolean value that indicates whether the specified range within a block buffer is contiguous.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbufferisempty(_:))*