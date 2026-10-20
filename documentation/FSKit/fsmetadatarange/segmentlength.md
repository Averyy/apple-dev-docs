# segmentLength

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The segment length in bytes.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var segmentLength: UInt64 { get }
```

```objc
@property (readonly) uint64_t segmentLength;
```

#### Discussion

Ensure this value is a multiple of the corresponding resource’s [`blockSize`](../fsblockdeviceresource/blocksize.md).

## See Also

### Accessing range properties
- [var startOffset: off_t](./startoffset.md)
  The start offset of the range in bytes.
- [var segmentCount: UInt64](./segmentcount.md)
  The number of segments in the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmetadatarange/segmentlength)*