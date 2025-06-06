# CMBlockBufferGetDataLength(_:)

**Framework**: Core Media  
**Kind**: func

Returns the total length of data that’s accessible by a block buffer.

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
func CMBlockBufferGetDataLength(_ theBuffer: CMBlockBuffer) -> Int
```

#### Return Value

Returns the total data length available via this `CMBlockBuffer`, or zero if it is empty, `NULL` if invalid.

#### Discussion

Obtains the total data length reachable via a `CMBlockBuffer`. This total is the sum of the `dataLengths` of the `CMBlockBuffer's` memoryBlocks and buffer references. Note that the `dataLengths` are the portions of those constituents that this `CMBlockBuffer` subscribes to. This `CMBlockBuffer` presents a contiguous range of offsets from zero to its `totalDataLength` as returned by this routine.

## Parameters

- `theBuffer`:   to examine.

## See Also

- [func CMBlockBufferGetDataPointer(CMBlockBuffer, atOffset: Int, lengthAtOffsetOut: UnsafeMutablePointer<Int>?, totalLengthOut: UnsafeMutablePointer<Int>?, dataPointerOut: UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>?) -> OSStatus](cmblockbuffergetdatapointer(_:atoffset:lengthatoffsetout:totallengthout:datapointerout:).md)
  Gains access to the data represented by a block buffer.
- [func CMBlockBufferIsRangeContiguous(CMBlockBuffer, atOffset: Int, length: Int) -> Bool](cmblockbufferisrangecontiguous(_:atoffset:length:).md)
  Returns a Boolean value that indicates whether the specified range within a block buffer is contiguous.
- [func CMBlockBufferIsEmpty(CMBlockBuffer) -> Bool](cmblockbufferisempty(_:).md)
  Returns a Boolean value that indicates whether the buffer is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbuffergetdatalength(_:))*