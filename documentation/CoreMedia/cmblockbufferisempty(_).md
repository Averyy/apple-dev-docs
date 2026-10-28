# CMBlockBufferIsEmpty(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

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

```c
extern Boolean CMBlockBufferIsEmpty(CMBlockBufferRef theBuffer);
```

## Return Value

False if the `CMBlockBuffer` is `NULL`.

## Discussion

Determines whether the given `CMBlockBuffer` is empty, i.e., devoid of any `memoryBlocks` or `CMBlockBuffer` references. Note that a `CMBlockBuffer` containing a not-yet allocated `memoryBlock` is not considered empty.

## Parameters

- `theBuffer`: `CMBlockBuffer` to examine. Must not be `NULL`.

## See Also

### Inspecting a Block Buffer
- [func CMBlockBufferGetDataPointer(CMBlockBuffer, atOffset: Int, lengthAtOffsetOut: UnsafeMutablePointer<Int>?, totalLengthOut: UnsafeMutablePointer<Int>?, dataPointerOut: UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>?) -> OSStatus](./cmblockbuffergetdatapointer%28_,atoffset,lengthatoffsetout,totallengthout,datapointerout%29.md)
  Gains access to the data represented by a block buffer.
- [func CMBlockBufferGetDataLength(CMBlockBuffer) -> Int](./cmblockbuffergetdatalength%28_%29.md)
  Returns the total length of data that’s accessible by a block buffer.
- [func CMBlockBufferIsRangeContiguous(CMBlockBuffer, atOffset: Int, length: Int) -> Bool](./cmblockbufferisrangecontiguous%28_,atoffset,length%29.md)
  Returns a Boolean value that indicates whether the specified range within a block buffer is contiguous.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbufferisempty(_:))*