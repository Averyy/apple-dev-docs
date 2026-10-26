# init(offset:segmentLength:segmentCount:)

**Framework**: FSKit  
**Kind**: init  
**Role**: Initializer

Initializes a metadata range with the given properties.

**Availability**:
- macOS 15.4+

## Declaration

```swift
init(offset startOffset: off_t, segmentLength: UInt64, segmentCount: UInt64)
```

```objc
- (instancetype) initWithOffset:(off_t) startOffset segmentLength:(uint64_t) segmentLength segmentCount:(uint64_t) segmentCount;
```

## Parameters

- `startOffset`: The start offset of the range in bytes. Ensure this value is a multiple of the corresponding resource’s [`blockSize`](../fsblockdeviceresource/blocksize.md).
- `segmentLength`: The segment length in bytes. Ensure this value is a multiple of the corresponding resource’s [`blockSize`](../fsblockdeviceresource/blocksize.md).
- `segmentCount`: The number of segments in the range.

## See Also

### Creating a metadata range
- [+ rangeWithOffset:segmentLength:segmentCount:](./rangewithoffset_segmentlength_segmentcount_.md)
  Creates a metadata range with the given properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmetadatarange/init(offset:segmentlength:segmentcount:))*