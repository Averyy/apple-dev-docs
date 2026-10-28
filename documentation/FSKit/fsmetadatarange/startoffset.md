# startOffset

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The start offset of the range in bytes.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var startOffset: off_t { get }
```

```objc
@property (readonly) off_t startOffset;
```

## Discussion

Ensure this value is a multiple of the corresponding resource’s [`blockSize`](../fsblockdeviceresource/blocksize.md).

## See Also

### Accessing range properties
- [var segmentLength: UInt64](./segmentlength.md)
  The segment length in bytes.
- [var segmentCount: UInt64](./segmentcount.md)
  The number of segments in the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmetadatarange/startoffset)*