# init(offset:segmentLength:segmentCount:)

**Framework**: FSKit  
**Kind**: init

Initializes a metadata range with the given properties.

**Availability**:
- macOS 15.4+

## Declaration

```swift
init(offset startOffset: off_t, segmentLength: UInt64, segmentCount: UInt64)
```

## Parameters

- `startOffset`: The start offset of the range in bytes. Ensure this value is a multiple of the corresponding resource’s  .
- `segmentLength`: The segment length in bytes. Ensure this value is a multiple of the corresponding resource’s  .
- `segmentCount`: The number of segments in the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmetadatarange/init(offset:segmentlength:segmentcount:))*