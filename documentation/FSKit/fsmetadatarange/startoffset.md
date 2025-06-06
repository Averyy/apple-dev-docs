# startOffset

**Framework**: FSKit  
**Kind**: property

The start offset of the range in bytes.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var startOffset: off_t { get }
```

#### Discussion

Ensure this value is a multiple of the corresponding resource’s [`blockSize`](fsblockdeviceresource/blocksize.md).

## See Also

- [var segmentLength: UInt64](fsmetadatarange/segmentlength.md)
  The segment length in bytes.
- [var segmentCount: UInt64](fsmetadatarange/segmentcount.md)
  The number of segments in the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmetadatarange/startoffset)*