# segmentLength

**Framework**: FSKit  
**Kind**: property

The segment length in bytes.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var segmentLength: UInt64 { get }
```

#### Discussion

Ensure this value is a multiple of the corresponding resource’s [`blockSize`](fsblockdeviceresource/blocksize.md).

## See Also

- [var startOffset: off_t](fsmetadatarange/startoffset.md)
  The start offset of the range in bytes.
- [var segmentCount: UInt64](fsmetadatarange/segmentcount.md)
  The number of segments in the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmetadatarange/segmentlength)*